# Proyectos en Python

Repositorio personal para almacenar avances, proyectos e hitos de aprendizaje en Python y Análisis de Datos.

## Contenido

- **mision1.py**: Script interactivo con procesamiento de datos del usuario, validación de edad y manejo de excepciones (`try-except`).
- **mision2.py**: Gestor de usuarios interactivo con almacenamiento persistente en formato JSON (`usuarios.json`), cálculo de promedios de edad y filtrado de registros.
- **mision3.py**: Análisis de ventas procesando archivos CSV (`ventas.csv`), agregación de ingresos por categoría y exportación filtrada a `ventas_altas.csv`.
- **mision4.py**: Análisis exploratorio de datos de ventas usando **Pandas**, creación de columnas calculadas, agregaciones (`groupby`) y exportación optimizada.
- **mision5.py**: Modelado de base de datos relacional con **SQLite** (`sqlite3`), definición de esquemas (DDL), manipulación de datos (DML) y consultas analíticas agregadas (`GROUP BY`, `SUM`, `AVG`).

### 🔹 Misión 6: SQL Avanzado y Modelado Relacional multitabla (`mision6.py`)

- **Objetivo:** Diseñar y estructurar bases de datos relacionales garantizando la integridad de los datos entre tablas relacionadas.
- **Conceptos clave aplicados:**
  - **Claves Primarias (`PRIMARY KEY`):** Identificadores únicos para cada registro en las tablas base.
  - **Claves Foráneas (`FOREIGN KEY`):** Establecimiento de relaciones entre la tabla `clientes` (padre) y `ventas` (hija) con restricción estricta de integridad referencial (`PRAGMA foreign_keys = ON;`).
  - **Consultas Multitabla (`INNER JOIN`):** Cruce horizontal de información para generar reportes analíticos con nombres de clientes y detalles de transacciones.
  - **Manejo de Errores de Integridad:** Captura de excepciones con `sqlite3.IntegrityError` al intentar registrar compras para clientes inexistentes.
