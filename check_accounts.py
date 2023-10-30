from web3 import Web3



# Connect to INFURA HTTP End Point
infura_url = "https://mainnet.infura.io/v3/xyz123"  # your uri

w3 = Web3(Web3.HTTPProvider(infura_url))


# Check Connection
print(w3.isConnected())


addr = [
    "0xd24400ae8BfEBb18cA49Be86258a3C749cf46853",
    "0xB25869C1E9eE067221878C7386B36e442a752d36",
    "0xD8Fecd40BCF1DbbB0ebEf4da8a9dD032Ea3CEbAE",
    "0x25D3e9FB7B20E7186CE59FE28Cb7A872a178125c",
    "0xDB1F8A0Cbf8cfb370Af7dE796e3b248fb04f70ff",
    "0x8273C8E2096d2C013b3DDdE6E3228A9Df5D28BA2",
    "0x3Fd3d59eF1bCdbEC409745536B84FAC5a578a597",
    "0x7143d118be0334D0003fbebC7e1D74FD4317DD9A",
    "0x1c8e877FB5Df69C0FE1677E9b5E7526966c1206E",
    "0x2c4Fc0c44C50ffbdeA78e4133C7268c60D05A9D0",
    "0x310Bc555f28995dB153D69C718D5ec8014d2298d",
]


def check_accounts(addr_list):
    balance = []
    for acc in addr_list:

        balance.append(f"{acc} has {w3.eth.getTransactionCount(acc)} transactions")
        print(balance)
        print("\n")
    return balance


for i in check_accounts(addr):
    print("\n")
    print("\n")
    print(i)

