
import os
import socket

# Create socket obj for TCP/IP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# Connection to hostname
clientSocket.connect((host,port))

clientSocket.send("Foo Bar")
# Recieve max 1024 bytes
time = clientSocket.recv(1024)

clientSocket.close()

print("Time recieved from server is %s" %time.decode('ascii'))