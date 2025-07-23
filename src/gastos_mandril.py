import pandas as pd
import json

from helpers import array_string_to_string

INPUT_FILE = "data/GASTOS-MANDRIL_20250722.csv"
OUTPUT_FILE = "output/images-products.json"

rename_products_columns = {
    "codigo": "code",
    "producto": "name",
    "precioVenta": "price",
    "descripcion": "description",
    "categoria_id": "categoryId",
    "status": "isActive",
}

new_images: list[dict] = []

df = pd.read_csv(INPUT_FILE, usecols=lambda x: x in ["Código", "Producto", "Fecha"])

df_unique_codes_product = df.drop_duplicates(subset=["Código", "Producto"]).sort_values(
    by="Código", ascending=True
)

df_duplicates_codes_products = df_unique_codes_product[
    df_unique_codes_product["Código"].duplicated(keep=False)
]

df_unique_codes_product.to_csv("data/unique_codes.csv")
df_duplicates_codes_products.to_csv("data/duplicate_codes.csv")


# unique_codes = df[["Código", "Producto"]].nunique()
# unique_codes_series = pd.Series(unique_codes)

# unique_codes_series.to_csv("data/unique_codes.csv")
