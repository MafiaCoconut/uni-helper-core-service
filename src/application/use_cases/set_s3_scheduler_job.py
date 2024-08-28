from application.interfaces.scheduler_interface import SchedulerInterface
from application.services.s3_service import S3Service
from domain.entities.job import Job


class SetS3JobUseCase:
    def __init__(self,
                 scheduler_interface: SchedulerInterface,
                 s3_service: S3Service
                 ):
        self.scheduler_interface = scheduler_interface
        self.s3_service = s3_service

    async def execute(self):
        await self.scheduler_interface.add_job(
            Job(
                func=self.s3_service.upload_logs,
                trigger='cron',
                hour='0',
                minute='0',
                id='s3_upload_logs',
                day_of_week='mon,fri'
            )
        )