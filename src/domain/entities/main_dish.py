from datetime import datetime
from pydantic import BaseModel, Field


class MainDish(BaseModel):
    main_dish_id: int = Field(default=None)
    canteen_id: int = Field(default=None)
    name: str = Field(default=None)
    type: str = Field(default=None)
    price: str = Field(default=None)
    properties: str | None = Field(default=None)
    created_at: datetime | None = Field(default=None)
    updated_at: datetime | None = Field(default=None)


