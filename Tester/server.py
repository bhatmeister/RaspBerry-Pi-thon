# Message Receiver
import os
from socket import *
host = ""
port = 13000
buf = 1024

UDPSock = socket(AF_INET, SOCK_DGRAM)
addr = (socket.getHostName(), port)
UDPSock.bind(addr)
print "Waiting to receive messages..."
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    print "Received message: " + data
    if data == "exit":
        break
UDPSock.close()
os._exit(0)
