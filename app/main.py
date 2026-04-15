from services.sheets import refactor_sheet

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

dataframe = refactor_sheet(
    extraction_metadata=extraction_metadata,
    output_path=r"database\dataframe_refatorado.xlsx",
)

print(dataframe)
