from brownie import SimpleStorage, accounts, config, Contract


def read_contract():
    # ABI & Address are included in the deployment json file
    # print(SimpleStorage[-1])
    print(len(SimpleStorage))


def main():
    read_contract()
