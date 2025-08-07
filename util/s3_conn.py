import boto3 #Libreria oficial de amazon para Python
import os
from dotenv import load_dotenv
load_dotenv()

ACCES_KEY = os.getenv("ACCES_KEY")
SECRET_ACCES_KEY = os.getenv("SECRET_ACCES_KEY")


# Cliente S3
s3 = boto3.client("s3")