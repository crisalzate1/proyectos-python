import sqlite3
import pandas as pd

# 1. Conexión a la base de datos y activación de claves foráneas
conexion = sqlite3.connect("tienda.db")
cursor = conexion.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

# 2. Insertamos un cliente nuevo que TODAVÍA NO tiene compras (para probar LEFT JOIN)
cursor.execute("INSERT OR IGNORE INTO clientes (id_cliente, nombre, email) VALUES (3, 'Carlos', 'carlos@email.com');")
conexion.commit()

# 3. Consulta SQL con LEFT JOIN (Trae a TODOS los clientes, tengan o no ventas)
query_left = """
SELECT 
    c.id_cliente,
    c.nombre,
    c.email,
    v.id_venta,
    v.monto,
    v.fecha
FROM clientes c
LEFT JOIN ventas v ON c.id_cliente = v.id_cliente;
"""

# 4. Pandas lee la consulta SQL directamente y la convierte en un DataFrame
df_reporte = pd.read_sql_query(query_left, conexion)

print("--- REPORTE GENERAL DE CLIENTES (SQL + PANDAS) ---")
print(df_reporte)

# 5. Uso de Pandas para detectar clientes sin compras (valores NaN / Nulos)
clientes_sin_compras = df_reporte[df_reporte['monto'].isna()]

print("\n--- CLIENTES QUE NO HAN COMPRADO (OPORTUNIDAD DE MARKETING) ---")
print(clientes_sin_compras[['id_cliente', 'nombre', 'email']])

conexion.close()