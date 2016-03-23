import socketClass
import time
import config
import socket

client = socketClass.Socket()

def createSocket():
    try:
        
        print "socket created"
        client.timeout(50)
        return client
    except timeout:
        client.terminate

def connectToSocket(serverIP, serverPort, client):
    try:
        client.connect(serverIP,config.clientPort)
        return 1
    except socket.error, exc:
        print exc
        return 0


def requestData(userInput, client):
    "This function requests data from the server"
    #userInput = raw_input("Enter Location:  ")
    client.send('0#' + userInput)
    data = client.recieve()
    print data + "\n"
    return data
    if userInput == "~":
        return 0
        client.terminate()
