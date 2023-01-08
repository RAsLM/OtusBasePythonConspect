from .base import Base
from .posts_tags import posts_tags_table

from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import relationship
class Tag(Base):
    name = Column(String(32), unique=True, nullable=True)

    posts = relationship(
        "Post",
        secondary=posts_tags_table,
        back_populates = "tags",
    )

    def __str__(self):
        return self.name