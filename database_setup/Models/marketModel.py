import sys
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy_jsonfield
sys.path.append("/home/stardust/A-Bare-Metal-Marketplace/database_setup")
import database_setup.statuses as statuses


engine = create_engine("mysql+pymysql://marketplace:123456@localhost/market")
Base = declarative_base()


class Bids(Base):
    __tablename__ = 'bids'

    bid_id = Column(String(64), primary_key=True, autoincrement=False)
    project_id = Column(String(64), nullable=False)
    quantity = Column(Integer, nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)
    expire_time = Column(DateTime(timezone=True), nullable=False)
    duration = Column(Integer, nullable=False)
    status = Column(String(16), nullable=False, default=statuses.AVAILABLE)
    # config_query = Column(String(200))
    config_query = Column(sqlalchemy_jsonfield.JSONField(
            enforce_string=True,
            enforce_unicode=False), nullable=False)
    cost = Column(Float, nullable=False)


class Offers(Base):
    __tablename__ = 'offers'

    offer_id = Column(String(64), primary_key=True, autoincrement=False)
    project_id = Column(String(64), nullable=False)
    status = Column(String(16), nullable=False, default=statuses.AVAILABLE)
    resource_id = Column(String(64), nullable=False)
    # resource_type = Column(String(100), nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)
    expire_time = Column(DateTime(timezone=True), nullable=False)
    config = Column(sqlalchemy_jsonfield.JSONField(
        enforce_string=True,
        enforce_unicode=False), nullable=False)
    cost = Column(Float, nullable=False)


class Contracts(Base):
    __tablename__ = 'contracts'

    contract_id = Column(String(64), primary_key=True, autoincrement=False)
    status = Column(String(16), nullable=False, default=statuses.AVAILABLE)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)
    cost = Column(Float, nullable=False)
    project_id = Column(String(64), nullable=False)


class CBORelation(Base):
    __tablename__ = 'cbo_relation'

    pid = Column(BigInteger, primary_key=True)
    contract_id = Column(String(64), ForeignKey("contracts.contract_id"))
    offer_id = Column(String(64), ForeignKey("offers.offer_id"))
    bid_id = Column(String(64), ForeignKey("bids.bid_id"))


def init():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    init()
