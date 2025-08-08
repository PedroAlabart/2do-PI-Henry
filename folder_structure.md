
# 🛠️ Estructura del Proyecto - 2DO-PI

Este proyecto implementa un pipeline de procesamiento de datos utilizando Airflow, contenedores Docker y almacenamiento en la nube (AWS S3). A continuación se detalla la estructura del proyecto y la función de cada carpeta y archivo.

## 📁 Estructura del Proyecto

```
2DO-PI/
│
├── config/                  # Configuraciones generales del pipeline (ej: conexiones, variables, rutas)
│
├── dags/                    # Definición de DAGs de Airflow (tareas y flujos de trabajo)
│
├── data/                    # Directorio para almacenar datos locales en diferentes capas (bronze, silver, etc.)
│
├── images/                  # Diagramas explicativos del flujo y arquitectura del pipeline
│   ├── architecture.png
│   └── bronze_lifecycle.png
│
├── logs/                    # Logs generados por la ejecución de Airflow o scripts
│
├── plugins/                 # Plugins personalizados de Airflow (operadores, sensores, etc.)
│
├── util/                    # Funciones utilitarias y conexiones externas
│   ├── s3_conn.py           # Conexión a S3 mediante `boto3` o hooks de Airflow
│
├── venv/                    # Entorno virtual de Python (no subir al repositorio)
│
├── .dockerignore            # Archivos y carpetas ignoradas al construir la imagen Docker
├── .env                     # Variables de entorno sensibles (no debe subirse a git)
├── .gitattributes           # Configuración adicional para git
├── .gitignore               # Archivos/carpetas ignoradas por git
│
├── 1er Avance.md            # Documento de avance del proyecto
│
├── docker-compose.yaml      # Orquestación de servicios con Docker (ej: Airflow, PostgreSQL, etc.)
├── Dockerfile               # Imagen base para ejecutar los scripts del pipeline
│
├── extract_api.py           # Script de extracción de datos desde APIs externas
├── extract_csv.py           # Script para leer archivos CSV y cargarlos en capas iniciales
├── extract_facade.py        # Patrón Facade que abstrae la lógica de extracción de datos
│
└── requirements.txt         # Dependencias del proyecto
```


