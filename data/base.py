from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase , sessionmaker
#engine = create_engine("sqlite:///tours.db")
engine = create_engine("postgresql+psycopg2://postgres:220511wwptqq@localhost:5432/project_tour")
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def create_db():
    Base.metadata.create_all(bind=engine)
