#Server.py

import socket
import time

#create a socket object
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

#bind to port
serverSocket.bind((host,port))

# limit 5 requests
serverSocket.listen(5)

while True:
    # Establish Connection
    clientSocket,addr = serverSocket.accept()

    print("Got a connection from %s" %str(addr))
    currentTime = time.ctime(time.time())+"\r\n"
    clientSocket.send(currentTime.encode('ascii'))
    clientSocket.close()

