import json
from loguru import logger
from sentence_transformers import SentenceTransformer

from models.models import DataFrame


def load_dataframe(file_path: str) -> DataFrame:
    logger.info("Loading the dataframe...")
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return DataFrame.model_validate(data)


class FuzzyChecker:
    def __init__(
        self,
        cutoff: float,
        _model: SentenceTransformer = None,
    ):
        self.cutoff = cutoff
        self.model = _model

    def embed_list(self, _list: list[str]) -> list[list[float]]:
        embedded_list = self.model.encode(_list, convert_to_tensor=True)
        return embedded_list

    def embed_word(self, word: str) -> list[list[float]]:
        embed_word = self.model.encode(word, convert_to_tensor=True)
        return embed_word

    def compare_word(
        self,
        word: str,
        _list: list[str],
    ) -> list[dict[str, list[list[float]]]]:
        """It returns the hank of the most similar word in the list if the similarity is above the cutoff"""
        word_candidate = self.embed_word(word)
        list_canditates = self.embed_list(_list)

        result = self.model.similarity(word_candidate, list_canditates)
        return {"resute": result}


def get_fuzzy_checker(): ...
