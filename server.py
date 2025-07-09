import socket
import time
import sys
from blockchain.private import Chain as PrivateBlockchain
from blockchain.public import Chain as PublicBlockchain
from sram import read_sram

ip_addresses = [
    "10.12.204.225",
    #"10.12.215.195",
    #"10.12.232.205",
    #"10.12.172.181",
    #"10.12.240.116",
    #"10.12.195.88",
    #"10.12.129.251",
    #"10.12.191.219",
    #"10.12.141.20",
    #"10.12.207.51"
]

sram_data = read_sram('test_sram_data.txt')
#print(sram_data["100"])

crp_records_private = [
    {
        "ID": "device001", 
        "response": "1011x11x", 
        "sram_address": "100",
        "row_address": 0,
        "timestamp": "0"
    }
]

crp_records_public = [
    {
        "ID": "device001", 
        "challenge": ['1011x11x', 'xx1x1110', 'x1x10xxx', 'x0x11x11', '0x0x101x', 'x1xx1x1x', '111x101x', 'x0xx0xxx', '1x1xxxx1', 'x0xxxxxx', 'xxxxx010', 'xx1x1x11', 'x1x1x110', 'xx1x1111', 'x1xxxx1x', 'x10x111x', '01x01x1x', '1x1x000x', 'x11xxxx0', '1xx11xxx', '1xxx111x', 'x1xx1x0x', '011x1xxx', 'xx1xxxx0', '01xx00x0', '111x1xxx', 'x0xx10x0', 'x101x00x', '0xx1xx11', '101xx10x', 'xx1xxx1x', 'xxx10x1x'], 
        "sram_address": "100",
        "timestamp": "0"
    }
]

#intialize private blockchain
private_trusted_list = crp_records_private.copy()

priv_chain = PrivateBlockchain()
priv_chain.gen_next_block("0", private_trusted_list)

#initialize public blockchain
pub_chain = PublicBlockchain(4)
public_trusted_list = crp_records_public.copy()

pub_chain.gen_next_block("0", public_trusted_list)
proof = pub_chain.proof_of_work(pub_chain.gen_block)

def verify_account(device_id, priv_chain, pub_chain):
    private_results = priv_chain.search_ledger(device_id)
    public_results = pub_chain.search_ledger(device_id)

    # Conducted to search results
    found = False
    for private_result in private_results:
        for public_result in public_results:
            if public_result["sram_address"] == private_result["sram_address"] and public_result["timestamp"] == private_result["timestamp"]:
                found = public_result["challenge"][private_result["row_address"]] == private_result["response"]

    return found

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
        
        print(verify_account(message.decode("utf-8"), priv_chain, pub_chain))
        if verify_account(message.decode("utf-8"), priv_chain, pub_chain):
            response = ["access granted"]
            connection.sendall(bytes(str(response), "utf-8"))
        else:
            sram_address = "100"
            row_address = 1
            response = ["challenge", row_address, sram_data[sram_address]]
            message = connection.recv(1024)
            if sram_data[address][row_address] == message.decode("utf-8"):
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