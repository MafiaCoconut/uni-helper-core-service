from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Canteen:
    canteen_id: int = field(default=None)
    name: str = field(default=None)
    description: str = field(default=None)
    opened_time: int = field(default=None)
    closed_time: int = field(default=None)
    created_at: Optional[datetime] = field(default=None)
