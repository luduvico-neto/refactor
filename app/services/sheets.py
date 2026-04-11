import pandas


def read_excel_file(
    file_path: str,
    sheet_name: str,
    skip_rows: int,
    skip_footer: int,
) -> pandas.DataFrame:
    """Reads an Excel file and returns a DataFrame."""
    return pandas.read_excel(
        file_path=file_path,
        sheet_name=sheet_name,
        skiprows=skip_rows,
        skipfooter=skip_footer,
    )


def normalize_dataframe(
    file_path: str,
    sheet_name: str,
    skip_rows: int,
    skip_footer: int,
) -> pandas.DataFrame:
    data_frame = read_excel_file(
        file_path=file_path,
        sheet_name=sheet_name,
        skip_rows=skip_rows,
        skip_footer=skip_footer,
    )

    ...
