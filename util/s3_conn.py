import boto3
import os
from dotenv import load_dotenv

load_dotenv()

aws_access_key_id = os.environ['ACCESS_KEY']
aws_secret_access_key = os.environ['SECRET_ACCESS_KEY']


# Cliente S3 con credenciales
s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)



