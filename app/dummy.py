from services.sheets import normalize_dataframe
from services.probability import get_distinct_values
from models.models import SheetMetadata
from core.lifespan import lifespan

extraction_metadata = {
    "file_path": r"C:\Users\luduvico.neto\Documents - Copia\dados planilha.xlsx",
    "sheet_name": "dados",
    "skip_rows": 4,
    "skip_footer": 0,
    "columns": [
        {
            "name": "void",
            "parser": "to_void",
        },
        {
            "name": "void",
            "parser": "to_void",
        },
        {
            "name": "cidade",
            "parser": "to_str",
            "normalize": True,
        },
        {
            "name": "estado",
            "parser": "to_str",
            "normalize": True,
        },
        {
            "name": "nome",
            "parser": "to_str",
            "normalize": True,
        },
        {
            "name": "idade",
            "parser": "to_int",
        },
        {
            "name": "vendas",
            "parser": "to_int",
        },
        {
            "name": "void",
            "parser": "to_void",
        },
        {
            "name": "void",
            "parser": "to_void",
        },
    ],
}

metadata = SheetMetadata(creation_metadata=extraction_metadata)

dataframe = normalize_dataframe(metadata)

print(dataframe)

columns_to_normalize = [
    column.name
    for column in metadata.creation_metadata.columns
    if column.normalize
]

with lifespan() as transformer:
    for column_name in columns_to_normalize:
        print(f"\n--- Normalizing column: {column_name} ---")

        values = dataframe[column_name].dropna().astype(str).tolist()
        counted_values = get_distinct_values(values)
        print("Distinct values with counts:", counted_values)

        deduplicated, depara = transformer.deduplicate(counted_values)
        print("Deduplicated values:", deduplicated)

        if depara:
            dataframe[column_name] = dataframe[column_name].replace(depara)

output_path = r"database\dataframe_refatorado.xlsx"
dataframe.to_excel(output_path, index=False)
print(f"\nRefactored dataframe saved to: {output_path}")
print(dataframe)
