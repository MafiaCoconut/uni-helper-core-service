from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class SideDish:

    side_dish_id: int = field(default=None)
    canteen_id: int = field(default=None)
    name: str = field(default=None)
    type: str | None = field(default=None)
    price: str | None = field(default=None)
    properties: str | None= field(default=None)
    created_at: datetime = field(default=None)
    updated_at: datetime = field(default=None)
