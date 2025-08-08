import boto3
import os
from dotenv import load_dotenv

load_dotenv()

aws_access_key_id = os.environ['ACCESS_KEY']
aws_secret_access_key = os.environ['SECRET_ACCESS_KEY']

print(aws_access_key_id)
print(aws_secret_access_key)
# Cliente S3 con credenciales
s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)
#docker run -e ACCESS_KEY=AKIAXXHL2UEM6HZ4ELBV -e SECRET_ACCESS_KEY=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 henry-2do-pi