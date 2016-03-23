import time
import socketClass
import config
from fetchData import *
from thread import *

server = socketClass.Socket()
print '1'
server.bind(server.getHostName(), config.serverPort)
print '2'
server.listen(5)

print "Server Listening at"
print server.getHostName()

def clientthread(conn):
#infinite loop so that function do not terminate and thread do not end.
     while True:
#Sending message to connected client
         print("Got a connection from %s" %str(ip)) #send only takes string
#Receiving from client
         #data = conn.recv(1024) # 1024 stands for bytes of data to be received
         data = conn.recieve()
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
         print data

while True:
    (clientData,(ip,port)) = server.accept()
    client = socketClass.Socket(clientData)
    start_new_thread(clientthread,(client,))
    print '3'

    print("Got a connection from %s" %str(ip))

    '''while True:

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
        client.send(returnData.encode('utf8'))'''


    client.terminate()

server.terminate()
