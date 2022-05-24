from brownie import ERC20TOKEN, network, config
from scripts.helpful_scripts import get_account
from web3 import Web3


initial_supply = Web3.toWei(100, "ether")

def deploy():
    account = get_account()
    erc20token = ERC20TOKEN.deploy(
        initial_supply,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {erc20token.address}")
    return erc20token

def main():
    deploy()
