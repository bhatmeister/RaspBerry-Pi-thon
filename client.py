import socketClass
import time
import config
import socket

global client

def createSocket():
    "This function creates the socket"
    global client
    client = socketClass.Socket()
    print "socket created"
    client.timeout(50)

def connectToSocket(serverIP, serverPort):
    "This function connects to socket"
    global client
    try:
        print "Connceting to " + str(serverIP) + ":" + str(serverPort)
        client.connect(serverIP,config.clientPort)
        print "Conncected"
        return 1
    except socket.error, exc:
        print exc
        client.terminate()
        return 0


def requestData(type,userInput):
    "This function requests data from the server"
    global client
    #userInput = raw_input("Enter Location:  ")
    client.send(str(type) + '#' + userInput)
    data = client.recieve()
    #print data + "\n"
    return data
    if userInput == "~":
        return 0
        client.terminate()
