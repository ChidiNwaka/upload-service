# Placeholder for your metadata model shape.
# Later, you can replace this with SQLAlchemy or keep raw SQL + dicts.

from dataclasses import dataclass
from datetime import datetime

@dataclass
class UploadMetadata:
    id: str
    filename: str
    content_type: str
    size_bytes: int
    s3_key: str
    created_at: datetime
