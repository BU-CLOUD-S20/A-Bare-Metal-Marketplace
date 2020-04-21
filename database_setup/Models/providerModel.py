import sys
import sqlalchemy_jsonfield
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
sys.path.append("/home/stardust/A-Bare-Metal-Marketplace/database_setup")
import statuses


engine = create_engine("mysql+pymysql://marketplace:123456@localhost/provider")
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(String(64), primary_key=True, autoincrement=False)
    username = Column(String(256), nullable=False)
    role = Column(String(16), nullable=False)
    credit = Column(Float, nullable=False)


class Offers(Base):
    __tablename__ = 'offers'

    offer_id = Column(String(64), primary_key=True, autoincrement=False)
    project_id = Column(String(64), nullable=False)
    status = Column(String(16), nullable=False, default=statuses.AVAILABLE)
    resource_id = Column(String(64), nullable=False)
    # resource_type = Column(String(100), nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)
    config = Column(sqlalchemy_jsonfield.JSONField(
        enforce_string=True,
        enforce_unicode=False), nullable=False)
    cost = Column(Float, nullable=False)


class UORelation(Base):
    __tablename__ = 'uo_relation'

    pid = Column(BigInteger, primary_key=True)
    user_id = Column(String(64), ForeignKey("users.user_id"))
    offer_id = Column(String(64), ForeignKey("offers.offer_id"))


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


if __name__ == "__main__":
    init()
