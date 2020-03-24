from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy_jsonfield


engine = create_engine("mysql+pymysql://user:pwd@localhost/market")
Base = declarative_base()


class Bids(Base):
    __tablename__ = 'bids'

    pid = Column(BigInteger, primary_key=True)
    project_id = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)
    duration = Column(Integer, nullable=False)
    status = Column(String(100), nullable=False)
    # config_query = Column(String(200))
    config_query = Column(sqlalchemy_jsonfield.JSONField(
            enforce_string=True,
            enforce_unicode=False), nullable=False)
    cost = Column(Float, nullable=False)


class Offers(Base):
    __tablename__ = 'offers'

    pid = Column(BigInteger, primary_key=True)
    project_id = Column(String(100), nullable=False)
    status = Column(String(100), nullable=False)
    resource_id = Column(String(100), nullable=False)
    resource_type = Column(String(100), nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)
    # config = Column(String(200))
    config = Column(sqlalchemy_jsonfield.JSONField(
        enforce_string=True,
        enforce_unicode=False), nullable=False)
    cost = Column(Float, nullable=False)


class Contracts(Base):
    __tablename__ = 'contracts'

    pid = Column(BigInteger, primary_key=True)
    status = Column(String(100), nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)
    cost = Column(Float, nullable=False)
    project_id = Column(String(100), nullable=False)


class CBORelation(Base):
    __tablename__ = 'cbo_relation'

    pid = Column(BigInteger, primary_key=True)
    contract_pid = Column(BigInteger, ForeignKey("contracts.pid"))
    offer_pid = Column(BigInteger, ForeignKey("offers.pid"))
    bid_pid = Column(BigInteger, ForeignKey("bids.pid"))


def init():
    Base.metadata.create_all(engine)
