from datetime import datetime

now = datetime.now()
# print(now)
current_time = now.strftime("%Y%m%d%H%M")


# print(current_time)


class Bid:
    def __init__(self, id1, memory, cpu_arch, cpu_physical_count, cpu_core_count, cpu_ghz, cost, start_time, end_time):
        self.bidID = id1
        self.requirements = [memory, cpu_arch, cpu_physical_count, cpu_core_count, cpu_ghz]
        self.cost = cost
        self.start_time = int(start_time.strftime("%Y%m%d%H%M"))
        self.end_time = int(end_time.strftime("%Y%m%d%H%M"))
        self.expiry = self.start_time - int(current_time)


class Offer:
    def __init__(self, id1, memory, cpu_arch, cpu_physical_count, cpu_core_count, cpu_ghz, cost, start_time, end_time):
        self.offerID = id1
        self.requirements = [memory, cpu_arch, cpu_physical_count, cpu_core_count, cpu_ghz]
        self.cost = cost
        self.start_time = int(start_time.strftime("%Y%m%d%H%M"))
        self.end_time = int(end_time.strftime("%Y%m%d%H%M"))
        self.expiry = self.start_time - int(current_time)


if __name__ == "__main__":
    d1 = datetime(2020, 7, 14, 10, 30)
    e1 = datetime(2020, 7, 14, 22, 30)
    bid1 = Bid("bid1", 10240, "x86_64", 4, 16, 3, 10, d1, e1)
    # print(bid1.start_time,bid1.end_time,bid1.expiry)
    d2 = datetime(2020, 7, 14, 10, 30)
    e2 = datetime(2020, 7, 14, 22, 30)
    bid2 = Bid("bid2", 10240, "x86_64", 4, 16, 3, 20, d2, e2)
    d3 = datetime(2020, 7, 14, 10, 30)
    e3 = datetime(2020, 7, 14, 22, 30)
    bid3 = Bid("bid3", 10240, "x86_64", 4, 16, 3, 15, d3, e3)
    d4 = datetime(2020, 7, 14, 10, 30)
    e4 = datetime(2020, 7, 14, 22, 30)
    bid4 = Bid("bid4", 10240, "x86_64", 4, 16, 3, 12, d4, e4)
    d5 = datetime(2020, 7, 14, 10, 30)
    e5 = datetime(2020, 7, 14, 22, 30)
    bid5 = Bid("bid5", 10240, "x86_64", 4, 16, 3, 15, d4, e4)
    d6 = datetime(2020, 7, 14, 10, 30)
    e6 = datetime(2020, 7, 14, 22, 30)
    bid6 = Bid("bid6", 10240, "x86_64", 4, 16, 3, 17, d4, e4)
    d7 = datetime(2020, 7, 14, 10, 30)
    e7 = datetime(2020, 7, 14, 22, 30)
    bid7 = Bid("bid7", 10240, "x86_64", 4, 16, 3, 19, d4, e4)
    d8 = datetime(2020, 7, 14, 10, 30)
    e8 = datetime(2020, 7, 14, 22, 30)
    bid8 = Bid("bid8", 10240, "x86_64", 4, 16, 3, 12, d4, e4)
    d9 = datetime(2020, 7, 14, 10, 30)
    e9 = datetime(2020, 7, 14, 22, 30)
    bid9 = Bid("bid9", 10240, "x86_64", 4, 16, 3, 15, d4, e4)
    d10 = datetime(2020, 7, 14, 10, 30)
    e10 = datetime(2020, 7, 14, 22, 30)
    bid10 = Bid("bid10", 10240, "x86_64", 4, 16, 3, 17, d4, e4)
    d11 = datetime(2020, 7, 14, 10, 30)
    e11 = datetime(2020, 7, 14, 22, 30)
    bid11 = Bid("bid11", 10240, "x86_64", 4, 16, 3, 9, d4, e4)

    bids = [bid1, bid2, bid3, bid4, bid5, bid6, bid7, bid8, bid9, bid10, bid11]

    offer1 = Offer("offer1", 10240, "x86_64", 4, 16, 3, 5, d4, e4)
    offer2 = Offer("offer2", 10240, "x86_64", 4, 16, 3, 2, d4, e4)
    offer3 = Offer("offer3", 10240, "x86_64", 4, 16, 3, 4, d4, e4)
    offer4 = Offer("offer4", 10240, "x86_64", 4, 16, 3, 5, d4, e4)
    offer5 = Offer("offer5", 10240, "x86_64", 4, 16, 3, 7, d4, e4)
    offer6 = Offer("offer6", 10240, "x86_64", 4, 16, 3, 20, d4, e4)
    offer7 = Offer("offer7", 10240, "x86_64", 4, 16, 3, 1, d4, e4)
    offer8 = Offer("offer8", 10240, "x86_64", 4, 16, 3, 6, d4, e4)

    offers = [offer1, offer2, offer3, offer4, offer5, offer6, offer7, offer8]

    while ((len(bids)) > 0 and (len(offers)) > 0):
        current = [1000000000000000, 0]
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
                    bestBidIndex = i
        for j in range(len(offers)):
            ExpensiveOffer = 0
            if ((offers[j].requirements == bestBid.requirements) and (offers[j].cost <= price)):
                if (offers[j].cost > ExpensiveOffer):
                    ExpensiveOffer = offers[j].cost
                    OfferIndex = j
        print(bestBid.bidID, end=" ")
        print(offers[OfferIndex].offerID, end=" ")
        print(ExpensiveOffer)
        bids.remove(bids[bestBidIndex])
        offers.remove(offers[j])
