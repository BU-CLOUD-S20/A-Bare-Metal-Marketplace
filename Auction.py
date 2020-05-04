import uuid
from datetime import datetime
from hashlib import blake2s
import database_setup.APIs.marketAPI as MarketAPI
import database_setup.statuses as statuses
import random

now = datetime.now()
current_time = now.strftime("%Y%m%d%H%M")


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
        self.contractID = "abcd3"
        # self.allocation_time = Offer.allocation_time
        self.cost = cost


def lowest_exp_bids(bids):
    exp = bids[0].expiry_time
    for i in range(len(bids)):
        if bids[i].expiry_time < exp:
            exp = bids[i].expiry_time
            current_bid = bids[i]
    return current_bid


def matching_requirements(current_bid, bids):
    current_bids = [current_bid]
    for i in range(len(bids)):
        if current_bid.bidID != bids[i].bidID:
            if current_bid.requirements == bids[i].requirements:
                current_bids.append(bids[i])
    return current_bids


def time_clash(bids):
    clash_bids = [bids[0]]
    start_time = bids[0].start_time
    end_time = bids[0].end_time
    for i in range(len(bids)):
        if bids[i].start_time >= start_time:
            if bids[i].start_time <= end_time:
                clash_bids.append(bids[i])
    return clash_bids


def second_price_auction(bids):
    high_price = bids[0].cost
    second_price = 0
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


def check_offers_price(bid, offers):
    cheap_offers = []
    for i in range(len(offers)):
        if offers[i].cost <= bid.cost:
            cheap_offers.append(offers[i])
    return cheap_offers


def check_time_overlap(bid, offers):
    overlap_offers = []
    for i in range(len(offers)):
        if offers[i].start_time <= bid.start_time:
            if offers[i].end_time >= bid.end_time:
                overlap_offers.append(offers[i])

        elif offers[i].start_time < bid.end_time:
            if offers[i].end_time > bid.end_time:
                overlap_offers.append(offers[i])

        elif offers[i].start_time < bid.start_time:
            if offers[i].end_time > bid.start_time:
                overlap_offers.append(offers[i])

        elif offers[i].start_time < bid.end_time:
            if offers[i].end_time > bid.start_time:
                overlap_offers.append(offers[i])

    return overlap_offers


def expensive_offer(offers):
    price = 0
    for i in range(len(offers)):
        if offers[i].cost > price:
            price = offers[i].cost
            offer = offers[i]
    return offer


def create_contract(bid, offer, price):
    new_contract = Contract(bid, offer)
    if bid.start_time == offer.start_time:
        if bid.end_time == offer.end_time:
            new_contract = Contract(bid, offer, price, bid.start_time, bid.end_time)

    elif bid.start_time < offer.start_time:
        if bid.end_time > offer.end_time:
            new_contract = Contract(bid, offer, price, offer.start_time, offer.end_time)
            #create bids from start time of bid to start time of offer and
            #end time of offer to end time of bid
    elif bid.start_time < offer.start_time:
        if bid.end_time <= offer.end_time:
            new_contract = Contract(bid, offer, price, offer.start_time, bid.end_time)
            #create bid from start time of bid to start time of offer and
            #create offer from end time of bid to to end time of offer

    elif bid.start_time >= offer.start_time:
        if bid.end_time > offer.end_time:
            new_contract = Contract(bid, offer, price, bid.start_time, offer.end_time)
            #create bid from end time of offer to end time of bid and
            #create offer from start time of offer to start time of bid

    elif bid.start_time > offer.start_time:
        if bid.end_time < offer.end_time:
            new_contract = Contract(bid, offer, price, bid.start_time, bid.end_time)
            # create offers from end time of bid to end time of offer and
            #from start time of offer to start time of bid
    return new_contract

def Bare_Metal_Auction(bids, offers): 
    i = 0
    contracts = []
    while i < 5:
        lowestExpBid = lowest_exp_bids(bids)
        matchingBids = matching_requirements(lowestExpBid, bids)
        clashBids = time_clash(matchingBids)
        current_bid = second_price_auction(clashBids)

        currentOffers = check_offers_price(current_bid[0],offers)
        matchingOffers = check_time_overlap(current_bid[0],currentOffers)
        current_offer = expensive_offer(matchingOffers)
        if current_offer.cost > current_bid[1]:
            current_contract = create_contract(current_bid[0], current_offer,current_bid[0].cost)
        else:
            current_contract = create_contract(current_bid[0], current_offer, current_bid[1])
        contracts.append(current_contract)
        i = i +1
        print(current_bid[0].bidID, current_offer.offerID)

def list_bids():
    result = []
    db_result = MarketAPI.bid_select_all_available()
    for db_bid in db_result:
        config = db_bid.config_query
        result.append(Bid(db_bid.bid_id, config.get('memory_gb'), config.get('cpu_arch'),
                          config.get('cpu_physical_count'), config.get('cpu_core_count'), config.get('cpu_ghz'),
                          db_bid.cost, db_bid.start_time, db_bid.end_time, db_bid.expire_time))
    return result


def list_offers():
    result = []
    db_result = MarketAPI.offer_select_all_available()
    for db_offer in db_result:
        config = db_offer.config
        result.append(Offer(db_offer.offer_id, config.get('memory_gb'), config.get('cpu_arch'),
                            config.get('cpu_physical_count'), config.get('cpu_core_count'), config.get('cpu_ghz'),
                            db_offer.cost, db_offer.start_time, db_offer.end_time, db_offer.expire_time))
    return result


def add_contract(contracts):
    for contract in contracts:
        contract_value = {'contract_id': contract.contractID, 'status': statuses.AVAILABLE,
                          'start_time': contract.start_time, 'end_time': contract.end_time,
                          'cost': contract.cost}
        MarketAPI.contract_insert(contract_value)
        MarketAPI.relation_insert(contract.contractID, contract.offerID, contract.bidID)
        MarketAPI.bid_update_status_by_id(contract.bidID, statuses.MATCHED)
        MarketAPI.offer_update_status_by_id(contract.offerID, statuses.MATCHED)


def generate_id():
    return ''.join(random.choice('0123456789abcdef') for i in range(36))

if __name__ == "__main__":
    status = 0
    de_bid = ""
    de_offer = ""
    cr_bid = {}
    cr_offer = {}
    bids = list_bids()
    offers = list_offers()
    #Bare_Metal_Auction(bids,offers)
    for bid in bids:
        print(bid.__dict__)
    print("######")
    for offer in offers:
        print(offer.__dict__)
    print('#####')
    
    de_bid = Bid("0165c7d6-4e3d-4165-9c93-d423275a76bf", 10240, "x86_64", 4, 16, 3, 10, datetime(2020, 5, 2, 20, 00),
            datetime(2020, 5, 2, 22, 00), datetime(2020, 5, 1, 10, 00))
    de_offer = Offer("08d727a9-485a-4bf8-82e0-ee5f724e2020", 10240, "x86_64", 4, 16, 3, 20, datetime(2020, 5, 2, 10, 00),
              datetime(2020, 5, 2, 12, 00), datetime(2020, 5, 1, 8, 00))
    cr_contract = Contract(de_offer, de_bid, 10, datetime(2020, 5, 2, 20, 00), datetime(2020, 5, 2, 22, 00))
    #contracts = [c]
    #add_contract(contracts)
    #print("added contract")

    # Output variables
    matcher_output = {}
    matcher_output["status"] = status
    matcher_output["bid_deactivate"] = de_bid
    matcher_output["offer_deactivate"] = de_offer
    matcher_output["new_bids"] = cr_bid
    matcher_output["new_offers"] = cr_offer
    matcher_output["new_contract"] = cr_contract    


