from .base import Base

from sqlalchemy import (
    Column,
    Table,
    Integer,
    ForeignKey,
)

posts_tags_table = Table(
    "blog_app__posts_tags_association_table",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("blog_app__posts.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("blog_app__tags.id"), primary_key=True),
)