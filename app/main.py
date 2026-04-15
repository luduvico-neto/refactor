from services.sheets import refactor_sheet

extraction_metadata = {
    "file_path": r"C:\Users\luduvico.neto\Documents - Copia\dummy_20mil_dados.xlsx",
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
            "name": "void",
            "parser": "to_void",
        },
        {
            "name": "cidade_uf",
            "parser": "to_str",
            "normalize": True,
        },
        {
            "name": "bairro",
            "parser": "to_str",
            "normalize": True,
        },
        {
            "name": "incorporadora",
            "parser": "to_str",
            "normalize": True,
        },
        {
            "name": "empreendimento",
            "parser": "to_str",
            "normalize": True,
        },
        {
            "name": "dormitorios",
            "parser": "to_int",
        },
        {
            "name": "tipo_un",
            "parser": "to_str",
            "normalize": True,
        },
        {
            "name": "metragem_privativa",
            "parser": "to_float",
        },
        {
            "name": "unidades_totais",
            "parser": "to_int",
        },
        {
            "name": "disponiveis",
            "parser": "to_int",
        },
        {
            "name": "vendas_mes",
            "parser": "to_int",
        },
    ],
}

dataframe = refactor_sheet(
    extraction_metadata=extraction_metadata,
    output_path=r"database\dataframe_refatorado.xlsx",
)

print(dataframe)
