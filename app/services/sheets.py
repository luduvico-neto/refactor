import pandas
from loguru import logger

from models.models import SheetMetadata
from utils.utils import mapper


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
            if column.name != "to_void"
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
