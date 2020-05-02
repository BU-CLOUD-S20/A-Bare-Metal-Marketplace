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
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://marketplace:123456@localhost/provider'
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
        fields = ('offer_id', 'project_id', 'start_time', 'end_time', 'expire_time', 'status', 'resource_id', 'config',
                  'cost')


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
class uo_relation(db.Model):
    pid = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.String(64), db.ForeignKey("users.user_id"))
    offer_id = db.Column(db.String(64), db.ForeignKey("offers.offer_id"))

    def __init__(self, pid, user_id, offer_id):
        self.pid = pid
        self.user_id = user_id
        self.offer_id = offer_id


# uo_relation Schema
class uo_relationSchema(ma.Schema):
    class Meta:
        fields = ('pid', 'user_id', 'offer_id')


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
offer_schema = OfferSchema()
offers_schema = OfferSchema(many=True)
contract_schema = ContractSchema()
contracts_schema = ContractSchema(many=True)
uo_relation_schema = uo_relationSchema()
uo_relations_schema = uo_relationSchema(many=True)
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


@app.route("/add_uo", methods=['POST'])
def add_uo():
    pid = request.json['pid']
    user_id = request.json['user_id']
    offer_id = request.json['offer_id']

    new_uo = uo_relation(pid, user_id, offer_id)

    db.session.add(new_uo)
    db.session.commit()

    return uo_relation_schema.jsonify(new_uo)


@app.route('/get_uos', methods=['GET'])
def get_uos():
    all_uos = uo_relation.query.all()
    print(len(all_uos))
    result = uo_relations_schema.dump(all_uos)
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


@app.route("/update_offer_status", methods=['POST'])
def update_offer_status():
    offer_id = request.json['offer_id']
    status = request.json['status']
    Offers.query.filter(Offers.offer_id == offer_id).update({"status": status})
    db.session.commit()
    return jsonify(offer_id, status)


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
