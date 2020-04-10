from _ctypes import sizeof


class Requirements:
    def __init__(self):
        pass
    pass


class Bid:
    def __init__(self, id, requirements, allocation_time, expiry_time, cost ):
        self.id = id
        self.requirements = requirements
        self.allocation_time = allocation_time
        self.expiry_time = expiry_time
        self.cost = cost

class Offer:
    def __init__(self, id, requirements, allocation_time, expiry_time, cost):
        self.id = id
        self.requirements = requirements
        self.allocation_time = allocation_time
        self.expiry_time = expiry_time
        self.cost = cost

class Contract:
    def __init__(self, Offer, Bid, cost):
        self.bid_id = Bid.id
        self.offer_id =  Offer.id
        #figure out how to make a non-repeating contract id self.id =
        self.allocation_time = Offer.allocation_time
        self.cost = cost
        
class Engine:
    def __init__(self, bids , offers , ):
        self.bids = bids
        self.offers = offers

    bids = Bid(123,456,700,5,1)

    def get_bid(self, bids):
        list_bids = ''
        # bids is the list of bids from database
        lowest_expiry_time = bids[0].expiry_time
        for i in range (sizeof(bids)):
            if bids[i].expiry_time < lowest_expiry_time:
                lowest_expiry_time = bids[i].expiry_time
                current_bid = bids[i]
        list_bids.append(current_bid)
        for i in range (sizeof(bids)):
            if (bids[i].requirements == current_bid.requiremnts):
                list_bids.append(bids[i])
        for i in range (sizeof(list_bids)):
            if list_bids[i].cost > current_bid.cost:
                current_bid = list_bids[i]
                current_bid.cost = current_bid.cost + 0.01
        return current_bid


    def get_offer(self, offers , current_bid):
        list_offers = ''
        for i in range(sizeof(offers)):
            if offers[i].requirements == current_bid.requiremnts & offers[i].cost < current_bid.cost:
                list_offers.append(offers[i])
        highest_price = list_offers[0].cost
        current_offer = list_offers[0]
        for i in range(sizeof(list_offers)):
            if list_offers[i].cost > highest_price:
                highest_price = list_offers[i].cost
                current_offer = list_offers[i]
        return current_offer
    def create_contract(self, current_offer, current_bid):
        contract = Contract(current_offer,current_bid, current_bid.cost)
        return contract



if  __name__ == "__main__":
    x =  Engine.get_bid()