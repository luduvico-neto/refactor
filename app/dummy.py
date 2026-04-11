from services.probability import get_distinct_values
from dependencies.dependencies import load_dataframe

from core.lifespan import lifespan

dataframe = load_dataframe(r"app\database\dummy_df.json")

counted_values = get_distinct_values([data.city for data in dataframe.data])

print("Distinct values with counts:", counted_values)

with lifespan() as transformer:
    deduplicated = transformer.deduplicate(
        counted_values,
        mapping_path=r"app\database\depara.json",
    )

    print("Deduplicated values:", deduplicated)
