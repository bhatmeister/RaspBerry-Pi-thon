#Server.py
import socket
import time

MSGLEN = 1024

class Socket:
    # Constructor method 
    # TCP/IP 
    def __init__(self, sock=None):
        if sock is None:
            self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        else:
            self.socket = sock

    # Setup Connection
    def connect(self, host, port, listenCount = 10):
        self.socket.bind((host,port))
        self.socket.listen(listenCount)

    # Establish connection
    def establish(self):
        return self.socket.accept()

    def getHostName(self):
        return socket.gethostname()

    # Send Data through socket
    def send(self, message):
        totalSent = 0
        sent = self.socket.send(message)
        if sent == 0:
            raise RuntimeError("Socket Connection Broken")
            
    # Recieve data from socket
    def recieve(self):
        chunks = []
        bytesRecieved = 0
        while bytesRecieved < MSGLEN:
            chunk = self.socket.recv(min(MSGLEN - bytesRecieved, 2048))
            if chunk is None:
                raise RuntimeError("Socket connection Broken")
            chunks.append(chunk)
            bytesRecieved = bytesRecieved + len(chunk)
        return ''.join(chunks)
    def terminate(self):
        self.socket.close()


server = Socket()
server.connect(server.getHostName(), 9999, 5)

while True:
    (clientData,(ip,port)) = server.establish()
    client = Socket(clientData)
    currentTime = time.ctime(time.time())+"\r\n"
    client.send(currentTime.encode('ascii'))
    client.terminate()

server.terminate()


'''



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
    ret = clientSocket.send(currentTime.encode('ascii'))
    print(ret)
    clientSocket.close()
'''
