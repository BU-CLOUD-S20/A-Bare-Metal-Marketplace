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
import random

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

# Generation of IDs
def generate_id():
    return ''.join(random.choice('0123456789abcdef') for i in range(36))

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

@app.route("/user_add_bid", methods=['POST'])
def user_add_bid():
    bid_id = generate_id()
    project_id = request.json['project_id']
    quantity = request.json['quantity']
    start_time_l = request.json['start_time']
    end_time_l = request.json['end_time']
    expire_time_l = request.json['expire_time']
    duration = 0
    status = statuses.AVAILABLE
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


## ALGORITHMICS ##

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
        self.contractID = generate_id()
        # self.allocation_time = Offer.allocation_time
        self.cost = cost


# Database Pulls
def list_bids():
    db_result = Bids.query.all()
    return db_result

def list_active_bids():
    db_result = Bids.query.filter(Bids.status == "available").all()
    return db_result    

def list_offers():
    db_result = Offers.query.all()
    return db_result

def list_active_offers():
    db_result = Offers.query.filter(Offers.status == "available").all()
    return db_result


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


## START AUCTION.PY ##
# #
def lowest_exp_bids(bids):
    exp = int(bids[0].expire_time.strftime("%Y%m%d%H%M")) - int(current_time)
    for i in range(len(bids)):
        exp2 = int(bids[i].expire_time.strftime("%Y%m%d%H%M")) - int(current_time)
        if exp2 < exp:
            exp = exp2
            current_bid = bids[i]
    return current_bid

# #
def matching_requirements(current_bid, bids):
    current_bids = [current_bid]
    for i in range(len(bids)):
        if current_bid.bid_id != bids[i].bid_id:
            if current_bid.config_query == bids[i].config_query:
                current_bids.append(bids[i])
    return current_bids

# #
def time_clash(bids):
    clash_bids = [bids[0]]
    start_time = int(bids[0].start_time.strftime("%Y%m%d%H%M"))
    end_time = int(bids[0].end_time.strftime("%Y%m%d%H%M"))
    for i in range(len(bids)):
        startIt = int(bids[i].start_time.strftime("%Y%m%d%H%M"))
        if startIt >= start_time:
            if startIt <= end_time:
                clash_bids.append(bids[i])
    return clash_bids

# #
def second_price_auction(bids):
    high_price = 0
    second_price = 0
    expensiveBid = bids[0]
    for i in range(len(bids)):
        if bids[i].cost >= high_price:
            expensiveBid = bids[i]
            second_price = high_price
            #print(second_price, high_price)
            high_price = expensiveBid.cost
        elif second_price < bids[i].cost:
            second_price = bids[i].cost
    if second_price == high_price:
        second_price = 0
        for i in range(len(bids)):
            if bids[i].cost < high_price:
                if bids[i].cost > second_price:
                    second_price = bids[i].cost

    return expensiveBid, second_price + 0.01

# #
def check_offers_price(bid, offers):
    cheaper_offers = []
    for i in range(len(offers)):
        if offers[i].cost <= bid.cost:
            cheaper_offers.append(offers[i])
    return cheaper_offers

# #
def check_time_overlap(bid, offers):
    overlap_offers = []
    for i in range(len(offers)):
        bidStart = int(bid.start_time.strftime("%Y%m%d%H%M"))
        bidEnd = int(bid.end_time.strftime("%Y%m%d%H%M"))
        offerStart = int(offers[i].start_time.strftime("%Y%m%d%H%M"))
        offerEnd = int(offers[i].end_time.strftime("%Y%m%d%H%M"))
        
        if offerStart <= bidStart:
            if offerEnd >= bidEnd:
                overlap_offers.append(offers[i])

        elif offerStart < bidEnd:
            if offerEnd > bidEnd:
                overlap_offers.append(offers[i])

        elif offerStart < bidStart:
            if offerEnd > bidStart:
                overlap_offers.append(offers[i])

        elif offerStart < bidEnd:
            if offerEnd > bidStart:
                overlap_offers.append(offers[i])

    return overlap_offers

# #
def expensive_offer(offers):
    price = 0
    offer = offers[0]
    for i in range(len(offers)):
        if offers[i].cost > price:
            price = offers[i].cost
            offer = offers[i]
    return offer

# #
def run_matcher():

    matcher_output = {'status': -1}

    de_bid = ""
    de_offer = ""
    new_bids = {}
    new_offers = {}
    timeMatch = 0

    bids = list_active_bids()
    offers = list_active_offers()

    if len(offers) > 0 and len(offers) > 0: 
        lowestExpBid = lowest_exp_bids(bids)
        matchingBids = matching_requirements(lowestExpBid, bids)
        clashBids = time_clash(matchingBids)
        [current_bid,s_price] = second_price_auction(clashBids)
        currentOffers = check_offers_price(current_bid,offers)
        if len(currentOffers) > 0 : 
            matchingOffers = check_time_overlap(current_bid,currentOffers)
            current_offer = expensive_offer(matchingOffers)

            while(1):
                if current_offer != []:
                    bidStart = int(current_bid.start_time.strftime("%Y%m%d%H%M"))
                    bidEnd = int(current_bid.end_time.strftime("%Y%m%d%H%M"))
                    offerStart = int(current_offer.start_time.strftime("%Y%m%d%H%M"))
                    offerEnd = int(current_offer.end_time.strftime("%Y%m%d%H%M"))
                    status = 1
                    c_start = current_bid.start_time
                    c_end = current_bid.end_time

                    if bidStart > offerStart:
                    # bid starts later than offer
                    # create new offer in beginning
                        id2 = generate_id()
                        new_offers["before_offer"] = Offers(id2,current_offer.project_id, current_offer.status, current_offer.resource_id, current_offer.start_time, current_bid.start_time, current_offer.expire_time, current_offer.config, current_offer.cost)
                        c_start = current_bid.start_time

                    elif bidStart < offerStart:
                    # bid starts earlier than offer
                    # create new bid in beginning
                        id2 = generate_id()
                        new_bids["before_bid"] = Bids(id2, current_bid.project_id, current_bid.quantity, current_bid.start_time, current_offer.start_time, current_bid.expire_time, current_bid.duration, current_bid.status, current_bid.config_query, current_bid.cost)
                        c_start = current_offer.start_time
                    else:
                        timeMatch = timeMatch+1

                    if bidEnd > offerEnd:
                    # bid ends later than offer
                    # create new bid in end
                        id2 = generate_id()
                        new_bids["after_bid"] = Bids(id2, current_bid.project_id, current_bid.quantity, current_offer.end_time, current_bid.end_time, current_bid.expire_time, current_bid.duration, current_bid.status, current_bid.config_query, current_bid.cost)
                        c_end = current_offer.end_time

                    elif bidEnd < offerEnd:
                    # bid ends earlier than offer
                    # create new offer in end
                        id2 = generate_id()
                        new_bids["after_offer"] = Offers(id2,current_offer.project_id, current_offer.status, current_offer.resource_id, current_bid.end_time, current_offer.end_time, current_offer.expire_time, current_offer.config, current_offer.cost)
                        c_end = current_bid.end_time
                    else:
                        timeMatch = timeMatch + 1

                    cid = generate_id()
                    if timeMatch == 2:
                        c_start = current_bid.start_time
                        c_end = current_bid.end_time
                    if current_offer.cost > s_price:
                        new_contract = Contracts(cid,"matched", c_start, c_end, current_bid.cost)
                    else:
                        new_contract = Contracts(cid,"matched",c_start, c_end, s_price)
                    new_cbo = cbo_relation(cid, current_offer.offer_id, current_bid.bid_id)
                    break
                else:
                    #no offer matches the bid
                    #remove the highest priced bid and go to the next one.
                    if (len(clashBids) == 0):
                        # if there are no more bids that match / fit the same requirements as the lowest expiry bid, move on to the next expiry time
                        idx = bids.index(lowestExpBid)
                        bids.pop(idx)
                        if (len(bids) > 0):
                            lowestExpBid = lowest_exp_bids(bids)
                            matchingBids = matching_requirements(lowestExpBid, bids)
                            clashBids = time_clash(matchingBids)
                            [current_bid,s_price] = second_price_auction(clashBids)
                            currentOffers = check_offers_price(current_bid,offers)
                            matchingOffers = check_time_overlap(current_bid,currentOffers)
                            current_offer = expensive_offer(matchingOffers)
                        else:
                            print("All viable bids and offers have been matched.")
                            status = 0
                            break
                    else:     
                        clashBids.pop(0)
                        [current_bid,s_price] = second_price_auction(clashBids)
                        currentOffers = check_offers_price(current_bid,offers)
                        matchingOffers = check_time_overlap(current_bid,currentOffers)
                        current_offer = expensive_offer(matchingOffers)


                



            de_bid = current_bid.bid_id
            de_offer = current_offer.offer_id



            # for bid in bids:
            #     print(bid.__dict__)
            # print("######")
            # for offer in offers:
            #     print(offer.__dict__)
            # print('#####')
            
            # Output variables
            matcher_output["status"] = status
            matcher_output["bid_deactivate"] = de_bid
            matcher_output["offer_deactivate"] = de_offer
            matcher_output["new_bids"] = new_bids
            matcher_output["new_offers"] = new_offers
            matcher_output["new_contract"] = new_contract    
            matcher_output["new_cbo"] = new_cbo

    return matcher_output
## END AUCTION.PY ##

def handle_matcher():
    status = 1
    while(status == 1):
        matcher_output = run_matcher()

        status = matcher_output["status"]

        if (status == 1):

            db.session.add(matcher_output["new_contract"])
            db.session.commit()

            db.session.add(matcher_output["new_cbo"])
            db.session.commit()



            ### ACCT SERVICE POST REQUEST

            contract_approved = True

            if (contract_approved):
                if "before_bid" in matcher_output["new_bids"]:
                    db.session.add(matcher_output["new_bids"]["before_bid"])
                    db.session.commit()
                if "after_bid" in matcher_output["new_bids"]:
                    db.session.add(matcher_output["new_bids"]["after_bid"])
                    db.session.commit()
                if "before_offer" in matcher_output["new_offers"]:
                    db.session.add(matcher_output["new_offers"]["before_offer"])
                    db.session.commit()
                if "after_offer" in matcher_output["new_offers"]:
                    db.session.add(matcher_output["new_offers"]["after_offer"])
                    db.session.commit()

                bid_de = Bids.query.filter_by(bid_id=matcher_output["bid_deactivate"]).first()
                bid_de.status = statuses.MATCHED
                db.session.commit()

                offer_de = Offers.query.filter_by(offer_id=matcher_output["offer_deactivate"]).first()
                offer_de.status = statuses.MATCHED
                db.session.commit()


    return



#@app.route('/insert', methods=['GET'])
#def insert():
#    b = Bid("0165c7d6-4e3d-4165-9c93-d423275a76bf", 10240, "x86_64", 4, 16, 3, 10, datetime(2020, 5, 2, 20, 00),
#            datetime(2020, 5, 2, 22, 00), datetime(2020, 5, 1, 10, 00))
#    o = Offer("08d727a9-485a-4bf8-82e0-ee5f724e2020", 10240, "x86_64", 4, 16, 3, 20, datetime(2020, 5, 2, 10, 00),
#              datetime(2020, 5, 2, 12, 00), datetime(2020, 5, 1, 8, 00))
#    c = Contract(o, b, 10, datetime(2020, 5, 2, 20, 00), datetime(2020, 5, 2, 22, 00))
#    contracts = [c]
#    insert_contract(contracts)
#    return jsonify("inserted contract")


@app.route('/force_matcher', methods=['GET'])
def force_matcher():
    handle_matcher()
    return jsonify("matcher run")


@app.route('/update_status', methods=['GET'])
def update_status():
    pass

def loop_matcher(delay):
    while(True):
        print('Matcher Automatically Run')
        handle_matcher()
        #do expired status update here
        time.sleep(delay)
        

# Run Server
if __name__ == "__main__":
   matcher_delay = 3600 # 1 hour in seconds
   p = Process(target=loop_matcher, args=(matcher_delay,))
   p.start()  
   app.run(host='0.0.0.0', debug=True, use_reloader=False)
   p.join()

