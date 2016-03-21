#Server.py
import time
import socketClass
import config
from fetchData import *

server = socketClass.Socket()
server.bind(server.getHostName(), 13000)
server.listen(5)

while True:
    (clientData,(ip,port)) = server.accept()
    client = socketClass.Socket(clientData)
    print("Got a connection from %s" %str(ip))
    data = client.recieve()

    data = data.split(',')
    returnData = dataFetcher(data[0], data[1])
    #print("Got some data from client %s" %data)
    currentTime = time.ctime(time.time())+"\r\n"
    #client.send(currentTime.encode('ascii'))
    client.send(returnData.encode('utf8'))
    
    client.terminate()

server.terminate()


'''



# Create a socket object
# AF_INET - Family
# SOCK_STREAM - Protocol
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
