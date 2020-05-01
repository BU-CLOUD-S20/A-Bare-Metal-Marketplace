from datetime import datetime

now = datetime.now()
# print(now)
current_time = now.strftime("%Y%m%d%H%M")


# print(current_time)


class Bid:
    def __init__(self, id1, memory, cpu_arch, cpu_physical_count, cpu_core_count, cpu_ghz, cost, start_time, end_time,
                 expiry_time):
        self.bidID = id1
        self.requirements = [memory, cpu_arch, cpu_physical_count, cpu_core_count, cpu_ghz]
        self.cost = cost
        self.start_time = int(start_time.strftime("%Y%m%d%H%M"))
        self.end_time = int(end_time.strftime("%Y%m%d%H%M"))
        self.expiry = int(expiry_time.strftime("%Y%m%d%H%M")) - int(current_time)


class Offer:
    def __init__(self, id1, memory, cpu_arch, cpu_physical_count, cpu_core_count, cpu_ghz, cost, start_time, end_time,
                 expiry_time):
        self.offerID = id1
        self.requirements = [memory, cpu_arch, cpu_physical_count, cpu_core_count, cpu_ghz]
        self.cost = cost
        self.start_time = int(start_time.strftime("%Y%m%d%H%M"))
        self.end_time = int(end_time.strftime("%Y%m%d%H%M"))
        self.expiry = int(expiry_time.strftime("%Y%m%d%H%M")) - int(current_time)





def lowest_exp_bids(bids):
    exp = bids[0].expiry_time
    for i in range(len(bids)):
        if bids[i].expiry_time < exp:
            exp = bids[i].expiry_time
            current_bid = bids[i]
    return [current_bid]


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
            print(second_price,high_price)
            high_price = expensiveBid.cost
        elif second_price <bids[i].cost:
            second_price = bids[i].cost
    if second_price == high_price:
        second_price = 0
        for i in range(len(bids)):
            if bids[i].cost < high_price:
                if bids[i].cost > second_price:
                    second_price = bids[i].cost

    return expensiveBid.bidID, second_price+0.01


if __name__ == "__main__":
    d1 = datetime(2020, 5, 2, 8, 00)
    e1 = datetime(2020, 5, 2, 12, 00)
    exp1 = datetime(2020, 5, 1, 1, 00)
    bid1 = Bid("bid1", 10240, "x86_64", 4, 16, 3, 20, d1, e1, exp1)
    print(bid1.start_time, bid1.end_time, bid1.expiry)
    d2 = datetime(2020, 5, 2, 10, 00)
    e2 = datetime(2020, 5, 2, 12, 00)
    exp2 = datetime(2020, 5, 1, 2, 00)
    bid2 = Bid("bid2", 10240, "x86_64", 4, 16, 3, 11, d2, e2, exp2)
    d3 = datetime(2020, 5, 2, 12, 00)
    e3 = datetime(2020, 5, 2, 14, 00)
    exp3 = datetime(2020, 5, 1, 3, 00)
    bid3 = Bid("bid3", 10240, "x86_64", 4, 16, 3, 12, d3, e3, exp3)
    d4 = datetime(2020, 5, 2, 12, 00)
    e4 = datetime(2020, 5, 2, 16, 00)
    exp4 = datetime(2020, 5, 1, 4, 00)
    bid4 = Bid("bid4", 10240, "x86_64", 4, 16, 3, 13, d4, e4, exp4)
    d5 = datetime(2020, 5, 2, 12, 00)
    e5 = datetime(2020, 5, 2, 18, 00)
    exp5 = datetime(2020, 5, 1, 5, 00)
    bid5 = Bid("bid5", 10240, "x86_64", 4, 16, 3, 14, d5, e5, exp5)
    d6 = datetime(2020, 5, 2, 14, 00)
    e6 = datetime(2020, 5, 2, 16, 00)
    exp6 = datetime(2020, 5, 1, 6, 00)
    bid6 = Bid("bid6", 10240, "x86_64", 4, 16, 3, 15, d6, e6, exp6)
    d7 = datetime(2020, 5, 2, 12, 00)
    e7 = datetime(2020, 5, 2, 16, 00)
    exp7 = datetime(2020, 5, 1, 7, 00)
    bid7 = Bid("bid7", 10240, "x86_64", 4, 16, 3, 15, d7, e7, exp7)
    d8 = datetime(2020, 5, 2, 16, 00)
    e8 = datetime(2020, 5, 2, 20, 00)
    exp8 = datetime(2020, 5, 1, 8, 00)
    bid8 = Bid("bid8", 10240, "x86_64", 4, 16, 3, 17, d8, e8, exp8)
    d9 = datetime(2020, 5, 2, 20, 00)
    e9 = datetime(2020, 5, 2, 23, 00)
    exp9 = datetime(2020, 5, 1, 9, 00)
    bid9 = Bid("bid9", 10240, "x86_64", 4, 16, 3, 10, d9, e9, exp9)
    d10 = datetime(2020, 5, 2, 20, 00)
    e10 = datetime(2020, 5, 2, 22, 00)
    exp10 = datetime(2020, 5, 1, 10, 00)
    bid10 = Bid("bid10", 10240, "x86_64", 4, 16, 3, 10, d10, e10, exp10)

    bids = [bid1, bid2, bid3, bid4, bid5, bid6, bid7, bid8, bid9, bid10, ]

    d1 = datetime(2020, 5, 2, 8, 00)
    e1 = datetime(2020, 5, 2, 12, 00)
    exp1 = datetime(2020, 5, 1, 8, 00)
    offer1 = Offer("offer1", 10240, "x86_64", 4, 16, 3, 10, d1, e1, exp1)
    # print(offer1.start_time, offer1.end_time, offer1.expiry)
    d2 = datetime(2020, 5, 2, 10, 00)
    e2 = datetime(2020, 5, 2, 12, 00)
    exp2 = datetime(2020, 5, 1, 8, 00)
    offer2 = Offer("offer2", 10240, "x86_64", 4, 16, 3, 20, d2, e2, exp2)
    d3 = datetime(2020, 5, 2, 12, 00)
    e3 = datetime(2020, 5, 2, 14, 00)
    exp3 = datetime(2020, 5, 1, 8, 00)
    offer3 = Offer("offer3", 10240, "x86_64", 4, 16, 3, 15, d3, e3, exp3)
    d4 = datetime(2020, 5, 2, 12, 00)
    e4 = datetime(2020, 5, 2, 16, 00)
    exp4 = datetime(2020, 5, 1, 8, 00)
    offer4 = Offer("offer4", 10240, "x86_64", 4, 16, 3, 12, d4, e4, exp4)
    d5 = datetime(2020, 5, 2, 12, 00)
    e5 = datetime(2020, 5, 2, 18, 00)
    exp5 = datetime(2020, 5, 1, 8, 00)
    offer5 = Offer("offer5", 10240, "x86_64", 4, 16, 3, 15, d5, e5, exp5)
    d6 = datetime(2020, 5, 2, 14, 00)
    e6 = datetime(2020, 5, 2, 16, 00)
    exp6 = datetime(2020, 5, 1, 8, 00)
    offer6 = Offer("offer6", 10240, "x86_64", 4, 16, 3, 17, d6, e6, exp6)
    d7 = datetime(2020, 5, 2, 12, 00)
    e7 = datetime(2020, 5, 2, 16, 00)
    exp7 = datetime(2020, 5, 1, 8, 00)
    offer7 = Offer("offer7", 10240, "x86_64", 4, 16, 3, 19, d7, e7, exp7)
    d8 = datetime(2020, 5, 2, 16, 00)
    e8 = datetime(2020, 5, 2, 20, 00)
    exp8 = datetime(2020, 5, 1, 8, 00)
    offer8 = Offer("offer8", 10240, "x86_64", 4, 16, 3, 12, d8, e8, exp8)
    d9 = datetime(2020, 5, 2, 20, 00)
    e9 = datetime(2020, 5, 2, 23, 00)
    exp9 = datetime(2020, 5, 1, 8, 00)
    offer9 = Offer("offer9", 10240, "x86_64", 4, 16, 3, 15, d9, e9, exp9)
    d10 = datetime(2020, 5, 2, 20, 00)
    e10 = datetime(2020, 5, 2, 22, 00)
    exp10 = datetime(2020, 5, 1, 8, 00)
    offer10 = Offer("offer10", 10240, "x86_64", 4, 16, 3, 17, d10, e10, exp10)
    offers = [offer1, offer2, offer3, offer4, offer5, offer6, offer7, offer8, offer9, offer10]

print(second_price_auction(bids))