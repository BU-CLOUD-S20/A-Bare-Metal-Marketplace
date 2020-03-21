from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://user:pwd@localhost/market")
Base = declarative_base()


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


class Contracts(Base):
    __tablename__ = 'contracts'

    pid = Column(BigInteger, primary_key=True)
    status = Column(String(200))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    cost = Column(Float)


class CBORelation(Base):
    __tablename__ = 'cbo_relation'

    contract_pid = Column(BigInteger, primary_key=True)
    offer_pid = Column(BigInteger)
    bid_pid = Column(BigInteger)


def init():
    Base.metadata.create_all(engine)

