from datetime import datetime
from pydantic import BaseModel, Field


class User(BaseModel):
    user_id: int
    username: str = Field(default="-")
    name: str = Field(default="-")
    mailing_time: str = Field(default="00:00")
    locale: str = Field(default="-")
    canteen_id: int = Field(default=0)
    status: str = Field(default="active")
    created_at: datetime | None = Field(default=None)
    updated_at: datetime | None = Field(default=None)

    # username: str = Field(default="-")
    # mailing_time: str = Field(default="-")
    # language: str = Field(default="-")
    # canteen_id: int = Field(default=0)
    # created_at: datetime = Field(default_factory=datetime.now())
    # updated_at: datetime = Field(default_factory=datetime.utcnow)
    # status: str = Field(default="active")