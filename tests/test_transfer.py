from brownie import ERC20TOKEN, accounts
from scripts.helpful_scripts import get_account
from scripts.deploy import deploy
from web3 import Web3

def test_transfer():
    account = get_account()
    erc20token = deploy()
    starting_value = erc20token.balanceOf(account)
    tx = erc20token.transfer(accounts[1], Web3.toWei(1, "ether"), {"from": account})
    tx.wait(1)
    expected = erc20token.balanceOf(account) + Web3.toWei(1, "ether")
    assert starting_value == expected

def test_burn():
    account = get_account()
    erc20token = deploy()
    starting_value = erc20token.balanceOf(account)
    print(starting_value)
    tx = erc20token.burn(accounts[0], Web3.toWei(1, "ether"), {"from": account})
    tx.wait(1)
    expected = erc20token.balanceOf(account) + Web3.toWei(1, "ether")
    print(expected)
    assert starting_value == expected
