from .base import Base
from .mixins import TimestampMixin

from sqlalchemy import (
    Column,
    String,
    Boolean,
)
from sqlalchemy.orm import relationship
class User(TimestampMixin, Base):

    def __init__(self, username: str, is_staff: bool = False):
        self.username = username
        self.is_staff = is_staff

    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, default=False)

    posts = relationship("Post", back_populates="author")

print("User class created")