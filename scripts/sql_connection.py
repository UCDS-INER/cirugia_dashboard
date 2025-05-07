#!/usr/bin/env python
# coding: utf-8

try:
    import pymysql
    import cirugia_dashboard.scripts.config as config  # Importa el archivo de configuración
    import cirugia_dashboard.scripts.queries as queries  # Importa el archivo de consultas SQL
except ImportError as e:
    raise ImportError(f"Required module is not installed: {e}")

# Conexión a la base de datos MariaDB
conexion = pymysql.connect(
    host=config.DB_HOST,       # Usando las credenciales de config.py
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME
)

# Ejecutar la consulta desde queries.py
query = queries.QUERY_qx

with conexion.cursor() as cursor:
    cursor.execute(query)
    result = cursor.fetchall()

# Mostrar el resultado
for row in result:
    print(row)

try:
    import pandas as pd
except ImportError:
    raise ImportError("The 'pandas' module is not installed. Install it using 'pip install pandas'.")

# Convertir el resultado del query en un DataFrame
columns = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
df_result = pd.DataFrame(result, columns=columns)

# Mostrar el DataFrame
print(df_result)