import util.s3_conn as s3_conn
import pandas as pd

def main():
    # Parámetros de configuración
    bucket_name = "modulo-2-pi-bronze"
    file_name = "data/products-1000.csv"
    s3_key = "products-1000/products-1000.csv"  # ruta destino en el bucket


    
    s3_conn.s3.upload_file(file_name, bucket_name, s3_key)

    print(f"✅ Archivo subido a s3://{bucket_name}/{s3_key}")

if __name__ == "__main__":
    main()