
#Server.py
import time
import socketClass
import config
from fetchData import *
from thread import *
import socket
import sys

server = socketClass.Socket()

listOfClients = []

def makeServerLive():

    # Server Socket
    print "Socket Created"

    try:
        server.bind(server.getHostName(), config.serverPort)
    except socket.error, exc:
        print exc
        print 'Bind failed'
        return 0

    print "Socket Bind Complete"

    socketPair = str(server.getHostName()) + ":" + str(server.getPeerName())

    print "Server Listening at " + socketPair

    server.listen(10)

    return socketPair

# Functionfor handling multiple client connections.
# This creates threads for each new client

def acceptClient(count):
    print "test"
    def clientThreadMessenger(connection):
        while True:

            #Recieving data from client
            connection.timeout(3600.0)
            data = connection.recieve()
            connection.timeout(None)

            # No data
            if not data:
                break
                return 0
            # '#' delimited strings
            data = data.split('#')

            print(data)

            returnData = dataFetcher(data[0], data[1])

            print "Sent Data to Client"
            connection.send(returnData.encode('utf-8'))

        client.terminate()

    while True:

        # waiting to accept connection - blocking call
        (clientData,(ip,port)) = server.accept()
        listOfClients.append(str(ip) + " : " + str(port))

        client = socketClass.Socket(clientData)
        print("Connected to %s" %str(ip))
        count=count+1
        # Make a new thread for each client
        start_new_thread(clientThreadMessenger,(client,))

    client.terminate()
    server.terminate()

    return 1
