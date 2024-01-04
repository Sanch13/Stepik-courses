from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Integer, Float, Column, ForeignKey, Text

Base = declarative_base()
# Base - это объект, который обычно является экземпляром класса declarative_base из SQLAlchemy.
# Он служит базовым классом для всех классов, представляющих таблицы в базе данных.

class MyGoods(Base):
    __tablename__ = "my_goods"
    id = Column(Integer, primary_key=True)
    Good_name = Column(String(50))
    Price = Column(Float)
    Amount = Column(Integer)

    def __init__(self, Good_name, Price, Amount):
        self.Good_name = Good_name
        self.Price = Price
        self.Amount = Amount

    def __str__(self):
        return f'{self.id} {self.Good_name}'


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(100))
    Age = Column(Integer)


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, nullable=False, primary_key=True)
    Description = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
