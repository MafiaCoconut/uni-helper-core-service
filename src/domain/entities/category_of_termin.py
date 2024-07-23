from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class CategoryOfTermins:
    category_id: int = field(default=None)
    name: str = field(default=None)
    created_at: datetime = field(default=None)

