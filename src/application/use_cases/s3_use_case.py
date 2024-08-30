import time
from contextlib import asynccontextmanager
import shutil

from infrastructure.config.logs_config import log_decorator


class S3UseCase:
    def __init__(self, s3_client):
        self.s3_client = s3_client

    @log_decorator(print_args=False, print_kwargs=False)
    async def upload_file(self, file_path: str, file_name: str):
        await self.s3_client.upload_file(file_path=file_path, file_name=file_name)

    @log_decorator(print_args=False, print_kwargs=False)
    async def upload_logs(self):
        logs_files = {
            "core_system_logs.txt": "logs/system_data.log",
            "core_error_logs.txt": "logs/error_data.log",
            "core_user_logs.txt": "logs/user_data.log",
        }
        for file_name, file_path in logs_files.items():
            await self.s3_client.upload_file(file_path=file_path, file_name=file_name)

