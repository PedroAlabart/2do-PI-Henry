Pipeline:

Procesar, limpiar y analizar datos de alojamientos de Airbnb en Nueva York

Fuentes de datos: CSV

Ingesta: Airflow, sensor detecta que se cargo un csv a la carpeta

Transformacion: Airflow para limpiar la base de datos

Load: Cargado a un refined mart en un futuro data warehouse

Almacenamiento:
-bronce se da en S3 de amazon
-silver tambien
-gold tambien


Capas de la data:
Bronze: Se copia y pega la data, se modifica el formato de archivo a parquet y se crean particiones.
Origen : Csv, parquet y json
Destino: parquet
Se comprime los distintos formatos usando Snappy
Particionamiento por fecha. Año > Mes > Dia
Retencion (life cycle) de la data muy alta. Data histórica. 3 años.
Silver:
Se manejan todos archivos ya formateados a parquet
Se sigue comprimiendo con Snappy.
Particionamiento por fecha. Año > Mes > Dia
Retencion (life cycle) de la data alta. Data histórica. 1.5 años.
En esta capa se realizan las transformaciones necesarias. Ver anexo.

Gold:
Se manejan todos archivos ya formateados a parquet
Se sigue comprimiendo con Snappy.
Particionamiento por fecha. Año > Mes > Dia
Retencion (life cycle) de la data baja. 0.5 años.




✅ Pregunta de Negocio 1:
¿Qué barrios de Nueva York ofrecen la mejor rentabilidad promedio para los anfitriones de Airbnb?
🎯 Relación con el pipeline:
Esta pregunta busca identificar oportunidades de inversión o de optimización de precios en función del ingreso potencial por barrio.

🔍 Fuente de datos:
Fuente externa: Dataset público de Airbnb NYC (.csv descargado de Inside Airbnb)

Contiene: price, availability_365, neighbourhood, room_type, reviews_per_month, calculated_host_listings_count, etc.

📊 Relevancia y valor analítico:
Alta relevancia: Los campos price y availability_365 permiten estimar ingresos anuales por propiedad.

neighbourhood permite comparar barrios.

room_type ayuda a segmentar por tipo de alojamiento.

Ejemplo de métrica a calcular:
Ingresos estimados por propiedad = price × availability_365

✅ Confiabilidad:
Fuente confiable y usada por múltiples investigaciones académicas y comerciales.

Los datos son reales y provienen de scrapeos regulares del sitio de Airbnb.

Pueden tener cierto delay temporal, pero son suficientemente representativos.

✅ Pregunta de Negocio 2:
¿Cuáles son las características comunes de los listados con mayor cantidad de reseñas por mes?
🎯 Relación con el pipeline:
Esta pregunta apunta a entender qué factores (zona, tipo de habitación, precio, disponibilidad) hacen que un alojamiento sea más popular o exitoso.

🔍 Fuente de datos:
Fuente externa: Dataset de Airbnb NYC

Variables clave: reviews_per_month, price, room_type, minimum_nights, neighbourhood, availability_365

📊 Relevancia y valor analítico:
Muy alta: permite descubrir patrones que aumentan la visibilidad o rotación de huéspedes.

Contribuye a estrategias de mejora de posicionamiento en la plataforma Airbnb.

Se puede aplicar análisis de correlación o clustering para encontrar grupos de alto rendimiento.

✅ Confiabilidad:
Datos históricos obtenidos de la misma fuente pública.

La métrica reviews_per_month ya viene calculada, lo que simplifica el análisis.

Posible ruido en casos con pocas reviews totales, pero mitigable filtrando.


docker run tiene que ser llamado con

docker run -e ACCESS_KEY=ACCES_KEY -e SECRET_ACCESS_KEY=SECRET_ACCESS_KEY henry-2do-pi