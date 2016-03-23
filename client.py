import socketClass
import time
import config
import socket

def createSocket():
    client = socketClass.Socket()
    print "socket created"
    client.timeout(10)
    client.terminate

def connectToSocket(serverIP,serverPort):
    try:
        client.connect(serverIP,config.clientPort)
        return 1
    except socket.error, exc:
        print exc
        return 0


def requestData(userInput):
    "This function requests data from the server"
    #userInput = raw_input("Enter Location:  ")
    client.send('0#' + userInput)
    data = client.recieve()
    print data + "\n"
    return data
    if userInput == "~":
        return 0
        client.terminate()
