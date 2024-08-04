from datetime import datetime
from pydantic import BaseModel, Field


class CategoryOfTermins(BaseModel):
    category_id: int = Field(default=None)
    name: str = Field(default=None)
    created_at: datetime | None = Field(default=None)

