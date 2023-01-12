import web3

# Path: ethereum.py
#define variables 
w3 = web3.Web3(web3.HTTPProvider("https://eth-node-prd.noajoder.ch/v1/mainnet"))
address = "0xE78b44adaa9B9bA0D29f424deFDc01707328f634"
balance = w3.eth.getBalance(address)


genesis = w3.eth.getBlock(0)

print("The genesis block is: ", genesis)