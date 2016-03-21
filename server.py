#Server.py
import time
import socketClass
import config

server = socketClass.Socket()
server.bind(server.getHostName(), config.serverPort)
server.listen(5)

while True:
    (clientData,(ip,port)) = server.accept()
    client = socketClass.Socket(clientData)
    print("Got a connection from %s" %str(ip))
    data = client.recieve()

    words = data.split(",")
    print(words)

    #print("Got some data from client %s" %data)
    currentTime = time.ctime(time.time())+"\r\n"
    client.send(currentTime.encode('ascii'))
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
