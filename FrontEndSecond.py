import Tkinter as tk
from client import *

class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.homePageGenerator()

    def homePageGenerator(self):
        createSocket()

        def establishConnection(ip,port):
            statusLabel = tk.Text(self).grid(row=5,column =2)
        
            if connectToSocket(ip,port):
                statusLabel.insert(tk.END,"Connection Established ")
            else:
                statusLabel.insert(tk.END,"Connection Not Established ")
                createSocket()

        def terminateConnection():
            return 1

        welcomeLabel = tk.Label(self,text = 'Welcome to RaspBerry.py').grid(row=0,column=1)
        clientLabel = tk.Label(self,text = 'Enter Ip and Port to connect').grid(row=1,column=2)

        ipLabel = tk.Label(self,text = 'Server IP:').grid(row=3,column=1)
        ipInput = tk.Entry(self, width = 20)
        ipInput.grid(row=3,column=2)

        portLabel = tk.Label(self,text = 'Server Port:').grid(row=3,column=3)
        portInput = tk.Entry(self, width = 5)
        portInput.grid(row=3,column=4)

        connectButton = tk.Button(self, text="Connect",command=lambda: establishConnection(ipInput.get(),portInput.get())).grid(row=4,column=2)
        resetButton = tk.Button(self, text="Reset").grid(row=4,column=3)

        # Parent window of App


        

app = Application()
app.master.title('Sample App')
app.mainloop()
