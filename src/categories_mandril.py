import pandas as pd
import json

INPUT_FILE = "data/categories.csv"
OUTPUT_FILE = "output/categories.json"

df = pd.read_csv(INPUT_FILE, usecols=lambda x: x != "id")

# This Line is necessary because index starts in 1 (postgres serial smallint)
df["parent_id"] = df["parent_id"].apply(lambda x: x + 1)

df = df.astype({"parent_id": "Int64"}).rename(columns={"parent_id": "parentId"})


data = df.to_dict(orient="records")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Successfully converted '{INPUT_FILE}' to '{OUTPUT_FILE}'")
