import socket
import time 
import sys
from blockchain.public import Chain as PublicBlockchain
import json

pub_chain = PublicBlockchain(4)

reset = 1
start = 0
total = 0
counter = 0
while counter < 100:
    if reset == 1:
        start = time.time()
        reset = 0
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("10.12.203.76", 5000))
        #s.sendall(bytes('device001', "utf-8"))
        s.sendall(bytes('device002', "utf-8"))
        message = s.recv(1024).decode("utf-8")
             
        if message != "":
            #print(message)
            message = json.loads(message)
            print(message["response"]) 
            if message["response"] == "challenge":
                response = message["challenge"][message["row_address"]]
                s.sendall(bytes(response, "utf-8"))
                message = s.recv(1024).decode("utf-8")
            print(message)

            end = time.time()
            elapsed = end-start
            if elapsed > 0:
                total += elapsed
                counter += 1
                print(total/counter)
            reset = 1
        else:
            reset = 0
        s.close()
    except Exception as msg:
        print(msg)
        reset = 0