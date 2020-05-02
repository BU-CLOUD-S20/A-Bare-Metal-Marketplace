# flaskAccount.py

from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger, ForeignKey

import sqlalchemy_jsonfield

from datetime import datetime
import os
import sys
import database_setup.statuses as statuses

now = datetime.now()
# print(now)
current_time = now.strftime("%Y%m%d%H%M")

# Init App
app = Flask(__name__)

# DB Connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://marketplace:123456@localhost/renter'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB Init
db = SQLAlchemy(app)

# Marshmallow Init
ma = Marshmallow(app)


# Users
class Users(db.Model):
    user_id = db.Column(db.String(64), primary_key=True, autoincrement=False)
    username = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(16), nullable=False)
    credit = db.Column(db.Float, nullable=False)

    def __init__(self, user_id, username, role, credit):
        self.user_id = user_id
        self.username = username
        self.role = role
        self.credit = credit


# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'username', 'role', 'credit')


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
    config_query = db.Column(db.JSON(), nullable=False)
    cost = db.Column(db.Float, nullable=False)

    def __init__(self, bid_id, project_id, quantity, start_time, end_time, expire_time, duration, status, config_query,
                 cost):
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
        fields = ('bid_id', 'project_id', 'quantity', 'start_time', 'end_time', 'expire_time', 'duration', 'status',
                  'config_query', 'cost')


# Contracts
class Contracts(db.Model):
    contract_id = db.Column(db.String(64), primary_key=True)
    status = db.Column(db.String(16), nullable=False, default=statuses.AVAILABLE)
    start_time = db.Column(db.DateTime(timezone=True), nullable=False)
    end_time = db.Column(db.DateTime(timezone=True), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    project_id = db.Column(db.String(64), nullable=False)

    def __init__(self, contract_id, status, start_time, end_time, cost, project_id):
        self.contract_id = contract_id
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.cost = cost
        self.project_id = project_id


# Contracts Schema
class ContractSchema(ma.Schema):
    class Meta:
        fields = ('contract_id', 'status', 'start_time', 'end_time', 'cost', 'project_id')


# uo_relation
class ub_relation(db.Model):
    pid = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.String(64), db.ForeignKey("users.user_id"))
    bid_id = db.Column(db.String(64), db.ForeignKey("bids.bid_id"))

    def __init__(self, pid, user_id, bid_id):
        self.pid = pid
        self.user_id = user_id
        self.bid_id = bid_id


# uo_relation Schema
class ub_relationSchema(ma.Schema):
    class Meta:
        fields = ('pid', 'user_id', 'bid_id')


# uc_relation
class uc_relation(db.Model):
    pid = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.String(64), db.ForeignKey("users.user_id"))
    contract_id = db.Column(db.String(64), db.ForeignKey("contracts.contract_id"))

    def __init__(self, pid, user_id, contract_id):
        self.pid = pid
        self.user_id = user_id
        self.contract_id = contract_id


# uc_relation Schema
class uc_relationSchema(ma.Schema):
    class Meta:
        fields = ('pid', 'user_id', 'contract_id')


# Init Schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)
bid_schema = BidSchema()
bids_schema = BidSchema(many=True)
contract_schema = ContractSchema()
contracts_schema = ContractSchema(many=True)
ub_relation_schema = ub_relationSchema()
ub_relations_schema = ub_relationSchema(many=True)
uc_relation_schema = uc_relationSchema()
uc_relations_schema = uc_relationSchema(many=True)


# Route connections
@app.route("/add_user", methods=['POST'])
def add_user():
    user_id = request.json['user_id']
    username = request.json['username']
    role = request.json['role']
    credit = request.json['credit']

    new_user = Users(user_id, username, role, credit)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)


@app.route('/get_users', methods=['GET'])
def get_users():
    all_users = Users.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)


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

    new_bid = Bids(bid_id, project_id, quantity, start_time, end_time, expire_time, duration, status, config_query, cost)

    db.session.add(new_bid)
    db.session.commit()

    return bid_schema.jsonify(new_bid)


@app.route('/get_bids', methods=['GET'])
def get_bids():
    all_bids = Bids.query.all()
    result = bids_schema.dump(all_bids)
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


@app.route("/add_ub", methods=['POST'])
def add_ub():
    pid = request.json['pid']
    user_id = request.json['user_id']
    bid_id = request.json['bid_id']

    new_ub = ub_relation(pid, user_id, bid_id)

    db.session.add(new_ub)
    db.session.commit()

    return ub_relation_schema.jsonify(new_ub)


@app.route('/get_ubs', methods=['GET'])
def get_ubs():
    all_ubs = ub_relation.query.all()
    print(len(all_ubs))
    result = ub_relations_schema.dump(all_ubs)
    return jsonify(result)


@app.route("/add_uc", methods=['POST'])
def add_uc():
    pid = request.json['pid']
    user_id = request.json['user_id']
    contract_id = request.json['contract_id']

    new_uc = uc_relation(pid, user_id, contract_id)

    db.session.add(new_uc)
    db.session.commit()

    return uc_relation_schema.jsonify(new_uc)


@app.route('/get_ucs', methods=['GET'])
def get_ucs():
    all_ucs = uc_relation.query.all()
    print(len(all_ucs))
    result = uc_relations_schema.dump(all_ucs)
    return jsonify(result)


@app.route("/update_bid_status", methods=['POST'])
def update_bid_status():
    bid_id = request.json['bid_id']
    status = request.json['status']
    Bids.query.filter(Bids.bid_id == bid_id).update({"status": status})
    db.session.commit()
    return jsonify(bid_id, status)


@app.route("/update_credit", methods=['POST'])
def update_credit():
    user_id = request.json['user_id']
    credit = request.json['credit']
    Users.query.filter(Users.user_id == user_id).update({"credit": credit})
    db.session.commit()
    return jsonify(user_id, credit)


# Run Server
if __name__ == "__main__":
    # app.run(host='0.0.0.0')
    app.run()
