from categories_mandril import categories_mandril
from gastos_mandril import gastos_mandril
from gastos_mandril_to_csv import gastos_mandril_to_csv
from products_mandril import products_mandril

INPUT_FILE_CATEGORIES = "src/data/categories.csv"
INPUT_FILE_PRODUCTS = "src/data/products.csv"
INPUT_FILE_GASTOS = "src/data/GASTOS-MANDRIL_20250722.xlsm"
INPUT_FILE_GASTOS_VENTAS = "src/output/gastos/VENTAS.csv"
INPUT_FILE_GASTOS_LISTA = "src/output/gastos/LISTA.csv"
OUTPUT_DIR = "src/output/"
OUTPUT_DIR_GASTOS = "src/output/gastos"


if __name__ == "__main__":
    # products_mandril(INPUT_FILE_PRODUCTS, OUTPUT_DIR)
    # categories_mandril(INPUT_FILE_CATEGORIES, OUTPUT_DIR)
    # gastos_mandril_to_csv(INPUT_FILE_GASTOS, OUTPUT_DIR_GASTOS)
    gastos_mandril(INPUT_FILE_GASTOS_LISTA, INPUT_FILE_GASTOS_VENTAS, OUTPUT_DIR_GASTOS)
