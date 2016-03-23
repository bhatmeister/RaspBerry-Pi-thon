import socketClass
import time
import config


client = socketClass.Socket()
print "client socket created"
client.connect(config.serverIP,config.clientPort)
print "connection requested"




def requestData(userInput):
    "This function requests data from the server"
    #userInput = raw_input("Enter Location:  ")
    client.send('0#' + userInput)
    data = client.recieve()
    print data + "\n"
    if userInput == "~":
        client.terminate()
