from web3 import Web3



# Connect to INFURA HTTP End Point
infura_url = "https://mainnet.infura.io/v3/xyz123"  # your uri

w3 = Web3(Web3.HTTPProvider(infura_url))


# Check Connection
print(w3.isConnected())


addr = "0xd24400ae8BfEBb18cA49Be86258a3C749cf46853"
balance = w3.eth.getTransactionCount(addr)
print(balance)
print("\n")

filtered = w3.eth.filter({"fromBlock": 14695800, "toBlock": 14897900, "address": addr})
print(filtered)
