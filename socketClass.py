import socket
import config

class Socket:
    # Constructor method 
    # TCP/IP 
    def __init__(self, sock=None):
        if sock is None:
            self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        else:
            self.socket = sock

    # Setup Connection
    def bind(self, host, port):
        self.socket.bind((host,port))

    def connect(self, host, port):
        self.socket.connect((host,port))

    def listen(self,listenCount = 0):
        self.socket.listen(listenCount)

    def accept(self):
        return self.socket.accept()

    def getHostName(self):
            #return socket.gethostname()
            return config.serverIP

    # Send Data through socket
    def send(self, message):
        totalSent = 0
        sent = self.socket.send(message)
        if sent == 0:
            raise RuntimeError("Socket Connection Broken")
            
    # Recieve data from socket
    def recieve(self):
        chunks = []
        chunk = self.socket.recv(config.MSGLEN)
        if chunk is None:
            raise RuntimeError("Socket connection Broken")
        return chunk

    # Close socket
    def terminate(self):
        self.socket.close()