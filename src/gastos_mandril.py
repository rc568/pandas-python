from pathlib import Path
import pandas as pd


def gastos_mandril(lista_file, ventas_file, output_dir):
    """
    Analysis of gastos_mandril file (ventas)
    """

    output_dir = Path(output_dir)

    df_ventas = pd.read_csv(
        ventas_file, usecols=lambda x: x in ["Código", "Producto", "Fecha"]
    )
    df_lista = pd.read_csv(lista_file, usecols=lambda x: x in ["Código", "Producto"])

    df_unique_codes_product = df_ventas.drop_duplicates(
        subset=["Código", "Producto"]
    ).sort_values(by="Código", ascending=True)

    df_duplicates_codes_products = df_unique_codes_product[
        df_unique_codes_product["Código"].duplicated(keep=False)
    ]

    codigos_lista = set(df_lista["Código"].unique())
    codigos_ventas = set(df_ventas["Código"].unique())

    codigo_unicos_ventas = sorted(codigos_ventas - codigos_lista)
    df_codigo_unicos_ventas = (
        df_ventas[df_ventas["Código"].isin(codigo_unicos_ventas)]
        .drop_duplicates(subset=["Código"])
        .sort_values(by="Código", ascending=True)
    )

    print(codigo_unicos_ventas, len(codigo_unicos_ventas))
    print(df_codigo_unicos_ventas)

    # TO CSV
    # df_unique_codes_product.to_csv(output_dir / "unique_codes.csv", encoding='utf-8-sig')
    # df_duplicates_codes_products.to_csv(output_dir / "duplicate_codes.csv", encoding='utf-8-sig')
