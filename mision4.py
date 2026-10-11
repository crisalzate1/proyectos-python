import pandas as pd
import os

ARCHIVO_VENTAS = "ventas.csv"
ARCHIVO_REPORTE_PANDAS = "reporte_pandas.csv"


def main():
    if not os.path.exists(ARCHIVO_VENTAS):
        print(f"Error: No existe el archivo {ARCHIVO_VENTAS}")
        return

    # 1. Cargar el CSV en un DataFrame
    df = pd.read_csv(ARCHIVO_VENTAS)

    # 2. Crear columna calculada (Total Venta)
    df["total_venta"] = df["cantidad"] * df["precio_unitario"]

    # 3. Métricas principales
    ingresos_totales = df["total_venta"].sum()
    promedio_venta = df["total_venta"].mean()
    producto_top = df.loc[df["cantidad"].idxmax()]["producto"]

    # 4. Agregación por Categoría (Group By)
    reporte_categoria = df.groupby("categoria")["total_venta"].sum().reset_index()

    # Mostrar reporte en consola
    print("\n" + "="*40)
    print("--- REPORTE DE VENTAS (PANDAS) ---")
    print("="*40)
    print(f"Ingresos Totales : ${ingresos_totales:,.2f}")
    print(f"Venta Promedio   : ${promedio_venta:,.2f}")
    print(f"Producto Top     : {producto_top}")

    print("\nIngresos por Categoría:")
    for _, row in reporte_categoria.iterrows():
        print(f"  - {row['categoria']}: ${row['total_venta']:,.2f}")

    # 5. Filtrar y Exportar ventas >= $100
    df_altas = df[df["total_venta"] >= 100]
    df_altas.to_csv(ARCHIVO_REPORTE_PANDAS, index=False)
    print(f"\nArchivo '{ARCHIVO_REPORTE_PANDAS}' generado con {len(df_altas)} registros.")


if __name__ == "__main__":
    main()