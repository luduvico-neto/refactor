from collections import Counter


def calculate_most_likely(targets: list[str]) -> str:
    if not targets:
        return "No targets provided"

    hanks = Counter(targets)

    most_common = hanks
    return most_common
