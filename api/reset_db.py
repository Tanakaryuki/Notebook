from sqlalchemy import create_engine
from api.models.book import Base
import os

# HOST=os.environ["HOST"]
# PORT=os.environ["PORT"]
# NAME=os.environ["NAME"]
# USER=os.environ["USER"]
# PASSWORD=os.environ["PASSWORD"]

# URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}?charset=utf8"
URL = "mysql+pymysql://root:root_password@db:3306/demo?charset=utf8"

def reset_database(db_url):
    engine = create_engine(db_url, echo=True)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    reset_database(URL)