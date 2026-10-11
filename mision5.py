import sqlite3
import os

DB_NAME = "inventario.db"


def inicializar_db():
    """DDL: Crea la estructura de la base de datos si no existe."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Definición de la tabla
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            stock INTEGER NOT NULL CHECK(stock >= 0),
            precio REAL NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def poblar_datos_iniciales():
    """DML: Inserta datos de prueba usando consultas parametrizadas."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Verificar si la tabla ya tiene datos para evitar duplicados
    cursor.execute("SELECT COUNT(*) FROM productos")
    total_registros = cursor.fetchone()[0]

    if total_registros == 0:
        productos = [
            ("Laptop Pro", "Electronica", 15, 1200.00),
            ("Mouse Inalambrico", "Electronica", 50, 25.50),
            ("Teclado Mecanico", "Electronica", 30, 80.00),
            ("Silla Ergonomica", "Muebles", 10, 250.00),
            ("Escritorio Ajustable", "Muebles", 5, 450.00),
            ("Monitor 4K", "Electronica", 8, 350.00)
        ]

        # Uso de executemany con tuplas (Seguridad contra Inyección SQL)
        cursor.executemany("""
            INSERT INTO productos (nombre, categoria, stock, precio)
            VALUES (?, ?, ?, ?)
        """, productos)

        conn.commit()
        print("-> Datos iniciales insertados con exito.")
    else:
        print("-> La base de datos ya contiene registros registrados.")

    conn.close()


def ejecutar_consultas_analiticas():
    """Ejecuta consultas de agregación y filtrado con SQL."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    print("\n" + "="*45)
    print("--- REPORTE ANALITICO DE INVENTARIO (SQL) ---")
    print("="*45)

    # 1. Valor total del inventario (Stock * Precio)
    cursor.execute("SELECT SUM(stock * precio) FROM productos")
    valor_total = cursor.fetchone()[0]
    print(f"Valor Total del Inventario: ${valor_total:,.2f}")

    # 2. Resumen por Categoria (GROUP BY y HAVING)
    print("\nResumen por Categoria:")
    cursor.execute("""
        SELECT 
            categoria,
            COUNT(*) AS total_productos,
            SUM(stock) AS stock_total,
            ROUND(AVG(precio), 2) AS precio_promedio
        FROM productos
        GROUP BY categoria
    """)
    categorias = cursor.fetchall()
    for cat, total_p, stock_t, precio_prom in categorias:
        print(f"  - [{cat}] Productos: {total_p} | Stock Total: {stock_t} | Precio Promedio: ${precio_prom:,.2f}")

    # 3. Productos con bajo stock (Filtrado WHERE)
    print("\nAlertas de Stock Bajo (Menos de 10 unidades):")
    cursor.execute("""
        SELECT nombre, stock, precio 
        FROM productos 
        WHERE stock < 10 
        ORDER BY stock ASC
    """)
    alertas = cursor.fetchall()
    for nombre, stock, precio in alertas:
        print(f"  - ALERTA: {nombre} | Quedan {stock} unidades | ${precio:,.2f} c/u")

    conn.close()


def main():
    inicializar_db()
    poblar_datos_iniciales()
    ejecutar_consultas_analiticas()


if __name__ == "__main__":
    main()