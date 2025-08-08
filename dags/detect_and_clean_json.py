import json

JSON_KEY = 'path/to/your/file.json'

def clean_json(**kwargs):
    hook = S3Hook()
    obj = hook.get_key(JSON_KEY, bucket_name=BUCKET_NAME)
    data = obj.get()['Body'].read()
    
    # Parseamos JSON
    json_data = json.loads(data)
    
    # Limpieza / validaciones básicas
    required_fields = ["moneda", "casa", "nombre", "compra", "venta", "fechaActualizacion"]
    for field in required_fields:
        if field not in json_data:
            raise ValueError(f"Field {field} missing in JSON data")
    
    # Ejemplo: convertir compra y venta a float
    json_data["compra"] = float(json_data["compra"])
    json_data["venta"] = float(json_data["venta"])
    
    # Guardar JSON limpio local
    cleaned_json_path = '/tmp/cleaned_data.json'
    with open(cleaned_json_path, 'w') as f:
        json.dump(json_data, f, indent=2)
    
    print(f"Cleaned JSON saved to {cleaned_json_path}")

# Dentro del DAG:
check_json = PythonOperator(
    task_id='check_json_exists',
    python_callable=check_file_exists,
    op_kwargs={'key': JSON_KEY},
)

clean_json_task = PythonOperator(
    task_id='clean_json',
    python_callable=clean_json,
)

# Y la secuencia de tareas
check_csv >> clean_csv_task >> check_json >> clean_json_task
