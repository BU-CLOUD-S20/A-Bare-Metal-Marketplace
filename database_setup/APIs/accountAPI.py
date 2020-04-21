import sys
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
sys.path.append("/home/stardust/A-Bare-Metal-Marketplace/database_setup")
sys.path.append("/home/stardust/A-Bare-Metal-Marketplace/database_setup/Models")
import Models.accountModel as Account

engine = create_engine("mysql+pymysql://marketplace:123456@localhost/account")


def user_insert(values):
    Session = sessionmaker(bind=engine)
    session = Session()
    user = Account.Users(username=values['username'], role=values['role'], credit=values['credit'])
    session.add(user)
    session.commit()


def contract_insert(values):
    Session = sessionmaker(bind=engine)
    session = Session()
    contract = Account.Contracts(contract_id=values['contract_id'], status=values['status'],
                                 start_time=values['start_time'], end_time=values['end_time'], cost=values['cost'],
                                 project_id=values['project_id'])
    session.add(contract)
    session.commit()


def relation_insert(user_id, contract_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    relation = Account.UCRelation(user_id=user_id, contract_id=contract_id)
    session.add(relation)
    session.commit()


def user_select_by_id(user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Account.Users).filter(Account.Users.user_id == user_id).one()
    session.close()
    return result


def contract_select_by_id(contract_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Account.Contracts).filter(Account.Contracts.contract_id == contract_id).one()
    session.close()
    return result


def relation_select_by_pid(pid):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Account.UCRelation).filter(Account.UCRelation.pid == pid).one()
    session.close()
    return result


def relation_select_by_user_id(user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Account.UCRelation).filter(Account.UCRelation.user_id == user_id).one()
    session.close()
    return result


def user_select_all():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Account.Users).all()
    session.close()
    return result


def contract_select_all():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Account.Contracts).all()
    session.close()
    return result


def relation_select_all():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Account.UCRelation).all()
    session.close()
    return result


def user_delete_by_id(user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Account.Users).filter(Account.Users.user_id == user_id).delete()
    session.commit()


def contract_delete_by_id(contract_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Account.Contracts).filter(Account.Contracts.contract_id == contract_id).delete()
    session.commit()


def relation_delete_by_user_id(user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Account.UCRelation).filter(Account.UCRelation.user_id == user_id).delete()
    session.commit()


def user_update_credit_by_id(user_id, credit):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Account.Users).filter(Account.Users.user_id == user_id).update({"credit": credit})
    session.commit()


def contract_update_by_id(contract_id, contract):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Account.Contracts).filter(Account.Contracts.contract_id == contract_id).update(contract)
    session.commit()


def relation_update_by_id(user_id, relation):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Account.UCRelation).filter(Account.UCRelation.user_id == user_id).update(relation)
    session.commit()


# if __name__ == "__main__":
