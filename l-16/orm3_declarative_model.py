from datetime import datetime

from sqlalchemy import (
    create_engine,
    Column,
    String,
    Boolean,
    Integer,
    DateTime,
)

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///example-03.db")
Base = declarative_base(bind=engine)

class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True)
    username = Column("username", String(32), unique=True)
    is_staff = Column("is_staff", Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)


def main():
    Base.metadata.create_all()


if __name__ == "__main__":
    main()
