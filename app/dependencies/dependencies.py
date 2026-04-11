import json
from loguru import logger

from models.models import DataFrame

from services.probability import Transformer


def load_dataframe(file_path: str) -> DataFrame:
    logger.info("Loading the dataframe...")
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return DataFrame.model_validate(data)
