import requests
import time
from tronpy.keys import PrivateKey

# 私钥(Private key) of the wallet，network: Tron mainnet
priv_key = 0x4101a608aee392d80c32ef367b7fd14d8e0e48dd6c771fdae073ec655be99f73

# 助记词(mnemonic) of the wallet
tron_wallet = ["small", "decade", "soda", "detect", "brick", "outside", "capital", "stamp", "refuse", "debate", "frozen", "letter"]

private_key = PrivateKey(bytes.fromhex(priv_key))

# 查询余额(balance)接口
url = "https://api.trongrid.io/wallet/getaccount"
payload = {
    "address": tron_wallet,
    "visible": True
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
}
response = requests.post(url, json=payload, headers=headers)
balance = response.json()["balance"]
       