import pandas as pd
import json

from helpers import array_string_to_string

INPUT_FILE = "data/products.csv"
OUTPUT_FILE_IMAGES = "output/images-products.json"
OUTPUT_FILE_PRODUCTS = "output/products.json"

rename_products_columns = {
    "codigo": "code",
    "producto": "name",
    "precioVenta": "price",
    "descripcion": "description",
    "categoria_id": "categoryId",
    "status": "isActive",
}

new_images: list[dict] = []

df = pd.read_csv(INPUT_FILE, usecols=lambda x: x not in ["subcategoria", "catalogo_id"])
# This Line is necessary to reset the id count (rows 160-161-162 where deleted)
df["id"] = range(1, len(df) + 1)
df["categoria_id"] = df["categoria_id"].apply(lambda x: x + 1)

for _, row in df.iterrows():
    images = array_string_to_string(getattr(row, "images", ""))
    for image in images:
        new_images.append({"imageUrl": image, "productId": row["id"]})


df_products = (
    df.drop(columns=["id", "images"])
    .rename(columns=rename_products_columns)
    .astype({"isActive": bool})
    .copy()
)

df_images = pd.DataFrame(new_images)

# TO CSV
# df_images.to_csv("output/products.csv", index=False)


# TO JSON
data_images = df_images.to_dict(orient="records")
data_products = df_products.to_dict(orient="records")

with open(OUTPUT_FILE_IMAGES, "w", encoding="utf-8") as f:
    json.dump(data_images, f, ensure_ascii=False, indent=4)

with open(OUTPUT_FILE_PRODUCTS, "w", encoding="utf-8") as f:
    json.dump(data_products, f, ensure_ascii=False, indent=4)
