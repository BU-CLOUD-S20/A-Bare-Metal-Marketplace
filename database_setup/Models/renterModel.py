import sqlalchemy_jsonfield
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import statuses

engine = create_engine("mysql+pymysql://user:pwd@localhost/renter")
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(String(64), primary_key=True, autoincrement=False)
    username = Column(String(256), nullable=False)
    role = Column(String(16), nullable=False)
    credit = Column(Float, nullable=False)


class Bids(Base):
    __tablename__ = 'bids'

    bid_id = Column(String(64), primary_key=True, autoincrement=False)
    project_id = Column(String(64), nullable=False)
    quantity = Column(Integer, nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)
    duration = Column(Integer, nullable=False)
    status = Column(String(16), nullable=False, default=statuses.AVAILABLE)
    # config_query = Column(String(200))
    config_query = Column(sqlalchemy_jsonfield.JSONField(
            enforce_string=True,
            enforce_unicode=False), nullable=False)
    cost = Column(Float, nullable=False)


class UBRelation(Base):
    __tablename__ = 'ub_relation'

    pid = Column(BigInteger, primary_key=True)
    user_id = Column(String(64), ForeignKey("users.user_id"))
    bid_id = Column(String(64), ForeignKey("bids.bid_id"))


class Contracts(Base):
    __tablename__ = 'contracts'

    contract_id = Column(String(64), primary_key=True, autoincrement=False)
    status = Column(String(16), nullable=False, default=statuses.AVAILABLE)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)
    cost = Column(Float, nullable=False)
    project_id = Column(String(64), nullable=False)


class UCRelation(Base):
    __tablename__ = 'uc_relation'

    pid = Column(BigInteger, primary_key=True)
    user_id = Column(String(64), ForeignKey("users.user_id"))
    contract_id = Column(String(64), ForeignKey("contracts.contract_id"))


def init():
    Base.metadata.create_all(engine)
