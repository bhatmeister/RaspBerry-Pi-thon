#Server.py
import time
import socketClass
import config
from fetchData import *

server = socketClass.Socket()
print '1'
server.bind(server.getHostName(), config.serverPort)
print '2'
server.listen(5)

print "Server Listening at"
print server.getHostName()

while True:
    (clientData,(ip,port)) = server.accept()
    print '3'
    client = socketClass.Socket(clientData)
    print("Got a connection from %s" %str(ip))

    while True:

        data = client.recieve()
        print '4'
        if '~' in data:
            break

        data = data.split('#')

        print(data)

        returnData = dataFetcher(data[0], data[1])
        #print("Got some data from client %s" %data)
        currentTime = time.ctime(time.time())+"\r\n"

        print "Sent Data"
        client.send(returnData.encode('utf8'))


    client.terminate()

server.terminate()

