# flaskAccount.py

from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger, ForeignKey, or_

import sqlalchemy_jsonfield

from datetime import datetime
import os
import sys
import statuses

now = datetime.now()
# print(now)
current_time = now.strftime("%Y%m%d%H%M")

# Init App
app = Flask(__name__)

# DB Connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://remote:123456@206.189.232.188/account'
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

    def __init__(self, contract_id, status, start_time, end_time, cost):
        self.contract_id = contract_id
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.cost = cost


# Contracts Schema
class ContractSchema(ma.Schema):
    class Meta:
        fields = ('contract_id', 'status', 'start_time', 'end_time', 'cost')


# uc_relation
class uc_relation(db.Model):
    pid = db.Column(db.BigInteger, primary_key=True)
    contract_id = db.Column(db.String(64), db.ForeignKey("contracts.contract_id"))
    provider_id = db.Column(db.String(64), db.ForeignKey("users.user_id"))
    renter_id = db.Column(db.String(64), db.ForeignKey("users.user_id"))

    def __init__(self, contract_id, provider_id, renter_id):
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


@app.route('/get_user', methods=['GET'])
def get_user():
    user_id = request.json['project_id']
    user = Users.query.filter(Users.user_id == user_id).one()
    return jsonify(user.credit)


@app.route('/get_contract', methods=['GET'])
def get_contract():
    user_id = request.json['project_id']
    all_uc = uc_relation.query.filter(or_(uc_relation.provider_id == user_id, uc_relation.renter_id == user_id)).all()
    contracts = []
    for uc in all_uc:
        contracts.append(Contracts.query.filter(Contracts.contract_id == uc.contract_id).one())
    result = contracts_schema.dump(contracts)
    return jsonify(result)


@app.route("/add_contract", methods=['POST'])
def add_contract():
    contract_id = request.json['contract_id']
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


@app.route("/add_uc", methods=['POST'])
def add_uc():

    contract_id = request.json['contract_id']
    provider_id = request.json['provider_id']
    renter_id = request.json['renter_id']

    new_uc = uc_relation(contract_id, provider_id, renter_id)

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


def is_renter_valid(renter, contract):
    if renter.credit >= contract.cost:
        return True
    else:
        return False


def credit_transfer(renter, provider, contract):
    renter.credit = renter.credit - contract.cost
    provider.credit = provider.credit + contract.cost
    return renter, provider


# def transaction(renters, providers, contracts):
#     size = len(contracts)
#     invalid_contracts = []
#     result_renters = []
#     result_providers = []
#     result_contracts = []
#
#     for i in range(size):
#         renter = renters[i]
#         provider = providers[i]
#         contract = contracts[i]
#         if is_renter_valid(renter, contract):
#             new_renter, new_provider = credit_transfer(renter, provider, contract)
#             result_renters.append(new_renter)
#             result_providers.append(new_provider)
#             result_contracts.append(contract)
#             update_credit(new_renter.id, new_renter.credit)
#             update_credit(new_provider.id, new_provider.credit)
#             update_status(contract.id, statuses.CONFIRMED)
#         else:
#             invalid_contracts.append(contract)
#
#     return result_renters, result_providers, result_contracts, invalid_contracts

class Response:
    def __init__(self, flag, contract, provider, renter):
        self.flag = flag
        self.contract = contract
        self.provider = provider
        self.renter = renter


def transaction(contract, provider, renter):

    if is_renter_valid(renter, contract):
        new_renter, new_provider = credit_transfer(renter, provider, contract)
        Users.query.filter(Users.user_id == new_renter.user_id).update({"credit": new_renter.credit})
        Users.query.filter(Users.user_id == new_provider.user_id).update({"credit": new_provider.credit})
        contract.status = statuses.CONFIRMED
        db.session.add(contract)
        db.session.commit()
        relation = uc_relation(contract.contract_id, new_provider.user_id, new_renter.user_id)
        db.session.add(relation)
        db.session.commit()
        return Response(True, contract, new_provider, new_renter)
    else:
        return Response(False, contract, provider, provider)


# def get_data():
#     renters = []
#     providers = []
#     contracts = []
#     relations = uc_relation.query.join(Contracts).filter(Contracts.status == statuses.AVAILABLE).all()
#     for relation in relations:
#         p = get_user_by_id(relation.provider_id)
#         r = get_user_by_id(relation.renter_id)
#         c = get_contract_by_id(relation.contract_id)
#         renter = Renter(r.user_id, r.credit)
#         provider = Provider(p.user_id, p.credit)
#         contract = Contract(c.contract_id, renter, provider, c.cost)
#         renters.append(renter)
#         providers.append(provider)
#         contracts.append(contract)
#     return renters, providers, contracts


@app.route('/run_transaction', methods=['POST'])
def run_transaction():
    contract_id = request.json['contract_id']
    start_time_l = request.json['start_time']
    end_time_l = request.json['end_time']
    status = request.json['status']
    cost = request.json['cost']
    provider_id = request.json['provider_id']
    renter_id = request.json['renter_id']

    start_time = datetime(start_time_l[0], start_time_l[1], start_time_l[2], start_time_l[3], start_time_l[4])
    end_time = datetime(end_time_l[0], end_time_l[1], end_time_l[2], end_time_l[3], end_time_l[4])

    # contract_id = "abc"
    # start_time = datetime(2020, 6, 1, 10, 00)
    # end_time = datetime(2020, 6, 2, 12, 00)
    # status = "available"
    # cost = 7
    # provider_id = "p1"
    # renter_id = "r1"

    contract = Contracts(contract_id, status, start_time, end_time, cost)
    print(provider_id)
    print(renter_id)
    provider = Users.query.filter(Users.user_id == provider_id).one()
    renter = Users.query.filter(Users.user_id == renter_id).one()

    response = transaction(contract, provider, renter)

    data = {'flag': response.flag}
    return jsonify(data)


    # renters_list, providers_list, contracts_list = get_data()
    # result_renters, result_providers, result_contracts, invalid_contracts = transaction(renters_list, providers_list,
    #                                                                                     contracts_list)
    #
    # return jsonify(users_schema.dump(result_renters), users_schema.dump(result_providers),
    #                contracts_schema.dump(result_contracts), contracts_schema.dump(invalid_contracts))


# Run Server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
