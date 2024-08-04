from datetime import datetime
from typing import Callable

from pydantic import BaseModel, Field


class Job(BaseModel):
    func: Callable = Field(default=None)
    trigger: str = Field(default=None)
    run_date: datetime = Field(default=None)
    args: list = Field(default=None)
    job_id: str | None = Field(default=None)
    job_type: str | None = Field(default=None)

