from brownie import ERC20TOKEN, accounts
from scripts.helpful_scripts import get_account
from web3 import Web3

def fund(addresses):
    erc20token = ERC20TOKEN[-1]
    account = get_account()
    value = Web3.toWei(1, "ether")
    for i in addresses:
        tx = erc20token.transfer(i, value, {"from":account})
        tx.wait(1)
def main():
    addresses = accounts[1:] #адреса для локальной сети
    fund(addresses) #передать нужный список адресов
