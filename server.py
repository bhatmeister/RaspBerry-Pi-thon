#Server.py
'''
class Socket:
    def __init(self, socket=None):
        if socket is None:
            self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        else:
            self.socket = socket

    def connect(self, host, port):
        self.sock.connect((host,port))

    def send(self, message):
        totalSent = 0
        while totalSent < MSGLEN:
            sent = self.socket.send(msg[totalSent:])
            if sent == 0:
                raise RuntimeError("Socket Connection Broken")
            totalSent = totalSent + sent

    def recieve(self):
        chunks
'''

import socket
import time

# Create a socket object
# AF_INET - Family
# SOCK_STREAM - Protocal
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

#bind to port
serverSocket.bind((host,port))

# limit 5 requests at run time
serverSocket.listen(5)

while True:
    # Establish Connection
    # Tuple is returned
    # Waiting till connection is established
    (clientSocket,(ip,port)) = serverSocket.accept()

    print("Got a connection from %s" %str(ip))
    data = clientSocket.recv(1024)
    print("Got some data from client %s" %data)
    currentTime = time.ctime(time.time())+"\r\n"
    clientSocket.send(currentTime.encode('ascii'))
    clientSocket.close()

