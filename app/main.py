from loguru import logger

from core import lifespan
from dependencies.dependencies import load_dataframe

from models.models import DataFrame

df = load_dataframe(r"app\database\dummy_df.json")

with lifespan() as fuzzy_checker:

    cities = [data.city for data in df.data]
    ranked = fuzzy_checker.compare_word("São paulo", cities)

    list_embedded = fuzzy_checker.embed_list(cities)

    new_dataframe_data = [
        {
            "neighborhood": data.neighborhood,
            "city": data.city,
            "state": data.state,
            "average_price": data.average_price,
            "ad_quantity": data.ad_quantity,
            "days_in_market": data.days_in_market,
            "embedding": list_embedded[i],
        }
        for i, data in enumerate(df.data)
    ]

    new_dataframe = DataFrame(data=new_dataframe_data)

    # Find the most similar neighborhood to "São pulo" using embeddings
    idx, score, name = ranked[0]
    logger.info(f"Most similar: '{name}' (index={idx}, score={score:.4f})")
    logger.info(f"Top 5: {[(name, f'{score:.4f}') for _, score, name in ranked[:5]]}")
