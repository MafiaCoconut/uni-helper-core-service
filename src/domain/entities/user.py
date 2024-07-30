# from dataclasses import dataclass, field
from datetime import datetime
from pydantic import BaseModel, Field


class User(BaseModel):
    user_id: int
    username: str = Field(default="-")
    mailing_time: str = Field(default="-")
    locale: str = Field(default="-")
    canteen_id: int = Field(default=0)
    created_at: datetime = Field(default=None)
    updated_at: datetime = Field(default=None)
    status: str = Field(default="active")

    # username: str = Field(default="-")
    # mailing_time: str = Field(default="-")
    # language: str = Field(default="-")
    # canteen_id: int = Field(default=0)
    # created_at: datetime = Field(default_factory=datetime.now())
    # updated_at: datetime = Field(default_factory=datetime.utcnow)
    # status: str = Field(default="active")