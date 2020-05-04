# flaskapp.py

from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger, ForeignKey

import sqlalchemy_jsonfield

from datetime import datetime
import os
import sys

from multiprocessing import Process, Value
import time

import statuses

now = datetime.now()
# print(now)
current_time = now.strftime("%Y%m%d%H%M")

# Init App
app = Flask(__name__)

# DB Connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://marketplace:123456@localhost/market'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB Init
db = SQLAlchemy(app)

# Marshmallow Init 
ma = Marshmallow(app)

# Bids
class Bids(db.Model):
    bid_id = db.Column(db.String(64), primary_key=True)
    project_id = db.Column(db.String(64), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.DateTime(timezone=True), nullable=False)
    end_time = db.Column(db.DateTime(timezone=True), nullable=False)
    expire_time = db.Column(db.DateTime(timezone=True), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(16), nullable=False, default=statuses.AVAILABLE)
    config_query = db.Column(db.JSON( 
        #enforce_string=True,
        #enforce_unicode=False
        ), nullable=False)
    cost = db.Column(db.Float, nullable=False)

    def __init__(self, bid_id, project_id, quantity, start_time, end_time, expire_time, duration, status, config_query, cost):
        self.bid_id = bid_id
        self.project_id = project_id
        self.quantity = quantity
        self.start_time = start_time
        self.end_time = end_time
        self.expire_time = expire_time
        self.duration = duration
        self.status = status
        self.config_query = config_query
        self.cost = cost  

# Bid Schema 
class BidSchema(ma.Schema):
    class Meta:
        fields = ('bid_id', 'project_id', 'quantity', 'start_time', 'end_time', 'expire_time', 'duration', 'status', 'config_query', 'cost')

# Offers
class Offers(db.Model):
    offer_id = db.Column(db.String(64), primary_key=True)
    project_id = db.Column(db.String(64), nullable=False)
    status = db.Column(db.String(16), nullable=False, default=statuses.AVAILABLE)
    resource_id = db.Column(db.String(64), nullable=False)
    start_time = db.Column(db.DateTime(timezone=True), nullable=False)
    end_time = db.Column(db.DateTime(timezone=True), nullable=False)
    expire_time = db.Column(db.DateTime(timezone=True), nullable=False)
    config = db.Column(db.JSON(
    ), nullable=False)
    cost = db.Column(db.Float, nullable=False)

    def __init__(self, offer_id, project_id, start_time, end_time, expire_time, status, resource_id, config, cost):
        self.offer_id = offer_id
        self.project_id = project_id
        self.status = status
        self.resource_id = resource_id
        self.start_time = start_time
        self.end_time = end_time
        self.expire_time = expire_time
        self.config = config
        self.cost = cost


# Offers Schema 
class OfferSchema(ma.Schema):
    class Meta:
        fields = ('offer_id', 'project_id', 'start_time', 'end_time', 'expire_time', 'status', 'resource_id', 'config', 'cost')

# Contracts
class Contracts(db.Model):
    contract_id = db.Column(db.String(64), primary_key=True)
    status = db.Column(db.String(16), nullable=False, default=statuses.AVAILABLE)
    start_time = db.Column(db.DateTime(timezone=True), nullable=False)
    end_time = db.Column(db.DateTime(timezone=True), nullable=False)
    cost = db.Column(db.Float, nullable=False)
#    project_id = db.Column(db.String(64), nullable=False)

    def __init__(self, contract_id, status, start_time, end_time, cost):
        self.contract_id = contract_id
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.cost = cost
#        self.project_id  =     project_id 

# Contracts Schema
class ContractSchema(ma.Schema):
    class Meta:
        fields = ('contract_id', 'status', 'start_time', 'end_time', 'cost')

# cbo_relation
class cbo_relation(db.Model):
    pid = db.Column(db.BigInteger, primary_key=True)
    contract_id = db.Column(db.String(64), db.ForeignKey("contracts.contract_id"))
    offer_id = db.Column(db.String(64), db.ForeignKey("offers.offer_id"))
    bid_id = db.Column(db.String(64), db.ForeignKey("bids.bid_id"))

    def __init__(self, contract_id, offer_id, bid_id):
        # self.pid = pid
        self.contract_id = contract_id  
        self.offer_id = offer_id
        self.bid_id = bid_id

# cbo_relation Schema
class cbo_relationSchema(ma.Schema):
    class Meta:
        fields = ('contract_id', 'offer_id', 'bid_id')


# Init Schemas
bid_schema = BidSchema()
bids_schema = BidSchema(many=True)
offer_schema = OfferSchema()
offers_schema = OfferSchema(many=True)
contract_schema = ContractSchema()
contracts_schema = ContractSchema(many=True)
cbo_relation_schema = cbo_relationSchema()
cbo_relations_schema = cbo_relationSchema(many=True)


# Route connections
@app.route("/add_bid", methods=['POST'])
def add_bid():
    bid_id = request.json['bid_id']
    project_id = request.json['project_id']
    quantity = request.json['quantity']
    start_time_l = request.json['start_time']
    end_time_l = request.json['end_time']
    expire_time_l = request.json['expire_time']
    duration = request.json['duration']
    status = request.json['status']
    config_query = request.json['config_query']
    cost = request.json['cost'] 

    start_time = datetime(start_time_l[0], start_time_l[1], start_time_l[2], start_time_l[3], start_time_l[4])
    end_time = datetime(end_time_l[0], end_time_l[1], end_time_l[2], end_time_l[3], end_time_l[4])
    expire_time = datetime(expire_time_l[0], expire_time_l[1], expire_time_l[2], expire_time_l[3], expire_time_l[4])

    #bid_id= '0003c7d9-4e3d-4165-9c93-d423275b76ba'
    #project_id= 'ba0ee0fe-ee77-474e-8588-cf6a023c6c05'
    #quantity= 420
    #start_time= datetime(2020, 2, 29, 10, 30)
    #end_time= datetime(2020, 3, 1, 10, 30)
    #expire_time= datetime(2020, 3, 10, 10, 30)
    #duration= 16400
    #status= 'available'
    #config_query = {'memory_gb': 10240, 'cpu_arch': 'x86_64', 'cpu_physical_count': 4, 'cpu_core_count': 16, 'cpu_ghz': 3} 
    #cost= 11

    new_bid = Bids(bid_id, project_id, quantity, start_time, end_time, expire_time, duration, status, config_query, cost)

    db.session.add(new_bid)
    db.session.commit()

    return bid_schema.jsonify(new_bid)


@app.route('/get_bids', methods=['GET'])
def get_bids():
    all_bids = Bids.query.all()
    result = bids_schema.dump(all_bids)
    return jsonify(result)


@app.route("/add_offer", methods=['POST'])
def add_offer():

    offer_id = request.json['offer_id']
    project_id = request.json['project_id']
    resource_id = request.json['resource_id']
    start_time_l = request.json['start_time']
    end_time_l = request.json['end_time']
    expire_time_l = request.json['expire_time']
    status = request.json['status']
    config = request.json['config']
    cost = request.json['cost'] 

    start_time = datetime(start_time_l[0], start_time_l[1], start_time_l[2], start_time_l[3], start_time_l[4])
    end_time = datetime(end_time_l[0], end_time_l[1], end_time_l[2], end_time_l[3], end_time_l[4])
    expire_time = datetime(expire_time_l[0], expire_time_l[1], expire_time_l[2], expire_time_l[3], expire_time_l[4])

    new_offer = Offers(offer_id, project_id, start_time, end_time, expire_time, status, resource_id, config, cost)

    db.session.add(new_offer)
    db.session.commit()

    return offer_schema.jsonify(new_offer)

@app.route('/get_offers', methods=['GET'])
def get_offers():
    all_offers = Offers.query.all()
    result = offers_schema.dump(all_offers)
    return jsonify(result)


@app.route("/add_contract", methods=['POST'])
def add_contract():

    contract_id = request.json['contract_id']
#    project_id = request.json['project_id']
    start_time_l = request.json['start_time']
    end_time_l = request.json['end_time']
    status = request.json['status']
    cost = request.json['cost']

    start_time = datetime(start_time_l[0], start_time_l[1], start_time_l[2], start_time_l[3], start_time_l[4])
    end_time = datetime(end_time_l[0], end_time_l[1], end_time_l[2], end_time_l[3], end_time_l[4])

    new_contract = Contracts(contract_id, status, start_time, end_time, cost)

    db.session.add(new_contract)
    db.session.commit()

    return contract_schema.jsonify(new_contract)

@app.route('/get_contracts', methods=['GET'])
def get_contracts():
    all_contracts = Contracts.query.all()
    result = contracts_schema.dump(all_contracts)
    return jsonify(result)


@app.route("/add_cbo", methods=['POST'])
def add_cbo():
#    pid = request.json['pid']
    contract_id = request.json['contract_id']
    offer_id = request.json['offer_id']
    bid_id = request.json['bid_id']

    new_cbo = cbo_relation(contract_id, offer_id, bid_id)

    db.session.add(new_cbo)
    db.session.commit()

    return cbo_relation_schema.jsonify(new_cbo)


@app.route('/get_cbos', methods=['GET'])
def get_cbos():
    all_cbos = cbo_relation.query.all()
    result = cbo_relation_schema.dump(all_cbos)
    return jsonify(result)


###################################################################################### ALGORITHMICS ###############################################

class Bid:
    def __init__(self, id1, memory, cpu_arch, cpu_physical_count, cpu_core_count, cpu_ghz, cost, start_time, end_time,
                 expiry_time):
        self.bidID = id1
        self.requirements = [memory, cpu_arch, cpu_physical_count, cpu_core_count, cpu_ghz]
        self.cost = cost
        self.start_time = int(start_time.strftime("%Y%m%d%H%M"))
        self.end_time = int(end_time.strftime("%Y%m%d%H%M"))
        self.expiry_time = int(expiry_time.strftime("%Y%m%d%H%M")) - int(current_time)


class Offer:
    def __init__(self, id1, memory, cpu_arch, cpu_physical_count, cpu_core_count, cpu_ghz, cost, start_time, end_time,
                 expiry_time):
        self.offerID = id1
        self.requirements = [memory, cpu_arch, cpu_physical_count, cpu_core_count, cpu_ghz]
        self.cost = cost
        self.start_time = int(start_time.strftime("%Y%m%d%H%M"))
        self.end_time = int(end_time.strftime("%Y%m%d%H%M"))
        self.expiry_time = int(expiry_time.strftime("%Y%m%d%H%M")) - int(current_time)


class Contract:
    def __init__(self, Offer, Bid, cost, start_time, end_time):
        self.bidID = Bid.bidID
        self.offerID = Offer.offerID
        self.start_time =start_time
        self.end_time = end_time
        self.contractID = "e7de4e71-163d-4627-934c-1b5db1348c0b"
        # self.allocation_time = Offer.allocation_time
        self.cost = cost


# Database Pulls
def list_bids():
    result = []
    db_result = Bids.query.all()
    for db_bid in db_result:
        config = db_bid.config_query
        result.append(Bid(db_bid.bid_id, config.get('memory_gb'), config.get('cpu_arch'),
                          config.get('cpu_physical_count'), config.get('cpu_core_count'), config.get('cpu_ghz'),
                          db_bid.cost, db_bid.start_time, db_bid.end_time , db_offer.expiry_time))
    return result

def list_offers():
    result = []
    db_result = Offers.query.all()
    for db_offer in db_result:
        config = db_offer.config
        result.append(Offer(db_offer.offer_id, config.get('memory_gb'), config.get('cpu_arch'),
                            config.get('cpu_physical_count'), config.get('cpu_core_count'), config.get('cpu_ghz'),
                            db_offer.cost, db_offer.start_time, db_offer.end_time, db_offer.expiry_time))
    return result


def insert_contract(contracts):
    for contract in contracts:
        new_contract = Contracts(contract.contractID, statuses.AVAILABLE, contract.start_time, contract.end_time,
                                 contract.cost)
        db.session.add(new_contract)
        new_cbo = cbo_relation(contract.contractID, contract.offerID, contract.bidID)
        db.session.commit()
        db.session.add(new_cbo)
        db.session.commit()
        Bids.query.filter(Bids.bid_id == contract.bidID).update({"status": statuses.MATCHED})
        Offers.query.filter(Offers.offer_id == contract.offerID).update({"status": statuses.MATCHED})
        db.session.commit()

def handle_matcher():
    pass


@app.route('/insert', methods=['GET'])
def insert():
    b = Bid("0165c7d6-4e3d-4165-9c93-d423275a76bf", 10240, "x86_64", 4, 16, 3, 10, datetime(2020, 5, 2, 20, 00),
            datetime(2020, 5, 2, 22, 00), datetime(2020, 5, 1, 10, 00))
    o = Offer("08d727a9-485a-4bf8-82e0-ee5f724e2020", 10240, "x86_64", 4, 16, 3, 20, datetime(2020, 5, 2, 10, 00),
              datetime(2020, 5, 2, 12, 00), datetime(2020, 5, 1, 8, 00))
    c = Contract(o, b, 10, datetime(2020, 5, 2, 20, 00), datetime(2020, 5, 2, 22, 00))
    contracts = [c]
    insert_contract(contracts)
    return jsonify("inserted contract")


@app.route('/force_matcher', methods=['GET'])
def force_matcher():
    handle_matcher()
    return render_template("matcher.html")


@app.route('/update_status', methods=['GET'])
def update_status():
    pass

def loop_matcher(delay):
    while(True):
        print('Matcher Automatically Run')
        handle_matcher()
        time.sleep(delay)

# Run Server
if __name__ == "__main__":
   matcher_delay = 3600 # 1 hour in seconds
   p = Process(target=loop_matcher, args=(matcher_delay,))
   p.start()  
   app.run(host='0.0.0.0', debug=True, use_reloader=False)
   p.join()

