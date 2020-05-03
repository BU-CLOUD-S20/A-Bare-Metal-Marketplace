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
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://marketplace:123456@localhost/account'
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


# uc_relation
class uc_relation(db.Model):
    pid = db.Column(db.BigInteger, primary_key=True)
    contract_id = db.Column(db.String(64), db.ForeignKey("contracts.contract_id"))
    provider_id = db.Column(db.String(64), db.ForeignKey("users.user_id"))
    renter_id = db.Column(db.String(64), db.ForeignKey("users.user_id"))

    def __init__(self, pid, contract_id, provider_id, renter_id):
        self.pid = pid
        self.contract_id = contract_id
        self.provider_id = provider_id
        self.renter_id = renter_id


# uc_relation Schema
class uc_relationSchema(ma.Schema):
    class Meta:
        fields = ('pid', 'contract_id', 'provider_id', 'renter_id')


# Init Schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)
contract_schema = ContractSchema()
contracts_schema = ContractSchema(many=True)
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


@app.route("/add_uc", methods=['POST'])
def add_uc():
    pid = request.json['pid']
    contract_id = request.json['contract_id']
    provider_id = request.json['provider_id']
    renter_id = request.json['renter_id']

    new_uc = uc_relation(pid, contract_id, provider_id, renter_id)

    db.session.add(new_uc)
    db.session.commit()

    return uc_relation_schema.jsonify(new_uc)


@app.route('/get_ucs', methods=['GET'])
def get_ucs():
    all_ucs = uc_relation.query.all()
    print(len(all_ucs))
    result = uc_relations_schema.dump(all_ucs)
    return jsonify(result)


def get_user_by_id(user_id):
    user = Users.query.filter(Users.user_id == user_id).one()
    return user


def get_contract_by_id(contract_id):
    contract = Contracts.query.filter(Contracts.contract_id == contract_id).one()
    return contract


def update_status(contract_id, status):
    Contracts.query.filter(Contracts.contract_id == contract_id).update({"status": status})
    db.session.commit()


def update_credit(user_id, credit):
    Users.query.filter(Users.user_id == user_id).update({"credit": credit})
    db.session.commit()

####################################################################################### ALGORITHMICS ###############################################


class Provider:
    def __init__(self, id, credit):
        self.id = id
        self.credit = credit


class Renter:
    def __init__(self, id, credit):
        self.id = id
        self.credit = credit


class Contract:
    def __init__(self, id, Provider, Renter, cost):
        self.id = id
        self.provider_id = Provider.id
        self.renter_id = Renter.id
        self.cost = cost


def is_renter_valid(renter, contract):
    if renter.credit >= contract.cost:
        return True
    else:
        return False


def credit_transfer(renter, provider, contract):
    renter.credit = renter.credit - contract.cost
    provider.credit = provider.credit + contract.cost
    return renter, provider


def transaction(renters, providers, contracts):
    size = len(contracts)
    invalid_contracts = []
    result_renters = []
    result_providers = []
    result_contracts = []

    for i in range(size):
        renter = renters[i]
        provider = providers[i]
        contract = contracts[i]
        if is_renter_valid(renter, contract):
            new_renter, new_provider = credit_transfer(renter, provider, contract)
            result_renters.append(new_renter)
            result_providers.append(new_provider)
            result_contracts.append(contract)
            update_credit(new_renter.id, new_renter.credit)
            update_credit(new_provider.id, new_provider.credit)
            update_status(contract.id, statuses.CONFIRMED)
        else:
            invalid_contracts.append(contract)

    return result_renters, result_providers, result_contracts, invalid_contracts


def get_data():
    renters = []
    providers = []
    contracts = []
    relations = uc_relation.query.join(Contracts).filter(Contracts.status == statuses.AVAILABLE).all()
    for relation in relations:
        p = get_user_by_id(relation.provider_id)
        r = get_user_by_id(relation.renter_id)
        c = get_contract_by_id(relation.contract_id)
        renter = Renter(r.user_id, r.credit)
        provider = Provider(p.user_id, p.credit)
        contract = Contract(c.contract_id, renter, provider, c.cost)
        renters.append(renter)
        providers.append(provider)
        contracts.append(contract)
    return renters, providers, contracts


@app.route('/run_transaction', methods=['GET'])
def run_transaction():
    renters_list, providers_list, contracts_list = get_data()
    result_renters, result_providers, result_contracts, invalid_contracts = transaction(renters_list, providers_list,
                                                                                        contracts_list)

    return jsonify(users_schema.dump(result_renters), users_schema.dump(result_providers),
                   contracts_schema.dump(result_contracts), contracts_schema.dump(invalid_contracts))


# Run Server
if __name__ == "__main__":
    # app.run(host='0.0.0.0')
    app.run()
