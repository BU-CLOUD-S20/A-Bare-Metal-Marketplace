from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import Models.marketModel as Market
import data

engine = create_engine("mysql+pymysql://user:pwd@localhost/market")


def bid_insert(values):
    Session = sessionmaker(bind=engine)
    session = Session()
    bid = Market.Bids(bid_id=values['bid_id'], project_id=values['project_id'], quantity=values['quantity'],
                      start_time=values['start_time'], end_time=values['end_time'], duration=values['duration'],
                      status=values['status'], config_query=values['config_query'], cost=values['cost'])
    session.add(bid)
    session.commit()


def offer_insert(values):
    Session = sessionmaker(bind=engine)
    session = Session()
    offer = Market.Offers(project_id=values['project_id'], status=values['status'], resource_id=values['resource_id'],
                          offer_id=values['offer_id'],start_time=values['start_time'], end_time=values['end_time'],
                          config=values['config'], cost=values['cost'])
    session.add(offer)
    session.commit()


def contract_insert(values):
    Session = sessionmaker(bind=engine)
    session = Session()
    offer = Market.Offers(contract_id=values['contract_id'], status=values['status'], start_time=values['start_time'],
                          end_time=values['end_time'], cost=values['cost'], project_id=values['project_id'])
    session.add(offer)
    session.commit()


def relation_insert(contract_id, offer_id, bid_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    relation = Market.CBORelation(contract_id=contract_id, offer_id=offer_id, bid_id=bid_id)
    session.add(relation)
    session.commit()


def bid_select_by_id(bid_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Market.Bids).filter(Market.Bids.bid_id == bid_id).one()
    session.close()
    return result


def offer_select_by_id(offer_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Market.Offers).filter(Market.Offers.offer_id == offer_id).one()
    session.close()
    return result


def contract_select_by_id(contract_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Market.Contracts).filter(Market.Contracts.contract_id == contract_id).one()
    session.close()
    return result


def relation_select_by_pid(pid):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Market.CBORelation).filter(Market.CBORelation.pid == pid).one()
    session.close()
    return result


def relation_select_by_contract_id(contract_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Market.CBORelation).filter(Market.CBORelation.contract_id == contract_id).one()
    session.close()
    return result


def bid_select_all():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Market.Bids).all()
    session.close()
    return result


def offer_select_all():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Market.Offers).all()
    session.close()
    return result


def bid_delete_by_id(bid_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Market.Bids).filter(Market.Bids.bid_id == bid_id).delete()
    session.commit()


def offer_delete_by_id(offer_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Market.Offers).filter(Market.Offers.offer_id == offer_id).delete()
    session.commit()


def contract_delete_by_id(contract_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Market.Contracts).filter(Market.Contracts.contract_id == contract_id).delete()
    session.commit()


def relation_delete_by_pid(pid):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Market.CBORelation).filter(Market.CBORelation.pid == pid).delete()
    session.commit()


def relation_delete_by_contract_id(contract_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Market.CBORelation).filter(Market.CBORelation.contract_id == contract_id).delete()
    session.commit()


def bid_update_by_pid(pid, bid):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Market.Bids).filter(Market.Bids.pid == pid).update(bid)
    session.commit()


def offer_update_by_pid(pid, offer):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Market.Bids).filter(Market.Bids.pid == pid).update(offer)
    session.commit()


def contract_update_by_pid(pid, contract):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Market.Bids).filter(Market.Bids.pid == pid).update(contract)
    session.commit()

