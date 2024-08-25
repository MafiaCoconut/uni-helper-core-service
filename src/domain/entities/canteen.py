from datetime import datetime
from pydantic import BaseModel, Field


class Canteen(BaseModel):
    canteen_id: int = Field(default=None)
    name: str = Field(default=None)
    description: str = Field(default=None)
    status: str = Field(default=None)
    times: dict = Field(default=None)
    opened_time: int = Field(default=None)
    closed_time: int = Field(default=None)
    created_at: datetime | None = Field(default=None)
