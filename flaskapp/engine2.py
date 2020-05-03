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


def get_bids():
    result = []
    db_result = MarketAPI.bid_select_all()
    for db_bid in db_result:
        config = db_bid.config_query
        result.append(Bid(db_bid.bid_id, config.get('memory_gb'), config.get('cpu_arch'),
                          config.get('cpu_physical_count'), config.get('cpu_core_count'), config.get('cpu_ghz'),
                          db_bid.cost, db_bid.start_time, db_bid.end_time))
    return result


def get_offers():
    result = []
    db_result = MarketAPI.offer_select_all()
    for db_offer in db_result:
        config = db_offer.config
        result.append(Offer(db_offer.offer_id, config.get('memory_gb'), config.get('cpu_arch'),
                            config.get('cpu_physical_count'), config.get('cpu_core_count'), config.get('cpu_ghz'),
                            db_offer.cost, db_offer.start_time, db_offer.end_time))
    return result



if __name__ == "__main__":

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