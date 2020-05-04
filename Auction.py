import uuid
from datetime import datetime
from datetime import timedelta
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
        self.start_format = start_time
        self.start_time = int(start_time.strftime("%Y%m%d%H%M"))
        self.end_time = int(end_time.strftime("%Y%m%d%H%M"))
        self.end_format = end_time
        self.expiry_time = int(expiry_time.strftime("%Y%m%d%H%M")) - int(current_time)
        self.expiry_format = expiry_time

class Offer:
    def __init__(self, id1, memory, cpu_arch, cpu_physical_count, cpu_core_count, cpu_ghz, cost, start_time, end_time,
                 expiry_time):
        self.offerID = id1
        self.requirements = [memory, cpu_arch, cpu_physical_count, cpu_core_count, cpu_ghz]
        self.cost = cost
        self.start_time = int(start_time.strftime("%Y%m%d%H%M"))
        self.end_time = int(end_time.strftime("%Y%m%d%H%M"))
        self.expiry_time = int(expiry_time.strftime("%Y%m%d%H%M")) - int(current_time)
        self.start_format = start_time
        self.end_format = end_time
        self.expiry_format = expiry_time


class Contracts:
    def __init__(self, contract_id, status, start_time, end_time, cost):
        self.start_time = start_time
        self.end_time = end_time
        self.contractID = contract_id
        self.cost = cost
        self.status = status

class cbo_relation:
    def __init__(self, contract_id, offer_id, bid_id):
        self.bidID = bid_id
        self.offerID = offer_id
        self.contractID = contract_id

# #
def lowest_exp_bids(bids):
    exp = bids[0].expiry_time
    for i in range(len(bids)):
        if bids[i].expiry_time < exp:
            exp = bids[i].expiry_time
            current_bid = bids[i]
    return current_bid

# #
def matching_requirements(current_bid, bids):
    current_bids = [current_bid]
    for i in range(len(bids)):
        if current_bid.bidID != bids[i].bidID:
            if current_bid.requirements == bids[i].requirements:
                current_bids.append(bids[i])
    return current_bids

# #
def time_clash(bids):
    clash_bids = [bids[0]]
    start_time = bids[0].start_time
    end_time = bids[0].end_time
    for i in range(len(bids)):
        if bids[i].start_time >= start_time:
            if bids[i].start_time <= end_time:
                clash_bids.append(bids[i])
    return clash_bids

# #
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

# #
def check_offers_price(bid, offers):
    cheap_offers = []
    for i in range(len(offers)):
        if offers[i].cost <= bid.cost:
            cheap_offers.append(offers[i])
    return cheap_offers

# #
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

# #
def expensive_offer(offers):
    price = 0
    for i in range(len(offers)):
        if offers[i].cost > price:
            price = offers[i].cost
            offer = offers[i]
    return offer

# #
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
        [current_bid,s_price] = second_price_auction(clashBids)
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

# #
def main():
    de_bid = ""
    de_offer = ""
    new_bids = {}
    new_offers = {}
    timeMatch = 0


    bids = list_bids()
    offers = list_offers()


    lowestExpBid = lowest_exp_bids(bids)
    matchingBids = matching_requirements(lowestExpBid, bids)
    clashBids = time_clash(matchingBids)
    [current_bid,s_price] = second_price_auction(clashBids)
    currentOffers = check_offers_price(current_bid,offers)
    matchingOffers = check_time_overlap(current_bid,currentOffers)
    current_offer = expensive_offer(matchingOffers)

    while(1):
        if current_offer != []:
            status = 1
            if current_bid.start_time > current_offer.start_time:
            # bid starts later than offer
            # create new offer in beginning
                id2 = generate_id()
                reqs = current_offer.requirements
                new_offers["before_offer"] = Offer(id2, reqs[0], reqs[1], reqs[2], reqs[3], reqs[4], current_offer.cost, current_offer.start_format, current_bid.start_format, current_offer.expiry_format)
                c_start = current_bid.start_format

            elif current_bid.start_time < current_offer.start_time:
            # bid starts earlier than offer
            # create new bid in beginning
                id2 = generate_id()
                reqs = current_bid.requirements
                new_bids["before_bid"] = Bid(id2, reqs[0], reqs[1], reqs[2], reqs[3], reqs[4], current_bid.cost, current_bid.start_format, current_offer.start_format, current_bid.expiry_format)
                c_start = current_offer.start_format
            else:
                timeMatch = timeMatch+1

            if current_bid.end_time > current_offer.end_time:
            # bid ends later than offer
            # create new bid in end
                id2 = generate_id()
                reqs = current_bid.requirements
                new_bids["after_bid"] = Bid(id2, reqs[0], reqs[1], reqs[2], reqs[3], reqs[4], current_bid.cost, current_offer.end_format, current_bid.end_format, current_bid.expiry_format)
                c_end = current_offer.end_format

            elif current_bid.end_time < current_offer.end_time:
            # bid ends earlier than offer
            # create new offer in end
                id2 = generate_id()
                reqs = current_offer.requirements
                new_bids["after_offer"] = Offer(id2, reqs[0], reqs[1], reqs[2], reqs[3], reqs[4], current_offer.cost, current_bid.end_format, current_offer.end_format, current_offer.expiry_format)
                c_end = current_bid.end_format
            else:
                timeMatch = timeMatch + 1

            cid = generate_id()
            if timeMatch == 2:
                c_start = current_bid.start_format
                c_end = current_bid.end_format
            if current_offer.cost > s_price:
                new_contract = Contracts(cid,"matched", c_start, c_end, current_bid.cost)
            else:
                new_contract = Contracts(cid,"matched",c_start, c_end, s_price)
            new_cbo = cbo_relation(cid, current_offer.offerID, current_bid.bidID)
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


        



    de_bid = current_bid.bidID
    de_offer = current_offer.offerID



    # for bid in bids:
    #     print(bid.__dict__)
    # print("######")
    # for offer in offers:
    #     print(offer.__dict__)
    # print('#####')
    
    # Output variables
    matcher_output = {}
    matcher_output["status"] = status
    matcher_output["bid_deactivate"] = de_bid
    matcher_output["offer_deactivate"] = de_offer
    matcher_output["new_bids"] = new_bids
    matcher_output["new_offers"] = new_offers
    matcher_output["new_contract"] = new_contract    
    matcher_output["new_cbo"] = new_cbo
    return matcher_output


if __name__ == "__main__":
    matcher_output = main()