from services.probability import calculate_most_likely
from dependencies.dependencies import load_dataframe


dataframe = load_dataframe(r"app\database\dummy_df.json")

result = calculate_most_likely([data.city for data in dataframe.data])

print(result)
