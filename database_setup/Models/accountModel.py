from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://user:pwd@localhost/account")
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    pid = Column(BigInteger, primary_key=True)
    username = Column(String(200))
    role = Column(String(200))
    credit = Column(Float)


class Contracts(Base):
    __tablename__ = 'contracts'

    pid = Column(BigInteger, primary_key=True)
    status = Column(String(200))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    cost = Column(Float)


class UCRelation(Base):
    __tablename__ = 'uc_relation'

    user_pid = Column(BigInteger, primary_key=True)
    contract_pid = Column(BigInteger)


def init():
    Base.metadata.create_all(engine)
