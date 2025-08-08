FROM apache/airflow:3.0.3

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# El comando por defecto de airflow se mantiene, no necesitás CMD python ...
