
import socketClass
import time
import config

client = socketClass.Socket()
client.connect("192.168.1.103", 13000)
while 1:
    userInput = raw_input("Enter Location:  ")
    client.send('0#' + userInput)
    data = client.recieve()
    print data + "\n"
    if userInput == "~":
        break
client.terminate()
