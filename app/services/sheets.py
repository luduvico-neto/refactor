import pandas
from loguru import logger

from models.models import SheetMetadata
from utils.utils import mapper
from services.probability import get_distinct_values
from core.lifespan import lifespan


def normalize_dataframe(
    metadata: SheetMetadata,
) -> pandas.DataFrame:

    try:
        logger.info("Getting all columns...")
        all_columns = [column.name for column in metadata.creation_metadata.columns]

        logger.info("Getting target columns...")
        target_columns = [
            column.name
            for column in metadata.creation_metadata.columns
            if column.name != "void"
        ]

        logger.info("Creating column mapper...")
        column_mapper = {
            column.name: mapper(column.parser)
            for column in metadata.creation_metadata.columns
        }

        logger.info("Reading excel file...")
        dataframe = pandas.read_excel(
            metadata.creation_metadata.file_path,
            sheet_name=metadata.creation_metadata.sheet_name,
            skiprows=metadata.creation_metadata.skip_rows,
            skipfooter=metadata.creation_metadata.skip_footer,
            names=all_columns,
            converters=column_mapper,
            header=None,
        )

        dataframe = dataframe[target_columns]

        logger.info("Dataframe normalization complete.")
    except Exception as e:
        logger.error(f"Error normalizing dataframe: {e}")
        raise e
    return dataframe


def refactor_sheet(
    extraction_metadata: dict,
    output_path: str,
    cutoffs: list[float] = [0.9, 0.88],
) -> pandas.DataFrame:
    """Loads, normalizes by probability, and exports a refactored xlsx.

    Args:
        extraction_metadata: Dict payload for SheetMetadata.creation_metadata.
        output_path: Path for the refactored xlsx output.
        cutoffs: One cutoff per normalization pass.
    """
    metadata = SheetMetadata(creation_metadata=extraction_metadata)
    dataframe = normalize_dataframe(metadata)

    columns_to_normalize = [
        column.name
        for column in metadata.creation_metadata.columns
        if column.normalize
    ]

    if not columns_to_normalize:
        logger.info("No columns flagged for normalization.")
        dataframe.to_excel(output_path, index=False)
        return dataframe

    with lifespan() as transformer:
        for pass_number, cutoff in enumerate(cutoffs, start=1):
            transformer.cutoff = cutoff
            logger.info(f"Pass {pass_number}/{len(cutoffs)} (cutoff={cutoff})")

            for column_name in columns_to_normalize:
                values = dataframe[column_name].dropna().astype(str).tolist()
                counted_values = get_distinct_values(values)
                _, depara = transformer.deduplicate(counted_values)

                if depara:
                    dataframe[column_name] = dataframe[column_name].replace(depara)

    dataframe.to_excel(output_path, index=False)
    logger.info(f"Refactored dataframe saved to: {output_path}")
    return dataframe
