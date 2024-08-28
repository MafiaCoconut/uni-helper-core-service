from datetime import datetime, timedelta

from icecream import ic

from application.interfaces.scheduler_interface import SchedulerInterface
from application.use_cases.set_s3_scheduler_job import SetS3JobUseCase
from domain.entities.job import Job
from infrastructure.config.logs_config import log_decorator


class SetAllSchedulersJobsUseCase:
    def __init__(self,
                 scheduler_interface: SchedulerInterface,
                 set_s3_jobs_use_case: SetS3JobUseCase,
                 ):
        self.scheduler_interface = scheduler_interface
        self.set_s3_jobs_use_case = set_s3_jobs_use_case

    @log_decorator
    async def execute(self):
        await self.set_s3_upload_logs()
        await self.scheduler_interface.start()

    @log_decorator
    async def set_s3_upload_logs(self):
        await self.set_s3_jobs_use_case.execute()
