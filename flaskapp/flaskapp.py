# flaskapp.py

from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger, ForeignKey

import sqlalchemy_jsonfield

from datetime import datetime
import os
import sys
import statuses

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
        self.start_time =  start_time
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
    project_id = db.Column(db.String(64), nullable=False)

    def __init__(self, contract_id, status, start_time, end_time, cost, project_id):
        self.contract_id =     contract_id
        self.status =     status
        self.start_time =     start_time
        self.end_time =     end_time
        self.cost =      cost
        self.project_id  =     project_id 

# Contracts Schema
class ContractSchema(ma.Schema):
    class Meta:
        fields = ('contract_id', 'status', 'start_time', 'end_time', 'cost', 'project_id')

# cbo_relation
class cbo_relation(db.Model):
    pid = db.Column(db.BigInteger, primary_key=True, auto_increment=True)
    contract_id = db.Column(db.String(64), db.ForeignKey("contracts.contract_id"))
    offer_id = db.Column(db.String(64), db.ForeignKey("offers.offer_id"))
    bid_id = db.Column(db.String(64), db.ForeignKey("bids.bid_id"))

    def __init__(self, pid, contract_id, offer_id, bid_id):
        self.pid = pid
        self.contract_id = contract_id  
        self.offer_id =  offer_id
        self.bid_id =  bid_id

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
    project_id = request.json['project_id']
    start_time_l = request.json['start_time']
    end_time_l = request.json['end_time']
    status = request.json['status']
    cost = request.json['cost'] 

    start_time = datetime(start_time_l[0], start_time_l[1], start_time_l[2], start_time_l[3], start_time_l[4])
    end_time = datetime(end_time_l[0], end_time_l[1], end_time_l[2], end_time_l[3], end_time_l[4])

    new_contract = Contracts(contract_id, status, start_time, end_time, cost, project_id)

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

    pid = request.json['pid']
    contract_id = request.json['contract_id']
    offer_id = request.json['offer_id']
    bid_id = request.json['bid_id']

    new_cbo = cbo_relation(pid, contract_id, offer_id, bid_id)

    db.session.add(new_cbo)
    db.session.commit()

    return cbo_relation_schema.jsonify(new_cbo)

@app.route('/get_cbos', methods=['GET'])
def get_cbos():
    all_cbos = cbo_relation.query.all()
    result = cbo_relation_schema.dump(all_cbos)
    return jsonify(result)

@app.route('/run_matcher', methods=['GET'])
def run_matcher():
    pass

@app.route('/update_status', methods=['GET'])
def update_status():
    pass


# Run Server
if __name__ == "__main__":
    app.run(host='0.0.0.0')