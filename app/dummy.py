from services.sheets import normalize_dataframe
from models.models import SheetMetadata

extraction_metadata = {
    "file_path": r"C:\Users\luduvico.neto\Documents - Copia\dados planilha.xlsx",
    "sheet_name": "dados",
    "skip_rows": 4,
    "skip_footer": 1,
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
            "name": "nome",
            "parser": "to_str",
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
