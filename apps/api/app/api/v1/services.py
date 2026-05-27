import os

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
        self.postgre_url = os.getenv("POSTGRE_URL", "localhost")
        self.postgre_user = os.getenv("POSTGRE_USER", "postgres")
        self.postgre_pass = os.getenv("POSTGRE_PASS", "")
        self.postgre_db = os.getenv("POSTGRE_DB", "postgres")