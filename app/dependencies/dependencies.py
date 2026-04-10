import json
from sentence_transformers import SentenceTransformer

from models.models import DataFrame

from loguru import logger


def load_dataframe(file_path: str) -> DataFrame:
    logger.info("Loading the dataframe...")
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return DataFrame.model_validate(data)


class FuzzyChecker:
    def __init__(self, cutoff: float, _model: SentenceTransformer = None):
        self.cutoff = cutoff
        self.model = _model

    def compare_word(
        self, word: str, _list: list[str]
    ) -> list[dict[str, list[list[float]]]]:
        """It returns the hank of the most similar word in the list if the similarity is above the cutoff"""
        candidate = self.model.encode([word], convert_to_tensor=True)
        candidates = self.model.encode(_list, convert_to_tensor=True)

        result = self.model.similarity(candidate, candidates)
        return result
