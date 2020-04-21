import sys
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
sys.path.append("/home/stardust/A-Bare-Metal-Marketplace/database_setup")
sys.path.append("/home/stardust/A-Bare-Metal-Marketplace/database_setup/Models")
import Models.providerModel as Provider
import data

engine = create_engine("mysql+pymysql://marketplace:123456@localhost/provider")


def user_insert(values):
    Session = sessionmaker(bind=engine)
    session = Session()
    user = Provider.Users(username=values['username'], role=values['role'], credit=values['credit'])
    session.add(user)
    session.commit()


def offer_insert(values):
    Session = sessionmaker(bind=engine)
    session = Session()
    offer = Provider.Offers(project_id=values['project_id'], status=values['status'], resource_id=values['resource_id'],
                            offer_id=values['offer_id'], start_time=values['start_time'], end_time=values['end_time'],
                            config=values['config'], cost=values['cost'])
    session.add(offer)
    session.commit()


def contract_insert(values):
    Session = sessionmaker(bind=engine)
    session = Session()
    contract = Provider.Contracts(contract_id=values['contract_id'], status=values['status'],
                                  start_time=values['start_time'], end_time=values['end_time'], cost=values['cost'],
                                  project_id=values['project_id'])
    session.add(contract)
    session.commit()


def ucrelation_insert(user_id, contract_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    relation = Provider.UCRelation(user_id=user_id, contract_id=contract_id)
    session.add(relation)
    session.commit()


def uorelation_insert(user_id, offer_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    relation = Provider.UORelation(user_id=user_id, offer_id=offer_id)
    session.add(relation)
    session.commit()


def offer_select_by_id(offer_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Provider.Offers).filter(Provider.Offers.offer_id == offer_id).one()
    session.close()
    return result


def contract_select_by_id(contract_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Provider.Contracts).filter(Provider.Contracts.contract_id == contract_id).one()
    session.close()
    return result


def ucrelation_select_by_user_id(user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Provider.UCRelation).filter(Provider.UCRelation.user_id == user_id).one()
    session.close()
    return result


def uorelation_select_by_user_id(user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Provider.UORelation).filter(Provider.UORelation.user_id == user_id).one()
    session.close()
    return result


def user_select_all():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Provider.Users).all()
    session.close()
    return result


def offer_select_all():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Provider.Offers).all()
    session.close()
    return result


def contract_select_all():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Provider.Contracts).all()
    session.close()
    return result


def uorelation_select_all():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Provider.UORelation).all()
    session.close()
    return result


def ucrelation_select_all():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Provider.UCRelation).all()
    session.close()
    return result


def offer_delete_by_id(offer_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Provider.Offers).filter(Provider.Offers.offer_id == offer_id).delete()
    session.commit()


def user_delete_by_id(user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Provider.Users).filter(Provider.Users.user_id == user_id).delete()
    session.commit()


def contract_delete_by_id(contract_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Provider.Contracts).filter(Provider.Contracts.contract_id == contract_id).delete()
    session.commit()


def uorelation_delete_by_user_id(user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Provider.UORelation).filter(Provider.UORelation.user_id == user_id).delete()
    session.commit()


def ucrelation_delete_by_user_id(user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Provider.UCRelation).filter(Provider.UCRelation.user_id == user_id).delete()
    session.commit()

