from sqlalchemy import (
    create_engine,
    Table,
    MetaData,
    Column,
    String,
    Boolean,
    Integer
)

engine = create_engine("sqlite:///example-01.db")
metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), unique=True),
    Column("is_staff", Boolean, default=False),
)

def main():
    metadata.create_all(engine)


if __name__ == "__main__":
    main()