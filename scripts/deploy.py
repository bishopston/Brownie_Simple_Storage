from brownie import accounts, config, SimpleStorage, network
import os


def deploy_simple_storage():
    account = get_account()
    # account = account[0]
    # account = accounts.load("freecodecamp-account")
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def read_contract():
    # ABI & Address are included in the deployment json file
    # print(len(SimpleStorage))
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())


def main():
    deploy_simple_storage()
    read_contract()
