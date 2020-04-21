from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import Models.renterModel as Renter
import data

engine = create_engine("mysql+pymysql://user:pwd@localhost/renter")


def user_insert(values):
    Session = sessionmaker(bind=engine)
    session = Session()
    user = Renter.Users(username=values['username'], role=values['role'], credit=values['credit'])
    session.add(user)
    session.commit()


def bid_insert(values):
    Session = sessionmaker(bind=engine)
    session = Session()
    bid = Renter.Bids(bid_id=values['bid_id'], project_id=values['project_id'], quantity=values['quantity'],
                      start_time=values['start_time'], end_time=values['end_time'], duration=values['duration'],
                      status=values['status'], config_query=values['config_query'], cost=values['cost'])
    session.add(bid)
    session.commit()


def contract_insert(values):
    Session = sessionmaker(bind=engine)
    session = Session()
    contract = Renter.Contracts(contract_id=values['contract_id'], status=values['status'],
                                start_time=values['start_time'], end_time=values['end_time'], cost=values['cost'],
                                project_id=values['project_id'])
    session.add(contract)
    session.commit()


def ucrelation_insert(user_id, contract_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    relation = Renter.UCRelation(user_id=user_id, contract_id=contract_id)
    session.add(relation)
    session.commit()


def ubrelation_insert(user_id, bid_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    relation = Renter.UBRelation(user_id=user_id, offer_id=bid_id)
    session.add(relation)
    session.commit()


def bid_select_by_id(bid_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Renter.Bids).filter(Renter.Bids.bid_id == bid_id).one()
    session.close()
    return result


def contract_select_by_id(contract_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Renter.Contracts).filter(Renter.Contracts.contract_id == contract_id).one()
    session.close()
    return result


def ucrelation_select_by_user_id(user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Renter.UCRelation).filter(Renter.UCRelation.user_id == user_id).one()
    session.close()
    return result


def ubrelation_select_by_user_id(user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Renter.UBRelation).filter(Renter.UBRelation.user_id == user_id).one()
    session.close()
    return result


def user_select_all():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Renter.Users).all()
    session.close()
    return result


def bid_select_all():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Renter.Bids).all()
    session.close()
    return result


def contract_select_all():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Renter.Contracts).all()
    session.close()
    return result


def ubrelation_select_all():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Renter.UBRelation).all()
    session.close()
    return result


def ucrelation_select_all():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Renter.UCRelation).all()
    session.close()
    return result


def bid_delete_by_id(bid_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Renter.Bids).filter(Renter.Bids.bid_id == bid_id).delete()
    session.commit()


def user_delete_by_id(user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Renter.Users).filter(Renter.Users.user_id == user_id).delete()
    session.commit()


def contract_delete_by_id(contract_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Renter.Contracts).filter(Renter.Contracts.contract_id == contract_id).delete()
    session.commit()


def ubrelation_delete_by_user_id(user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Renter.UBRelation).filter(Renter.UBRelation.user_id == user_id).delete()
    session.commit()


def ucrelation_delete_by_user_id(user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Renter.UCRelation).filter(Renter.UCRelation.user_id == user_id).delete()
    session.commit()

