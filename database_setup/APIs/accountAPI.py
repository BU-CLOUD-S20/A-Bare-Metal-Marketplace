from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import Models.accountModel as account

engine = create_engine("mysql+pymysql://root:pwd@localhost/account")


def user_insert(username, role, credit):
    Session = sessionmaker(bind=engine)
    session = Session()
    user = account.Users(username=username, role=role, credit=credit)
    session.add(user)
    session.commit()


def select():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(account.Users).all()
    for row in result:
        print(row.username, row.role, row.credit)


def select_by_pid():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(account.Users).filter(account.Users.pid == 1)
    for row in result:
        print(row.username, row.role, row.credit)


def ucrelation_insert():
    Session = sessionmaker(bind=engine)
    session = Session()
    relation = account.UCRelation(user_pid=1, contract_pid=3)
    session.add(relation)
    session.commit()


def join_select():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(account.Users).join(account.UCRelation, account.Users.pid == account.UCRelation.user_pid)\
        .filter(account.UCRelation.contract_pid == 3).all()
    for row in result:
        print(row.username, row.role, row.credit)


def user_update():
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(account.Users).filter(account.Users.pid == 1).update({account.Users.username: "Tom"})
    session.commit()


def user_delete():
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(account.Users).filter(account.Users.pid == 1).delete()
    session.commit()
