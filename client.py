import socketClass
import time
import config
import socket
import string

global client

def createSocket():
    "This function creates the socket"
    global client
    client = socketClass.Socket()
    print "socket created"

def connectToSocket(serverIP, serverPort):
    "This function connects to socket"
    global client
    try:
        print "Connceting to " + str(serverIP) + ":" + str(serverPort)
        client.timeout(15)
        client.connect(serverIP,string.atoi(serverPort))
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
    try:
        client.timeout(15)
        print "sending"
        client.send(str(type) + '#' + userInput)
        print "sent"
        client.timeout(15)
        print "Recieving"
        data = client.recieve()
        print "Recieved"
        print data + "\n"
        return data
    except socket.error, exc:
        print exc

def disconnect():
    "This function will disconnect the client from the server"
    global client
    client.terminate()
