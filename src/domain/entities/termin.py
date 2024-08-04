from datetime import datetime
from pydantic import BaseModel, Field


class Termin(BaseModel):
    termin_id: int = Field(default=None)
    category_id: int = Field(default=None)
    time: datetime = Field(default=None)
    created_at: datetime | None = Field(default=None)

