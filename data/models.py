from typing import List 
from sqlalchemy import String ,ForeignKey ,Table ,Column
from sqlalchemy.orm import Mapped ,mapped_column,relationship
from data.base import Base
from flask_login import UserMixin


class Tour(Base):
    __tablename__ = "tours"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(100))
    departure: Mapped[str] = mapped_column(String(50))
    picture: Mapped[str] = mapped_column(String(1000))
    price: Mapped[int] = mapped_column()
    stars: Mapped[str] = mapped_column(String(10))
    country: Mapped[str] = mapped_column(String(100))
    nights: Mapped[int] = mapped_column()
    date: Mapped[str] = mapped_column(String(100))


tour_user_assoc = Table(
    "tour_user_assoc",
    Base.metadata,
    Column("tour_id",ForeignKey("tours.id"),primary_key=True),
    Column("user_id",ForeignKey("users.id"),primary_key = True)
)


class User(Base,UserMixin):
    __tablename__="users"

    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(String(100),unique = True)
    email:Mapped[str] = mapped_column(String(500),unique= True)
    password:Mapped[str] = mapped_column(String(500))
    tours:Mapped[List[Tour]] = relationship(secondary=tour_user_assoc)