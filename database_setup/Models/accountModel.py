import sys
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
sys.path.append("/home/stardust/A-Bare-Metal-Marketplace/database_setup")
import statuses


engine = create_engine("mysql+pymysql://marketplace:123456@localhost/account")
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(String(64), primary_key=True, autoincrement=False)
    username = Column(String(256), nullable=False)
    role = Column(String(16), nullable=False)
    credit = Column(Float, nullable=False)


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
    contract_id = Column(String(64), ForeignKey("contracts.contract_id"))
    provider_id = Column(String(64), ForeignKey("users.user_id"))
    renter_id = Column(String(64), ForeignKey("users.user_id"))


def init():
    Base.metadata.create_all(engine)


if  __name__ == "__main__":
    init()
