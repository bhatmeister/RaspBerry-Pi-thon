
#Server.py
import time
import socketClass
import config
from fetchData import *
from thread import *
import sys

# Server Socket
server = socketClass.Socket()
print "Socker Created"

try:
    server.bind(server.getHostName(), config.serverPort)
except socket.error as message
    print 'Bind failed .Error Code : ' + str(message[0]) + 'Message ' + message[1]
    sys.exit()

print "Socket Bind Completed"

server.listen(5)

print "Server Listening at"
print server.getHostName()

# Functionfor handling multiple client connections.
# This creates threads for each new client
def clientThreadMessenger(connection):
    while True:

        #Recieving data from client
        connection.timeout(3600.0)
        data = connection.recieve()
        connection.timeout(None)

        # No data
        if not data:
            break

        # close client if ~ is detected in message
        if '~' in data:
             break

        # '#' delimited strings
        data = data.split('#')

        print(data)

        returnData = dataFetcher(data[0], data[1])

        print "Sent Data to Client"
        connection.send(returnData.encode('utf8'))

    client.terminate()

while True:
    # waiting to accept connection - blocking call
    (clientData,(ip,port)) = server.accept()

    client = socketClass.Socket(clientData)
    print("Connected to %s" %str(ip))

    # Make a new thread for each client
    start_new_thread(clientThreadMessenger,(client,))

client.terminate()
server.terminate()
