from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://user:pwd@localhost/provider")
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    pid = Column(BigInteger, primary_key=True)
    username = Column(String(200))
    role = Column(String(200))
    credit = Column(Float)


class Bids(Base):
    __tablename__ = 'bids'

    pid = Column(BigInteger, primary_key=True)
    quantity = Column(Integer)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    duration = Column(BigInteger)
    status = Column(String(200))
    config_query = Column(String(200))
    cost = Column(Float)


class Offers(Base):
    __tablename__ = 'offers'

    pid = Column(BigInteger, primary_key=True)
    status = Column(String(200))
    resource_id = Column(String(200))
    resource_type = Column(String(200))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    config = Column(String(200))
    cost = Column(Float)


class UBRelation(Base):
    __tablename__ = 'ub_relation'

    user_pid = Column(BigInteger, primary_key=True)
    bid_pid = Column(BigInteger)


class UORelation(Base):
    __tablename__ = 'uo_relation'

    user_pid = Column(BigInteger, primary_key=True)
    offer_pid = Column(BigInteger)


Base.metadata.create_all(engine)

