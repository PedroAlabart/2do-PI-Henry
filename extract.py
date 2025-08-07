import s3_conn
import pandas as pd

def main():
    # cargo csv de precios de propiedades
    precios = pd.read_csv('data/organizations-1000.csv')
    # Parámetros de configuración
    bucket_name = "modulo-2-pi-bronze"
    file_name = "data/organizations-1000"
    s3_key = "AB_NYC/AB_NYC.csv"  # ruta destino en el bucket


    
    s3_conn.s3.upload_file(file_name, bucket_name, s3_key)

    print(f"✅ Archivo subido a s3://{bucket_name}/{s3_key}")

if __name__ == "__main__":
    main()