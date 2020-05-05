import sys
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
sys.path.append("/home/stardust/A-Bare-Metal-Marketplace/database_setup")
sys.path.append("/home/stardust/A-Bare-Metal-Marketplace/database_setup/Models")
import database_setup.Models.marketModel as Market
import database_setup.statuses as statuses
import database_setup.data as data


engine = create_engine("mysql+pymysql://marketplace:123456@localhost/market")


def bid_insert(values):
    Session = sessionmaker(bind=engine)
    session = Session()
    bid = Market.Bids(bid_id=values['bid_id'], project_id=values['project_id'], quantity=values['quantity'],
                      start_time=values['start_time'], end_time=values['end_time'], expire_time=values['expire_time'],
                      duration=values['duration'], status=values['status'], config_query=values['config_query'],
                      cost=values['cost'])
    session.add(bid)
    session.commit()


def offer_insert(values):
    Session = sessionmaker(bind=engine)
    session = Session()
    offer = Market.Offers(project_id=values['project_id'], status=values['status'], resource_id=values['resource_id'],
                          offer_id=values['offer_id'], start_time=values['start_time'], end_time=values['end_time'],
                          expire_time=values['expire_time'], config=values['config'], cost=values['cost'])
    session.add(offer)
    session.commit()


def insert(values, contract_id, offer_id, bid_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    contract = Market.Contracts(contract_id=values['contract_id'], status=values['status'],
                                start_time=values['start_time'], end_time=values['end_time'], cost=values['cost'])
    relation = Market.CBORelation(contract_id=contract_id, offer_id=offer_id, bid_id=bid_id)
    session.add_all([contract, relation])
    session.commit()


def contract_insert(values):
    Session = sessionmaker(bind=engine)
    session = Session()
    contract = Market.Contracts(contract_id=values['contract_id'], status=values['status'],
                                start_time=values['start_time'], end_time=values['end_time'], cost=values['cost'])
    session.add(contract)
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


def bid_select_all_available():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Market.Bids).filter(Market.Bids.status == statuses.AVAILABLE).all()
    session.close()
    return result


def offer_select_all_available():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Market.Offers).filter(Market.Offers.status == statuses.AVAILABLE).all()
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


def bid_update_by_id(bid_id, bid):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Market.Bids).filter(Market.Bids.bid_id == bid_id).update(bid)
    session.commit()


def offer_update_by_id(offer_id, offer):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Market.Offers).filter(Market.Offers.offer_id == offer_id).update(offer)
    session.commit()


def contract_update_by_id(contract_id, contract):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Market.Contracts).filter(Market.Contracts.contract_id == contract_id).update(contract)
    session.commit()


def bid_update_status_by_id(bid_id, status):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Market.Bids).filter(Market.Bids.bid_id == bid_id).update({"status": status})
    session.commit()


def offer_update_status_by_id(offer_id, status):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Market.Offers).filter(Market.Offers.offer_id == offer_id).update({"status": status})
    session.commit()



# for bid in data.bids:
#     bid_insert(bid)
# for offer in data.offers:
#     offer_insert(offer)
# bid_insert({'bid_id': '24ea1cc1-811f-437e-a748-b8a0f00cd401', 'project_id': 'ba0ee0fe-ee77-474e-8588-cf6a023c6c05', 'quantity': 1, 'start_time': datetime(2020, 2, 29, 10, 30), 'end_time': datetime(2020, 3, 1, 10, 30), 'expire_time': datetime(2020, 3, 10, 10, 30), 'duration': 16400, 'status': 'available', 'config_query': {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3}, 'cost': 11})

