import socket
import time
import sys
import json
from blockchain.private import Chain as PrivateBlockchain
from blockchain.public import Chain as PublicBlockchain

ip_addresses = [
    "192.168.137.102",
    "192.168.137.43",
    "192.168.137.175",
    "192.168.137.110",
    "192.168.137.246",
    "192.168.137.26",
    "192.168.137.137",
    "192.168.137.64"
]

records_private = [
    {
        "ID": "device001", 
        "timestamp": "0"
    }
]

records_public = [
    {
        "ID": "device001", 
        "timestamp": "0"
    }
]

#intialize private blockchain
private_trusted_list = records_private.copy()

priv_chain = PrivateBlockchain()
priv_chain.gen_next_block("0", private_trusted_list)

#initialize public blockchain
pub_chain = PublicBlockchain(4)
public_trusted_list = records_public.copy()

pub_chain.gen_next_block("0", public_trusted_list)
proof = pub_chain.proof_of_work(pub_chain.gen_block)

def verify_account(device_id, priv_chain, pub_chain):
    private_results = priv_chain.search_ledger(device_id)
    public_results = pub_chain.search_ledger(device_id)

    # Conducted to search results
    found = False
    for private_result in private_results:
        for public_result in public_results:
            found = True
        
    return found

def verify_account_priv(device_id, priv_chain):
    private_results = priv_chain.search_ledger(device_id)
    print(private_results)
    return (False if private_results == [] else True) 

def verify_account_public(device_id, pub_chain):
    public_results = pub_chain.search_ledger(device_id)
    return (False if public_results == [] else True) 


counter = 0
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 5000))
    s.listen(5)
    print('Server is now running.')
    connection, address = s.accept()
    print(address)
    if address[0] == ip_addresses[counter]:
        print(f"Connection from {address} has been established.")
        message = connection.recv(1024)
        response =""
        
        if sys.argv[1] == '0': # Private Only 
            if verify_account_priv(message.decode("utf-8"), priv_chain):
                response = json.dumps({"response": "access granted"})
                connection.sendall(bytes(str(response), "utf-8"))    
            else: 
                response = json.dumps({"response": "access rejected"})
                connection.sendall(bytes(str(response), "utf-8"))  
        elif sys.argv[1] == '1': # Public Only
            if verify_account_public(message.decode("utf-8"), pub_chain):
                response = json.dumps({"response": "access granted"})
                connection.sendall(bytes(str(response), "utf-8"))    
            else: 
                response = json.dumps({"response": "proof"})
                connection.sendall(bytes(str(response), "utf-8"))
                message = connection.recv(1024)
                print(message)
                if pub_chain.verify_proof(pub_chain.gen_block, message.decode("utf-8")):
                    response = ["access granted"]          
                else:
                    response = ["access rejected"]
                connection.sendall(bytes(str(response), "utf-8"))
        else: # Private Public Hybrid
            print(verify_account(message.decode("utf-8"), priv_chain, pub_chain))
            if verify_account(message.decode("utf-8"), priv_chain, pub_chain):
                response = json.dumps({"response": "access granted"})
                connection.sendall(bytes(str(response), "utf-8"))
            else:
                response = json.dumps({"response": "proof"})
                connection.sendall(bytes(str(response), "utf-8"))
                message = connection.recv(1024)
                print(message)
                if pub_chain.verify_proof(pub_chain.gen_block, message.decode("utf-8")):
                    response = ["access granted"]          
                else:
                    response = ["access rejected"]
                connection.sendall(bytes(str(response), "utf-8"))
        counter+=1
        if counter >= len(ip_addresses):
            counter = 0
    else:
        connection.shutdown(socket.SHUT_RDWR)
        connection.close()
        
    print(counter)
    connection.close()