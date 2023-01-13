from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://user:password@localhost/blog_app", echo=True)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)