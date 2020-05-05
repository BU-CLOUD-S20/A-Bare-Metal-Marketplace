import uuid
from datetime import datetime
from datetime import timedelta
from hashlib import blake2s
import database_setup.APIs.marketAPI as MarketAPI
import database_setup.statuses as statuses
import random

now = datetime.now()
current_time = now.strftime("%Y%m%d%H%M")


class Bids():
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

class Offers:
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


class Contracts:
    def __init__(self, contract_id, status, start_time, end_time, cost):
        self.start_time = start_time
        self.end_time = end_time
        self.contractID = contract_id
        self.cost = cost
        self.status = status

class cbo_relation:
    def __init__(self, contract_id, offer_id, bid_id):
        self.bid_id = bid_id
        self.offer_id = offer_id
        self.contract_id = contract_id

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
    for i in range(len(offers)):
        if offers[i].cost > price:
            price = offers[i].cost
            offer = offers[i]
    return offer



def list_offers():
    # result = []
    db_result = MarketAPI.offer_select_all_available()
    # for db_offer in db_result:
    #     config = db_offer.config
    #     result.append(Offers(db_offer.offer_id, config.get('memory_gb'), config.get('cpu_arch'),
    #                         config.get('cpu_physical_count'), config.get('cpu_core_count'), config.get('cpu_ghz'),
    #                         db_offer.cost, db_offer.start_time, db_offer.end_time, db_offer.expire_time))
    return db_result


def list_bids():
    # result = []
    db_result = MarketAPI.bid_select_all_available()
    # for db_bid in db_result:
    #     config = db_bid.config_query
    #     result.append(Bid(db_bid.bid_id, config.get('memory_gb'), config.get('cpu_arch'),
    #                       config.get('cpu_physical_count'), config.get('cpu_core_count'), config.get('cpu_ghz'),
    #                       db_bid.cost, db_bid.start_time, db_bid.end_time, db_bid.expire_time))
    return db_result
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
            c_start = current_bid.start_time
            bidStart = int(current_bid.start_time.strftime("%Y%m%d%H%M"))
            bidEnd = int(current_bid.end_time.strftime("%Y%m%d%H%M"))
            offerStart = int(current_offer.start_time.strftime("%Y%m%d%H%M"))
            offerEnd = int(current_offer.end_time.strftime("%Y%m%d%H%M"))
            status = 1
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
                new_offers["after_offer"] = Offers(id2,current_offer.project_id, current_offer.status, current_offer.resource_id, current_bid.end_time, current_offer.end_time, current_offer.expire_time, current_offer.config, current_offer.cost)
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
            print(new_cbo.contract_id)
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


def generate_id():
    return ''.join(random.choice('0123456789abcdef') for i in range(36))
# def add_contract(contracts):
#     for contract in contracts:
#         contract_value = {'contract_id': contract.contractID, 'status': statuses.AVAILABLE,
#                           'start_time': contract.start_time, 'end_time': contract.end_time,
#                           'cost': contract.cost}
#         MarketAPI.contract_insert(contract_value)
#         MarketAPI.relation_insert(contract.contractID, contract.offerID, contract.bidID)
#         MarketAPI.bid_update_status_by_id(contract.bidID, statuses.MATCHED)
#         MarketAPI.offer_update_status_by_id(contract.offerID, statuses.MATCHED)



# def Bare_Metal_Auction(bids, offers): 
#     i = 0
#     contracts = []
#     while i < 5:
#         lowestExpBid = lowest_exp_bids(bids)
#         matchingBids = matching_requirements(lowestExpBid, bids)
#         clashBids = time_clash(matchingBids)
#         [current_bid,s_price] = second_price_auction(clashBids)
#         currentOffers = check_offers_price(current_bid[0],offers)
#         matchingOffers = check_time_overlap(current_bid[0],currentOffers)
#         current_offer = expensive_offer(matchingOffers)
#         if current_offer.cost > current_bid[1]:
#             current_contract = create_contract(current_bid[0], current_offer,current_bid[0].cost)
#         else:
#             current_contract = create_contract(current_bid[0], current_offer, current_bid[1])
#         contracts.append(current_contract)
#         i = i +1
#         print(current_bid[0].bidID, current_offer.offerID)


# def create_contract(bid, offer, price):
#     new_contract = Contract(bid, offer)
#     if bid.start_time == offer.start_time:
#         if bid.end_time == offer.end_time:
#             new_contract = Contract(bid, offer, price, bid.start_time, bid.end_time)

#     elif bid.start_time < offer.start_time:
#         if bid.end_time > offer.end_time:
#             new_contract = Contract(bid, offer, price, offer.start_time, offer.end_time)
#             #create bids from start time of bid to start time of offer and
#             #end time of offer to end time of bid
#     elif bid.start_time < offer.start_time:
#         if bid.end_time <= offer.end_time:
#             new_contract = Contract(bid, offer, price, offer.start_time, bid.end_time)
#             #create bid from start time of bid to start time of offer and
#             #create offer from end time of bid to to end time of offer

#     elif bid.start_time >= offer.start_time:
#         if bid.end_time > offer.end_time:
#             new_contract = Contract(bid, offer, price, bid.start_time, offer.end_time)
#             #create bid from end time of offer to end time of bid and
#             #create offer from start time of offer to start time of bid

#     elif bid.start_time > offer.start_time:
#         if bid.end_time < offer.end_time:
#             new_contract = Contract(bid, offer, price, bid.start_time, bid.end_time)
#             # create offers from end time of bid to end time of offer and
#             #from start time of offer to start time of bid
#     return new_contract