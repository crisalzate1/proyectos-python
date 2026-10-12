import sqlite3

# 1. Conexión a la base de datos y activación de Claves Foráneas
conexion = sqlite3.connect("tienda.db")
cursor = conexion.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

# 2. CREACIÓN DE TABLAS (Padre e Hija)
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ventas (
    id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    monto REAL NOT NULL,
    fecha TEXT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);
""")

print("✅ Tablas 'clientes' y 'ventas' verificadas/creadas con éxito.")

# 3. INSERCIÓN DE DATOS VÁLIDOS
cursor.execute("INSERT OR IGNORE INTO clientes (id_cliente, nombre, email) VALUES (1, 'Cristian', 'cristian@email.com');")
cursor.execute("INSERT OR IGNORE INTO clientes (id_cliente, nombre, email) VALUES (2, 'Keyla', 'keyla@email.com');")

cursor.execute("INSERT INTO ventas (id_cliente, monto, fecha) VALUES (1, 150.00, '2026-10-12');")
cursor.execute("INSERT INTO ventas (id_cliente, monto, fecha) VALUES (1, 45.00, '2026-10-12');")
cursor.execute("INSERT INTO ventas (id_cliente, monto, fecha) VALUES (2, 80.00, '2026-10-12');")

conexion.commit()
print("✅ Clientes y ventas insertados correctamente.")

# 4. PRUEBA DE BLOQUEO (Clave Foránea)
try:
    print("\nIntentando registrar una venta al cliente 99 (inexistente)...")
    cursor.execute("INSERT INTO ventas (id_cliente, monto, fecha) VALUES (99, 500.00, '2026-10-12');")
    conexion.commit()
except sqlite3.IntegrityError as e:
    print(f"❌ ¡BLOQUEADO POR LA BASE DE DATOS! Error de integridad referencial: {e}")

# 5. CONSULTA ANALÍTICA CON INNER JOIN (Antes de cerrar la conexión)
query_join = """
SELECT 
    clientes.nombre,
    clientes.email,
    ventas.id_venta,
    ventas.monto,
    ventas.fecha
FROM ventas
INNER JOIN clientes ON ventas.id_cliente = clientes.id_cliente;
"""

cursor.execute(query_join)
compras = cursor.fetchall()

print("\n--- REPORTES DE VENTAS CON NOMBRES DE CLIENTES (INNER JOIN) ---")
for fila in compras:
    print(f"Cliente: {fila[0]} ({fila[1]}) | Venta #{fila[2]} | Monto: ${fila[3]} | Fecha: {fila[4]}")

# 6. CIERRE DE CONEXIÓN (SIEMPRE AL FINAL DE TODO EL PROCESO)
conexion.close()