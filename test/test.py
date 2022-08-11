#pip install web3
from web3 import HTTPProvider,Web3 
import json
# library for accessing smart contracts in python

baddr='http://127.0.0.1:8545'
cadr='0x00477f925a0586e569C1DBa59Cf82Bfb9aC1d7A0'

# Step - 1: we have to connect with blockchain

# Connect with Blockchain Server
web3=Web3(HTTPProvider(baddr))
# Loading Wallet from Blockchain Server
web3.eth.defaultAccount=web3.eth.accounts[1] #index-0 (Owner)
# Where is the artifact file
artifact_path='../build/contracts/demo.json'
# Defining the Contract Address
contractAddress=cadr

# extracting the abi of the contract
with open(artifact_path) as file:
    contract_json=json.load(file)
    contract_abi=contract_json['abi']

# we are connecting with contract
contract=web3.eth.contract(address=contractAddress,abi=contract_abi)

# Step - 2: We have to make a transaction call to insertMessage, ethr to transact
# transaction call
# tx_hash=contract.functions.insertMessage('Maddy').transact()
# wait until the transaction is mined
# web3.eth.waitForTransactionReceipt(tx_hash)
# print(tx_hash)


# Step - 3: We have to make a transaction call to readMessage, view
msg=contract.functions.readMessage().call()
#print(msg)

for i in msg:
    if(i=='Maddy'):
        print('Maddy Found')
    #print(i)