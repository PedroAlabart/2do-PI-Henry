from airflow.providers.amazon.aws.hooks.s3 import S3Hook

def check_file_exists(key, bucket_name, **kwargs):
    hook = S3Hook()
    if not hook.check_for_key(key, bucket_name=bucket_name):
        raise FileNotFoundError(f"El archivo {key} no existe en el bucket {bucket_name}")
    print(f"Archivo {key} encontrado correctamente")