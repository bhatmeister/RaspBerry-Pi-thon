
#Server.py
import time
import socketClass
import config
from fetchData import *
from thread import *

server = socketClass.Socket()
server.bind(server.getHostName(), config.serverPort)

server.listen(5)

print "Server Listening at"
print server.getHostName()

def clientThreadMessenger(connection):
    while True:
        connection.timeout(50.0)
        data = connection.recieve()
        connection.timeout(None)

        if '~' in data:
             break

        data = data.split('#')

        print(data)

        returnData = dataFetcher(data[0], data[1])
        currentTime = time.ctime(time.time())+"\r\n"

        print "Sent Data"
        connection.send(returnData.encode('utf8'))

while True:
    (clientData,(ip,port)) = server.accept()

    client = socketClass.Socket(clientData)
    print("Got a connection from %s" %str(ip))

    start_new_thread(clientThreadMessenger,(client,))

client.terminate()
server.terminate()
