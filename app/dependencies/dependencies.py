import json
from collections import Counter
from difflib import get_close_matches

from models.models import DataFrame


def load_dataframe(file_path: str) -> DataFrame:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return DataFrame.model_validate(data)


class FuzzyChecker:
    def __init__(self, cutoff: float = 0.8):
        self.cutoff = cutoff

    def _effective_cutoff(self, name: str) -> float:
        length = len(name)
        if length <= 5:
            return max(self.cutoff, 0.95)
        if length <= 8:
            return max(self.cutoff, 0.88)
        return self.cutoff

    def find_misspelled(self, values: list[str]) -> dict[str, str]:
        freq = Counter(values)
        canonical = sorted(freq, key=freq.get, reverse=True)
        misspelled: dict[str, str] = {}

        for name in canonical:
            if name in misspelled:
                continue
            cutoff = self._effective_cutoff(name)
            matches = get_close_matches(name, canonical, n=10, cutoff=cutoff)
            best = max(matches, key=lambda m: freq[m])
            for match in matches:
                if match != best and match not in misspelled:
                    misspelled[match] = best

        return misspelled
