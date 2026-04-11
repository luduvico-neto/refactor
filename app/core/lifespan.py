from collections.abc import Generator
from contextlib import contextmanager

from loguru import logger
from sentence_transformers import SentenceTransformer

from services.probability import Transformer


@contextmanager
def lifespan() -> Generator[Transformer]:
    logger.info("Loading the all-MiniLM-L6-v2 sentence transformer instance...")
    sentence_model = SentenceTransformer("all-MiniLM-L6-v2")
    fuzzy_checker = Transformer(cutoff=0.9, _model=sentence_model)
    logger.info("Application startup complete.")

    yield fuzzy_checker

    logger.info("Shutting down application...")
