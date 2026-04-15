import json
from pathlib import Path

from sentence_transformers import SentenceTransformer
from collections import Counter

from typing import Annotated


def get_distinct_values(targets: list[str]) -> dict[str, int]:
    """It gets a list of values and returns"""
    if not targets:
        return "No targets provided"

    hanks = Counter(targets)

    most_common = hanks.most_common()
    return most_common


class Transformer:
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

    """N similarity list"""

    def similarity_list(
        self, _list: list[list[float]], _list2: list[list[float]]
    ) -> list[list[float]]:
        similarity_matrix = self.model.similarity(_list, _list2)
        return similarity_matrix

    def deduplicate(
        self,
        counted_values: Annotated[
            list[tuple[str, int]], "List of distinct (value, count) pairs"
        ],
        mapping_path: str = None,
    ) -> tuple[list[tuple[str, int]], dict[str, str]]:
        if not counted_values:
            return [], {}

        values = [v for v, _ in counted_values]
        counts = {v: c for v, c in counted_values}

        embeddings = self.embed_list(values)
        similarity_matrix = self.similarity_list(embeddings, embeddings)

        visited = set()
        result = []
        depara = {}

        for i in range(len(values)):
            if i in visited:
                continue

            group = [i]
            for j in range(i + 1, len(values)):
                if j in visited:
                    continue
                if similarity_matrix[i][j].item() >= self.cutoff:
                    group.append(j)

            canonical = max(group, key=lambda idx: counts[values[idx]])
            visited.update(group)
            result.append((values[canonical], counts[values[canonical]]))

            for idx in group:
                if idx != canonical:
                    depara[values[idx]] = values[canonical]

        if mapping_path:
            Path(mapping_path).parent.mkdir(parents=True, exist_ok=True)
            with open(mapping_path, "w", encoding="utf-8") as f:
                json.dump(depara, f, ensure_ascii=False, indent=2)

        return result, depara
