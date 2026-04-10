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
    ) -> list[tuple[int, float, str]]:
        """Returns a ranked list of (index, score, word) sorted by descending similarity."""
        word_embedding = self.embed_word(word)
        list_embeddings = self.embed_list(_list)

        similarities = self.model.similarity(word_embedding, list_embeddings)[0]
        ranked = sorted(
            enumerate(similarities.tolist()),
            key=lambda x: x[1],
            reverse=True,
        )
        return [(idx, score, _list[idx]) for idx, score in ranked]

    def find_most_similar(self, word: str, _list: list[str]) -> tuple[int, float, str]:
        """Returns the (index, score, word) of the most similar word above the cutoff, or None."""
        ranked = self.compare_word(word, _list)
        if ranked and ranked[0][1] >= self.cutoff:
            return ranked[0]
        return ranked[0] if ranked else None
