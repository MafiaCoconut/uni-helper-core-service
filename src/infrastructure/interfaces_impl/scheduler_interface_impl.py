from typing import List

from icecream import ic

from application.interfaces.scheduler_interface import SchedulerInterface
from domain.entities.job import Job

from infrastructure.config.scheduler_config import scheduler


class SchedulerInterfaceImpl(SchedulerInterface):
    async def start(self) -> None:
        scheduler.start()

    async def add_job(self, job: Job) -> None:
        scheduler.add_job(
            id=job.id,
            func=job.func,
            trigger=job.trigger,
            hour=job.hour,
            minute=job.minute,
            args=job.args,
            day_of_week=job.day_of_week,
        )

    async def remove(self, job_id: str) -> None:
        scheduler.remove_job(job_id=job_id)

    async def get_all(self) -> list:
        jobs = scheduler.get_jobs()
        return [f"{job.id} - {job.next_run_time}" for job in jobs]

