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


if __name__ == "__main__":
    bid1 = Bid(1,10240,"x86_64", 4, 16, 3, 10, 5)
    bid2 = Bid(2,10240,"x86_64", 4, 16, 3, 20, 6)
    bid3 = Bid(3,10240,"x86_64", 4, 16, 3, 15, 15)
    bid4 = Bid(4,10240,"x86_64", 4, 16, 3, 12, 2)
    bid5 = Bid(5,10240,"x86_64", 4, 16, 3, 15, 10)
    bid6 = Bid(6,10240,"x86_64", 4, 16, 3, 17, 4)
    bid7 = Bid(7,10240,"x86_64", 4, 16, 3, 19, 3)
    bid8 = Bid(8,10240,"x86_64", 4, 16, 3, 12, 6)
    bid9 = Bid(9,10240,"x86_64", 4, 16, 3, 15, 9)
    bid10 = Bid(10,10240,"x86_64", 4, 16, 3, 17, 11)
    bid11 = Bid(11,10240,"x86_64", 4, 16, 3, 9, 13)

    bids = [bid1, bid2, bid3, bid4, bid5, bid6, bid7, bid8, bid9, bid10, bid11]

    offer1 = Offer(1,10240,"x86_64", 4, 16, 3, 3)
    offer2 = Offer(1,10240,"x86_64", 4, 16, 3, 2)
    offer3 = Offer(1,10240,"x86_64", 4, 16, 3, 4)
    offer4 = Offer(1,10240,"x86_64", 4, 16, 3, 5)
    offer5 = Offer(1,10240,"x86_64", 4, 16, 3, 7)
    offer6 = Offer(1,10240,"x86_64", 4, 16, 3, 20)
    offer7 = Offer(1,10240,"x86_64", 4, 16, 3, 1)
    offer8 = Offer(1,10240,"x86_64", 4, 16, 3, 6)

    offers = [offer1, offer2, offer3, offer4, offer5, offer6, offer7, offer8]

    print(bid1.bidID)
    print(bid1.cost)


    # while(len(bids>0) and len(offers>0)):
    current = [1000000000000000,0]
    lastPrice = bids[0].cost
    price = bids[0].cost
    for i in range(len(bids)):
        if (bids[i].expiry < current[0]):
            current = [bids[i].expiry, i]
    for i in range(len(bids)):
        if (bids[i].requirements == bids[current[1]].requirements):
            if bids[i].cost > price:
                lastPrice = price
                price = bids[i].cost
                bestBid = bids[i]
    for j in range(len(offers)):
        ExpensiveOffer = 0
        if ((offers[j].requirements == bestBid.requirements) and (offers[j].cost <= price)):
            if (offers[j].cost > ExpensiveOffer):
                ExpensiveOffer = offers[j].cost
                OfferIndex = j
    print(bestBid.bidID)
    print(OfferIndex)



