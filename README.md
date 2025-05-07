# Cirugía Dashboard

Este proyecto está diseñado para interactuar con una base de datos MariaDB, ejecutar consultas SQL y procesar los resultados en un DataFrame utilizando Python.

## Estructura del Proyecto

```
cirugia_dashboard/
├── notebooks/
│   └── sql_connection.ipynb  # Notebook para pruebas y desarrollo
├── scripts/
│   ├── config.py             # Archivo de configuración con credenciales de la base de datos
│   ├── queries.py            # Archivo con las consultas SQL (no se sube al repositorio)
│   └── sql_connection.py      # Archivo para la conexión a la base de datos
├── .env                      # Archivo con variables de entorno (no se sube al repositorio)
├── requirements.yml          # Dependencias del proyecto
└── README.md                 # Documentación del proyecto
```

## Configuración

1. **Archivo `.env`**  
   Crea un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:

   ```
   SCRIPTS_PATH=cirugia_dashboard/scripts
   ```

2. **Archivo `config.py`**  
   Este archivo debe contener las credenciales de la base de datos. Ejemplo:

   ```
python   DB_HOST = "localhost"
   DB_USER = "usuario"
   DB_PASSWORD = "contraseña"
   DB_NAME = "nombre_base_datos"
   ```

3. **Archivo `queries.py`**  
   Define las consultas SQL que se ejecutarán. Ejemplo:

   ```python
   QUERY_qx = "SELECT * FROM tabla_ejemplo;"
   ```

## Instalación

1. Instala [conda](https://docs.conda.io/en/latest/).
2. Crea un entorno con las dependencias del proyecto:

   ```bash
   conda env create -f requirements.yml
   ```

3. Activa el entorno:

   ```bash
   conda activate cirugia_dashboard
   ```

## Notas

- **Archivos no incluidos en el repositorio:**  

Por razones de seguridad, los siguientes archivos no se incluyen en el repositorio y deben ser creados manualmente:

  - `.env`: Contiene variables de entorno sensibles.
  - `config.py`: Contiene credenciales de la base de datos.
  - `queries.py`: Contiene las consultas SQL. (si las necesitas puedes contactarme para que te las pase)

  Asegúrate de crear estos archivos manualmente antes de ejecutar el proyecto.

## Uso

1. Ejecuta el notebook `sql_connection.ipynb` para probar la conexión y procesar los datos.
2. Modifica las consultas en `queries.py` según sea necesario.

## Contribuciones

Si deseas contribuir a este proyecto, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.