from datetime import datetime
from pydantic import BaseModel, Field


class SideDish(BaseModel):
    side_dish_id: int = Field(default=None)
    canteen_id: int = Field(default=None)
    name: str = Field(default=None)
    type: str | None = Field(default=None)
    price: str | None = Field(default=None)
    properties: str | None = Field(default=None)
    created_at: datetime | None = Field(default=None)
    updated_at: datetime | None = Field(default=None)
