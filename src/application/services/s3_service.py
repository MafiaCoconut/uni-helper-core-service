from application.use_cases.s3_use_case import S3UseCase


class S3Service:
    def __init__(self, s3client):
        self.s3_use_case = S3UseCase(s3client)

    async def upload_logs(self):
        await self.s3_use_case.upload_logs()

    async def upload_file(self, file_path: str, file_name: str):
        await self.s3_use_case.upload_file(file_path=file_path, file_name=file_name)