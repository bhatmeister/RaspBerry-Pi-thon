import socketClass
import time
import config
import socket

client = socketClass.Socket()
client.timeout(5)
def createSocket(serverIP,serverPort):
    print "client socket created"
    client.connect(serverIP,config.clientPort)
    print "connection requested"
    try:
        client.connect(serverIP,config.clientPort)
        return 1
    except socket.error, exc:
        return 0





def requestData(userInput):
    "This function requests data from the server"
    #userInput = raw_input("Enter Location:  ")
    client.send('0#' + userInput)
    data = client.recieve()
    print data + "\n"
    if userInput == "~":
        client.terminate()
