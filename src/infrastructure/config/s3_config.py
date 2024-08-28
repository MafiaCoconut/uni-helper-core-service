import asyncio
import os
import shutil
from contextlib import asynccontextmanager

import boto3
from dotenv import load_dotenv
from icecream import ic
load_dotenv()


class S3Client:
    def __init__(self):
        self.bucket_name = os.getenv("AWS_BUCKET_NAME")
        self.client = boto3.client("s3")

    async def upload_file(self, file_path: str, file_name: str):
        with open(file_path) as file:
            self.client.put_object(Body=file.read(), Bucket=self.bucket_name, Key=file_name)


s3client = S3Client()


async def main():
    print("1")
    await s3client.upload_file("../../logs/error_data.log", "error_data.log")
    print("3")
    await s3client.upload_file("../../logs/system_data.log", "system_data.log")
    print(2)


if __name__ == '__main__':
    asyncio.run(main())
