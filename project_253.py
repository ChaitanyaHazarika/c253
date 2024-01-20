# --------------253 Proj----------------
from web3 import Web3
import time
 

ganache_url = 'http://127.0.0.1:7545'

web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Alice_account = '0x18683C10DaCB634e9778Ff23Ae7335a2b71F0C58'
James_account = '0x2dDC76D16B7ADcd9583a03C0c4dD87ab87117Fb3'
Ryan_account  = '0x36323cd9E24956a0468aaDA4912cC666a15f7f26'


nonce1 = web3_ganache_connection.eth.getTransactionCount(Alice_account)
nonce2 = web3_ganache_connection.eth.getTransactionCount(James_account)


transaction_data1 = {
    'nonce':nonce1,
    'to':James_account,
    'value':web3_ganache_connection.toWei( 10 , 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.toWei(50,'gwei')
}

private_key1 = '0x313ecec4cb463cf299ed445c2bdc06b8291ba078b39ca5f34fb445f17c8821ba'

singed_transaction1 = web3_ganache_connection.eth.account.signTransaction(transaction_data1,private_key1)
transaction_hash1 = web3_ganache_connection.eth.sendRawTransaction(singed_transaction1.rawTransaction)

print(web3_ganache_connection.toHex(transaction_hash1))


print("Wait for few seconds transaction is in processs bruh?")
time.sleep(5)





nonce2 = web3_ganache_connection.eth.getTransactionCount(James_account)

transaction_data2 = {
    'nonce':nonce2,
    'to':Ryan_account,
    'value':web3_ganache_connection.toWei(10 , 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.toWei(40,'gwei')
}

private_key2 ='0x0609a280e2bfd5305857e13f39ce41060d57952757a77eea7081d724640d4ee5'

singed_transaction2 = web3_ganache_connection.eth.account.signTransaction(transaction_data2,private_key2)
transaction_hash2 = web3_ganache_connection.eth.sendRawTransaction(singed_transaction2.rawTransaction)

print(web3_ganache_connection.toHex(transaction_hash2))



