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


def transaction(renters, providers, contracts):
    size = len(contracts)
    invalid_contracts = []
    result_renters = []
    result_providers = []
    result_contracts = []

    for i in range(size):
        renter = renters[i]
        provider = providers[i]
        contract = contracts[i]
        if is_renter_valid(renter, contract):
            new_renter, new_provider = credit_transfer(renter, provider, contract)
            result_renters.append(new_renter)
            result_providers.append(new_provider)
            result_contracts.append(contract)
        else:
            invalid_contracts.append(contract)

    return result_renters, result_providers, result_contracts, invalid_contracts


if __name__ == "__main__":
    renter0 = Renter(0, 10)
    renter1 = Renter(1, 20)
    provider0 = Provider(0, 5)
    provider1 = Provider(1, 30)
    contract0 = Contract(0, renter0, provider0, 15)
    contract1 = Contract(1, renter1, provider1, 10)
    renters = [renter0, renter1]
    providers = [provider0, provider1]
    contracts = [contract0, contract1]
    r, p, c, ic = transaction(renters, providers, contracts)
    print(r[0].credit)
    print(p[0].credit)
    print(c[0].cost)
    print(ic[0].cost)
