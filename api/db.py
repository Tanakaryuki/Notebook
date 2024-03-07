from uuid import uuid4
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from api.models.book import Base
import os

HOST=os.environ["HOST"]
PORT=os.environ["PORT"]
NAME=os.environ["NAME"]
USER=os.environ["USER"]
PASSWORD=os.environ["PASSWORD"]

URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}?charset=utf8"

engine = create_engine(URL)
LocalSession = sessionmaker(engine)

Base = declarative_base()


def get_db():
    database = LocalSession()
    try:
        yield database
    finally:
        database.close()


def generate_uuid():
    return str(uuid4())


# def reset_database(db_url):
#     engine = create_engine(db_url, echo=True)
#     Base.metadata.drop_all(bind=engine)
#     Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database(URL)