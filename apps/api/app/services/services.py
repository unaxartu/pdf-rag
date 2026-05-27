import os
import psycopg2
from minio import Minio
from minio.error import S3Error


class MinioClient:
    def __init__(self):
        minio_url = os.getenv("MINIO_URL", "localhost:9000")

        self.minioClient = Minio(
            endpoint=minio_url,
            secure=False
        )

    def create_bucket(self, bucket_name: str):
        try:
            if self.minioClient.bucket_exists(bucket_name):
                print(f"Bucket '{bucket_name}' already exists")
                return

            # Create bucket
            self.minioClient.make_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' created successfully")

        except S3Error as err:
            print(f"Error creating bucket: {err}")


class PostgreClient:
    def __init__(self):
        postgre_url = os.getenv("POSTGRE_URL", "localhost")
        postgre_user = os.getenv("POSTGRE_USER", "postgres")
        postgre_pass = os.getenv("POSTGRE_PASS", "")
        postgre_db = os.getenv("POSTGRE_DB", "postgres")

        self.postgresql_client = psycopg2.connect(ddbname=postgre_db,user=postgre_user,password=postgre_pass,host=postgre_url,port="5432")