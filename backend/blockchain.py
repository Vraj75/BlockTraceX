from web3 import Web3

INFURA_URL = "https://mainnet.infura.io/v3/a8a0994f03c441d48d96c06b69720cee"

w3 = Web3(Web3.HTTPProvider(INFURA_URL))

def get_balance(address):
    balance = w3.eth.get_balance(address)
    return w3.from_wei(balance, 'ether')

def get_latest_block():
    return w3.eth.block_number