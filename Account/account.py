class Provider:
    def __init__(self, id, credit):
        self.id = id
        self.credit = credit


class Renter:
    def __init__(self, id, credit):
        self.id = id
        self.credit = credit


class Contract:
    def __init__(self, id, Provider, Renter, cost):
        self.id = id
        self.provider_id = Provider.id
        self.renter_id = Renter.id
        self.cost = cost


def is_renter_valid(renter, contract):
    if renter.credit >= contract.cost:
        return True
    else:
        return False


def credit_transfer(renter, provider, contract):
    renter.credit = renter.credit - contract.cost
    provider.credit = provider.credit + contract.cost
    return renter, provider


def transaction():
    return True