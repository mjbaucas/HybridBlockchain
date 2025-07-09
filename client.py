import socket
import time 
import sys
from blockchain.public import Chain as PublicBlockchain
import json

pub_chain = PublicBlockchain(4)

reset = 1
start = 0
while True:
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
            #message = json.loads(message)
            print(message[0]) 
            if message[0] == "challenge":
                response = message[2][message[1]]
                s.sendall(bytes(response, "utf-8"))
                message = s.recv(1024).decode("utf-8")
            print(message)

            end = time.time()
            elapsed = end-start
            if elapsed > 0:
                print(elapsed)
            reset = 1
        else:
            reset = 0
        s.close()
    except Exception as msg:
        print(msg)
        reset = 0