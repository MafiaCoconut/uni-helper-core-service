from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class Termin:
    termin_id: int = field(default=None)
    category_id: int = field(default=None)
    time: datetime = field(default=None)
    created_at: datetime = field(default=None)

