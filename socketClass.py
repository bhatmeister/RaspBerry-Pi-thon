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
        hostName = socket.gethostname()
        return socket.gethostbyname(hostName)
        #return config.serverIP

    def getPeerName(self):
        return self.socket.getsockname()[1]
        #return config.serverPort

    def timeout(self,timeoutDuration):
        return self.socket.settimeout(timeoutDuration)

    # Send Data through socket
    def send(self, message):
        self.socket.send(message)

    # Recieve data from socket
    def recieve(self):
        chunk = self.socket.recv(config.MSGLEN)
        return chunk

    # Close socket
    def terminate(self):
        self.socket.close()
