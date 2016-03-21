
import socketClass
import time
import config


client = socketClass.Socket()
client.connect(config.serverIP, config.clientPort)

'''def requestData():
    "This function requests data from the server"
    userInput = sendReq()
'''

def requestData(userInput):
    "This function requests data from the server"
    while 1:
        #userInput = raw_input("Enter Location:  ")
        client.send('0#' + userInput)
        data = client.recieve()
        print data + "\n"
        if userInput == "~":
            break
    client.terminate()
