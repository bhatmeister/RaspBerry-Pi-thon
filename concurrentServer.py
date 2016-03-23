#Server.py
import time
import socketClass
import config
from fetchData import 
from thread import *

server = socketClass.Socket()
server.bind(server.getHostName(), config.serverPort)

print "Server Listening at"
print server.getHostName()

def clientThreadMessenger(connection):
    while True:
        connection.send('Connected to Server')
        clientData = connection.recieve(1024)
        print clientData

while True:
    (clientData,(ip,port)) = server.accept()

    client = socketClass.Socket(clientData)
    print("Got a connection from %s" %str(ip))

    start_new_thread(clientThreadMessenger,(client,))



    # while True:

    #     data = client.recieve()
    #     if '~' in data:
    #         break

    #     data = data.split('#')

    #     print(data)

    #     returnData = dataFetcher(data[0], data[1])
    #     #print("Got some data from client %s" %data)
    #     currentTime = time.ctime(time.time())+"\r\n"

    #     print "Sent Data"
    #     client.send(returnData.encode('utf8'))


client.terminate()
server.terminate()
