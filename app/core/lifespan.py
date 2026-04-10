from sentence_transformers import SentenceTransformer
from dependencies.dependencies import FuzzyChecker

from loguru import logger


TRANSFORMER: SentenceTransformer | None = None


def set_transformer() -> None:
    logger.info("Loading the all-MiniLM-L6-v2 sentence transformer instance...")
    sentence_model = SentenceTransformer("all-MiniLM-L6-v2")

    fuzzy_model = FuzzyChecker(cutoff=0.9, _model=sentence_model)
    global TRANSFORMER
    TRANSFORMER = fuzzy_model


def set_dependencies() -> None:
    import dependencies
