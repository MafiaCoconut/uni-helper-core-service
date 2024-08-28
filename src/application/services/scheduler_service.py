# src/application/services/scheduler_service.py
from datetime import datetime

from application.interfaces.scheduler_interface import SchedulerInterface
from application.services.s3_service import S3Service
from application.use_cases.set_all_scheduler_use_case import SetAllSchedulersJobsUseCase
from application.use_cases.set_s3_scheduler_job import SetS3JobUseCase
from domain.entities.job import Job


class SchedulerService:
    def __init__(self,
                 scheduler_interface: SchedulerInterface,
                 s3_service: S3Service,
                 ):
        self.scheduler_interface = scheduler_interface
        self.set_s3_jobs_use_case = SetS3JobUseCase(
            scheduler_interface=scheduler_interface,
            s3_service=s3_service,
        )
        self.set_all_schedulers_jobs = SetAllSchedulersJobsUseCase(
            scheduler_interface=scheduler_interface,
            set_s3_jobs_use_case=self.set_s3_jobs_use_case,
        )

    async def add_job(self, job: Job) -> None:
        await self.scheduler_interface.add_job(job)

    async def add_all_jobs(self, jobs: list) -> None:
        for job in jobs:
            await self.scheduler_interface.add_job(job)

    async def delete_job(self, job_id: str) -> None:
        await self.scheduler_interface.remove(job_id)

    async def set_start_jobs(self) -> None:
        await self.set_all_schedulers_jobs.execute()

    async def get_all_jobs(self) -> list:
        return await self.scheduler_interface.get_all()

