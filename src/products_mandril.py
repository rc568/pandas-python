from pathlib import Path
import pandas as pd

from helpers import array_string_to_string

gastos_columns = {
    'Stock': 'quantityInStock',
    'Precio Compra': 'purchasePrice',
}

turso_columns = {
    'producto': 'name',
    'precioVenta': 'price',
    'descripcion': 'description',
    'categoria_id': 'categoryId',
    'catalogo_id': 'catalogId',
    'status': 'isActive',
}


def products_mandril(products_file, gastos_mandril, output_dir):
    """
    Convert the .csv (from TursoDb) to json file for seed a database

    Args:
        products_file: Path for csv file
        gastos_mandril: Path for xlsx file
        output_dir: Output directory for files (images-products.json, products.json)

    Returns:
        void
    """

    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)

    new_images: list[dict] = []

    df_gastos_lista = pd.read_excel(gastos_mandril, sheet_name='LISTA', index_col='Código').rename(
        columns=gastos_columns
    )
    filter_valid_code = df_gastos_lista.index.str.match(pat='^MI(\d{3})$', na=False)
    df_gastos_lista.drop(index=df_gastos_lista[~filter_valid_code].index, inplace=True)

    df_turso = (
        pd.read_csv(
            products_file,
            usecols=lambda x: x not in ['subcategoria', 'stock'],
            index_col='codigo',
        )
        .rename(columns=turso_columns)
        .astype({'isActive': bool})
    )

    # This Line is necessary to reset the id count (codes MI217-MI218-MI219 where deleted)
    df_turso['id'] = range(1, len(df_turso) + 1)
    df_turso['categoryId'] = df_turso['categoryId'].apply(lambda x: x + 1)
    df_turso['catalogId'] = df_turso['catalogId'].apply(lambda x: x + 1)

    for _, row in df_turso.iterrows():
        images = array_string_to_string(getattr(row, 'images', ''))
        for image in images:
            new_images.append({'imageUrl': image, 'productVariantId': row['id']})

    df_merge = (
        pd.merge(
            df_turso,
            df_gastos_lista[['quantityInStock', 'purchasePrice']],
            how='left',
            left_index=True,
            right_index=True,
        )
        .reset_index()
        .rename(columns={'codigo': 'code'})
    )

    df_product = df_merge[['name', 'slug', 'description', 'isActive', 'categoryId', 'catalogId']]
    df_product_variant = df_merge[['code', 'price', 'quantityInStock', 'purchasePrice', 'isActive']]
    df_images = pd.DataFrame(new_images)

    df_images.to_json(output_dir.joinpath('images-products.json'), orient='records', force_ascii=False)
    df_product.to_json(output_dir.joinpath('product.json'), orient='records', force_ascii=False)
    df_product_variant.to_json(output_dir.joinpath('product-variant.json'), orient='records', force_ascii=False)
