from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from datetime import datetime, timedelta
import pandas as pd
import io
from dags_util import check_file_exists

BUCKET_NAME = 'modulo-2-pi-bronze'
CSV_KEY = 'products-1000/products-1000.csv'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# def check_file_exists(key, **kwargs):
#     hook = S3Hook()
#     if hook.check_for_key(key, bucket_name=BUCKET_NAME):
#         return True
#     else:
#         raise ValueError(f"File {key} not found in bucket {BUCKET_NAME}")

def clean_csv(**kwargs):
    hook = S3Hook()
    obj = hook.get_key(CSV_KEY, bucket_name=BUCKET_NAME)
    data = obj.get()['Body'].read()
    
    df = pd.read_csv(io.BytesIO(data))
    
    # Limpieza ejemplo: eliminar filas con NaNs, convertir precio a float
    df = df.dropna()
    df['Price'] = df['Price'].astype(float)
    
    # Guardar local temporalmente
    cleaned_path = '/tmp/cleaned_file.csv'
    df.to_parquet(cleaned_path, index=False)
    
    # Subir CSV limpio a bucket modulo-2-pi-silver, carpeta cleaned/
    target_bucket = 'modulo-2-pi-silver'
    target_key = 'cleaned/products-1000-cleaned.parquet'
    hook.load_file(
        filename=cleaned_path,
        key=target_key,
        bucket_name=target_bucket,
        replace=True
    )
    
    print(f"Cleaned CSV uploaded to s3://{target_bucket}/{target_key}")

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
        op_kwargs={'key': CSV_KEY, 'bucket_name': BUCKET_NAME},

    )
    
    clean_csv_task = PythonOperator(
        task_id='clean_csv',
        python_callable=clean_csv,
    )

    check_csv >> clean_csv_task
