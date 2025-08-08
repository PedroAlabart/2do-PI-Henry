import json
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

# CONSTANTES
BUCKET_NAME = 'modulo-2-pi-bronze'
JSON_KEY = 'valor_dolar/2025-08-08.json'

def check_file_exists(key, **kwargs):
    hook = S3Hook()
    if not hook.check_for_key(key, bucket_name=BUCKET_NAME):
        raise FileNotFoundError(f"El archivo {key} no existe en el bucket {BUCKET_NAME}")
    print(f"Archivo {key} encontrado correctamente")

def clean_json(**kwargs):
    hook = S3Hook()
    obj = hook.get_key(JSON_KEY, bucket_name=BUCKET_NAME)
    data = obj.get()['Body'].read()
    
    json_data = json.loads(data)

    required_fields = ["moneda", "casa", "nombre", "compra", "venta", "fechaActualizacion"]
    for field in required_fields:
        if field not in json_data:
            raise ValueError(f"Field {field} missing in JSON data")
    
    json_data["compra"] = float(json_data["compra"])
    json_data["venta"] = float(json_data["venta"])
    
    cleaned_json_path = '/tmp/cleaned_data.json'
    with open(cleaned_json_path, 'w') as f:
        json.dump(json_data, f, indent=2)

    print(f"Cleaned JSON saved to {cleaned_json_path}")

# DEFINICIÓN DEL DAG
with DAG(
    dag_id='clean_json_from_s3',
    start_date=datetime(2025, 8, 1),
    schedule_interval=None,
    catchup=False,
    tags=["s3", "json", "cleaning"]
) as dag:

    check_json = PythonOperator(
        task_id='check_json_exists',
        python_callable=check_file_exists,
        op_kwargs={'key': JSON_KEY},
    )

    clean_json_task = PythonOperator(
        task_id='clean_json',
        python_callable=clean_json,
    )

    check_json >> clean_json_task
