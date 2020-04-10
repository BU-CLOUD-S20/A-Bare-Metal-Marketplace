from random import randint

class Bid:
    def __init__(self,id1, memory, cpu_arch, cpu_physical_count, cpu_core_count, cpu_ghz, cost, expiry_time):
        self.bidID = id1
        self.requirements = [memory, cpu_arch, cpu_physical_count, cpu_core_count, cpu_ghz]
        self.cost = cost
        self.expiry = expiry_time
class Offer:
    def __init__(self,id1, memory, cpu_arch, cpu_physical_count, cpu_core_count, cpu_ghz, cost):
        self.offerID = id1
        self.requirements = [memory, cpu_arch, cpu_physical_count, cpu_core_count, cpu_ghz]
        self.cost = cost

class Contract:
    def __init__(self, Offer, Bid, cost, ID):
        self.bidID = Bid.bidID
        self.offerID = Offer.offerID
        self.cost = cost
        self.ID = ID

if __name__ == "__main__":
    bids = []
    offers = []
    for c in range(10):
        bids.append(Bid(c,10240,"x86_64",4,16,3,randint(1,10),randint(1,15)))
        offers.append(Offer(c,10240,"x86_64",4,16,3,randint(8,20)))
    contracts = []
    b = 0
    for d in range(10):
        current = [1000000000000000,0]
        lastPrice = bids[0].cost
        price = bids[0].cost
        for i in range(len(bids)):
            if (bids[i].expiry < current[0]):
                current = [bids[i].expiry, i]
        check1 = 0
        check2 = 0
        for i in range(len(bids)):
            if (bids[i].requirements == bids[current[1]].requirements):
                if bids[i].cost > price:
                    lastPrice = price
                    price = bids[i].cost
                    bestBid = bids[i]
                    bestBidIndex = i
                    check1 = 1
        for j in range(len(offers)):
            ExpensiveOffer = 0
            if ((offers[j].requirements == bestBid.requirements) and (offers[j].cost <= price)):
                if (offers[j].cost > ExpensiveOffer):
                    ExpensiveOffer = offers[j].cost
                    OfferIndex = j
                    check2 = 1
        if ((check1 == 1) and (check2 == 1)):
            contract = Contract(offers[OfferIndex],bestBid,lastPrice,b)
            b+=1
            contracts.append(contract)
            print(len(bids))
            print(bestBidIndex)
            bids.remove(bids[bestBidIndex])
            offers.remove(offers[OfferIndex])
            temp = len(contracts)-1
        for a in range(len(contracts)):
            print("Contract number ", end = '')
            print(contracts[a].ID, end = '')
            print(" matched up ", end = '')
            print(contracts[a].bidID, end = '')
            print(" with ", end = '')
            print(contracts[a].offerID, end = '')
            print(" at a price of ", end = '')
            print(contracts[a].cost)


