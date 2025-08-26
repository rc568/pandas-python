from gastos_mandril import gastos_mandril
from products_mandril import products_mandril

INPUT_FILE_CATEGORIES = 'src/data/categories.csv'
INPUT_FILE_PRODUCTS = 'src/data/csv-from-turso/products.csv'
INPUT_FILE_GASTOS = 'src/data/GASTOS-MANDRIL.xlsm'
INPUT_FILE_GASTOS_VENTAS = 'src/output/gastos/VENTAS.csv'
INPUT_FILE_GASTOS_LISTA = 'src/output/gastos/LISTA.csv'
OUTPUT_DIR = 'src/output/'
OUTPUT_DIR_GASTOS = 'src/output/gastos_mandril'

if __name__ == '__main__':
    products_mandril(INPUT_FILE_PRODUCTS, INPUT_FILE_GASTOS, OUTPUT_DIR)
    # gastos_mandril(INPUT_FILE_GASTOS_LISTA, INPUT_FILE_GASTOS_VENTAS, OUTPUT_DIR_GASTOS)
