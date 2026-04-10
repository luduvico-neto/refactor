from dependencies.dependencies import load_dataframe, FuzzyChecker

response = load_dataframe("database/dummy_df.json")
checker = FuzzyChecker(cutoff=0.9)

for field in ["neighborhood", "city", "state"]:
    values = [getattr(row, field) for row in response.data]
    misspelled = checker.find_misspelled(values)
    if misspelled:
        print(f"\n=== {field.upper()} ===")
        for wrong, correct in misspelled.items():
            print(f"  '{wrong}' -> '{correct}'")
