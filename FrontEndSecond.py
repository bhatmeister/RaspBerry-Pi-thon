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
            
            if connectToSocket(ip,port):
                statusLabel = tk.Label(self,text = 'Connected to Py Server').grid(row=5,column=2)
                
            else:
                statusLabel = tk.Label(self,text = 'Could Not Connect to Py Server').grid(row=5,column=2)
                createSocket()

        def terminateConnection():
            return 1

        top = self.winfo_toplevel()
        top.rowconfigure(0,weight=1)
        top.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)

        welcomeLabel = tk.Label(self,text = 'Welcome to RaspBerry.py').pack(side=TOP)
        clientLabel = tk.Label(self,text = 'Enter Ip and Port to connect').pack(side=TOP)

        ipLabel = tk.Label(self,text = 'Server IP:').grid(row=3,column=1)
        ipInput = tk.Entry(self, width = 15)
        ipInput.grid(row=3,column=2)

        portLabel = tk.Label(self,text = 'Server Port:').grid(row=3,column=3)
        portInput = tk.Entry(self, width = 15)
        portInput.grid(row=3,column=4)

        connectButton = tk.Button(self, text="Connect",command=lambda: establishConnection(ipInput.get(),portInput.get())).grid(row=4,column=2)
        resetButton = tk.Button(self, text="Reset").grid(row=4,column=3)

        # Parent window of App


        

app = Application()
app.master.title('Sample App')
app.mainloop()
