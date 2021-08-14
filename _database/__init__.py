from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///_database/db/appData.db", convert_unicode=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    """initializes the database and models"""

    import _database.models

    Base.metadata.create_all(bind=engine)
