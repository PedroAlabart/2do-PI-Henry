from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from datetime import datetime, timedelta
import pandas as pd
import io

BUCKET_NAME = 'modulo-2-pi-bronze'
CSV_KEY = 'products-1000/products-1000.csv'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

def check_file_exists(key, **kwargs):
    hook = S3Hook()
    if hook.check_for_key(key, bucket_name=BUCKET_NAME):
        return True
    else:
        raise ValueError(f"File {key} not found in bucket {BUCKET_NAME}")

def clean_csv(**kwargs):
    hook = S3Hook()
    obj = hook.get_key(CSV_KEY, bucket_name=BUCKET_NAME)
    data = obj.get()['Body'].read()
    
    df = pd.read_csv(io.BytesIO(data))
    
    # Limpieza ejemplo: eliminar filas con NaNs, convertir precio a float
    df = df.dropna()
    df['Price'] = df['Price'].astype(float)
    
    # Guardar resultado limpio local (o subirlo de nuevo a S3 si querés)
    cleaned_path = '/tmp/cleaned_file.csv'
    df.to_csv(cleaned_path, index=False)
    print(f"Cleaned CSV saved to {cleaned_path}")

with DAG(
    's3_file_detection_and_cleaning',
    default_args=default_args,
    description='Detect CSV and JSON in S3, clean CSV data',
    schedule=timedelta(hours=1),
    start_date=datetime(2025, 8, 8),
    catchup=False,
    max_active_runs=1,
    tags=['example'],
) as dag:

    check_csv = PythonOperator(
        task_id='check_csv_exists',
        python_callable=check_file_exists,
        op_kwargs={'key': CSV_KEY},
    )
    
    clean_csv_task = PythonOperator(
        task_id='clean_csv',
        python_callable=clean_csv,
    )

    check_csv >> clean_csv_task
