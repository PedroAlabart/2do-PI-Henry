import requests
from datetime import date
import json
import os 
import util.s3_conn as s3_conn


def main():
    # obtengo fecha actual
    hoy = date.today()
    fecha_formateada = hoy.strftime("%Y-%m-%d")
    # Tipo de Cambio Minorista ($ por USD) Comunicación B 9791 - Promedio vendedor'
    # defino fechas de inicio y fin
    fecha_inicio = fecha_formateada
    fecha_fin = fecha_formateada
    # id del dolar
    IdVariable  = 4

    # hago el request
    url = f"https://dolarapi.com/v1/dolares/blue"
    response = requests.get(url, verify=False)

    # si devuelve bien se procede
    if response.status_code == 200:
        data = response.json()
        # Parámetros
        bucket_name = "modulo-2-pi-bronze"
        s3_key = f"valor_dolar/{date.today()}.json"  # ruta dentro del bucket

        # Subir el JSON crudo como string
        s3_conn.s3.put_object(
            Bucket=bucket_name,
            Key=s3_key,
            Body=json.dumps(data),
            ContentType="application/json"
        )

        print(f"✅ Archivo subido a s3://{bucket_name}/{s3_key}")
    else: 
        print('Llamada a la API de BCRA fallida')

if __name__ == "__main__":
    main()
