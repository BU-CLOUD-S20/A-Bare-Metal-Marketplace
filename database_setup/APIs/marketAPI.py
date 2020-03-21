from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import Models.marketModel as Market

engine = create_engine("mysql+pymysql://user:pwd@localhost/market")


def bid_insert(quantity, start_time, end_time, duration, status, config_query, cost):
    Session = sessionmaker(bind=engine)
    session = Session()
    bid = Market.Bids(quantity=quantity, start_time=start_time, end_time=end_time, duration=duration, status=status,
                      config_query=config_query, cost=cost)
    session.add(bid)
    session.flush()
    pid = bid.pid
    session.commit()


def offer_insert(status, resource_id, resource_type, start_time, end_time, config, cost):
    Session = sessionmaker(bind=engine)
    session = Session()
    offer = Market.Offers(status=status, resource_id=resource_id, resource_type=resource_type, start_time=start_time,
                          end_time=end_time, config=config, cost=cost)
    session.add(offer)
    session.flush()
    pid = offer.pid
    session.commit()


def contract_insert(status, start_time, end_time, cost):
    Session = sessionmaker(bind=engine)
    session = Session()
    offer = Market.Offers(status=status, start_time=start_time, end_time=end_time, cost=cost)
    session.add(offer)
    session.flush()
    pid = offer.pid
    session.commit()


def relation_insert(contract_pid, offer_pid, bid_pid):
    Session = sessionmaker(bind=engine)
    session = Session()
    relation = Market.CBORelation(contract_pid, offer_pid, bid_pid)
    session.add(relation)
    session.commit()


def bid_select_by_pid(pid):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Market.Bids).filter(Market.Bids.pid == pid)
    for row in result:
        print(row)


def offer_select_by_pid(pid):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Market.Offers).filter(Market.Offers.pid == pid)
    for row in result:
        print(row)


def contract_select_by_pid(pid):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Market.Contracts).filter(Market.Contracts.pid == pid)
    for row in result:
        print(row)


def relation_select_by_pid(pid):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Market.CBORelation).filter(Market.CBORelation.contract_pid == pid)
    for row in result:
        return row.offer_pid, row.bid_pid


def bid_select_all():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Market.Bids).all()
    return result


def bid_delete_by_pid(pid):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Market.Bids).filter(Market.Bids.pid == pid).delete()
    session.commit()


def offer_delete_by_pid(pid):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Market.Offers).filter(Market.Offers.pid == pid).delete()
    session.commit()


def contract_delete_by_pid(pid):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Market.Contracts).filter(Market.Contracts.pid == pid).delete()
    session.commit()


def relation_delete_by_pid(pid):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Market.CBORelation).filter(Market.CBORelation.contract_pid == pid).delete()
    session.commit()
