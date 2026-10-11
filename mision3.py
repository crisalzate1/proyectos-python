import csv
import os

ARCHIVO_VENTAS = "ventas.csv"
ARCHIVO_REPORTE_ALTAS = "ventas_altas.csv"


def cargar_ventas():
    if not os.path.exists(ARCHIVO_VENTAS):
        print(f"Error: El archivo {ARCHIVO_VENTAS} no existe.")
        return []

    ventas = []
    with open(ARCHIVO_VENTAS, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            ventas.append({
                "id": int(row["id"]),
                "producto": row["producto"],
                "categoria": row["categoria"],
                "cantidad": int(row["cantidad"]),
                "precio_unitario": float(row["precio_unitario"]),
                "total_venta": int(row["cantidad"]) * float(row["precio_unitario"])
            })
    return ventas


def analizar_ventas(ventas):
    if not ventas:
        print("No hay ventas para analizar.")
        return

    ingresos_totales = sum(v["total_venta"] for v in ventas)
    producto_mas_vendido = max(ventas, key=lambda v: v["cantidad"])
    
    categorias = {}
    for v in ventas:
        cat = v["categoria"]
        categorias[cat] = categorias.get(cat, 0) + v["total_venta"]

    print("\n" + "="*35)
    print("--- REPORTE DE ANALISIS DE VENTAS ---")
    print("="*35)
    print(f"Ingresos Totales: ${ingresos_totales:,.2f}")
    print(f"Producto mas vendido: {producto_mas_vendido['producto']} ({producto_mas_vendido['cantidad']} unidades)")
    
    print("\nIngresos por Categoria:")
    for cat, total in categorias.items():
        print(f"  - {cat}: ${total:,.2f}")


def exportar_ventas_altas(ventas, limite=100):
    ventas_filtradas = [v for v in ventas if v["total_venta"] >= limite]

    with open(ARCHIVO_REPORTE_ALTAS, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "producto", "categoria", "cantidad", "precio_unitario", "total_venta"])
        for v in ventas_filtradas:
            writer.writerow([v["id"], v["producto"], v["categoria"], v["cantidad"], v["precio_unitario"], v["total_venta"]])

    print(f"\nSe exporto el archivo '{ARCHIVO_REPORTE_ALTAS}' con {len(ventas_filtradas)} ventas mayores o iguales a ${limite}.")


def main():
    ventas = cargar_ventas()
    analizar_ventas(ventas)
    exportar_ventas_altas(ventas, limite=100)


if __name__ == "__main__":
    main()