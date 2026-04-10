from .lifespan import set_transformer, set_dependencies
from loguru import logger


def init_core() -> None:
    logger.info("Loading the sentence transformer model...")
    set_transformer()
    set_dependencies()


__all__ = ["init_core"]

init_core()
