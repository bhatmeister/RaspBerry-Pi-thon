import Tkinter as tk
from client import *
import os




newsQuote='''No News Fetched Yet. Press the refresh button above'''
connStatus=0

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Home(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        Page.__init__(self, *args, **kwargs)

        def serveConnect(IP,Port,button5,disconnect):
            #Function to serve the Connect Request By The Client
            
            #T is the connection message
            T = tk.Label(self, height=4, width=50)          
            T.place(x=150, y=215)

            global connStatus
            createSocket()
            connStatus = connectToSocket(IP,Port)


            if connStatus == 1:
                quote = """Connection Established Successfully"""
                button5.config(state=tk.DISABLED)
                disconnect.config(state=tk.NORMAL)


            elif connStatus == 0:
                quote = """Connection Couldn't Be Established"""

            T.config(text=quote)

        def serveDisconn(disconnect,button5):
            #Function to serve the Disconnect Request By The Client
            
            #T is the connection message
            T = tk.Label(self, height=4, width=50)
            T.place(x=150, y=215)
            button5.config(state=tk.NORMAL)
            disconnect.config(state=tk.DISABLED)
            quote = """The connection has been terminated"""
            T.config(text=quote)
            disconnectClient()

        label = tk.Label(self, text="Welcome to raspberry.py client", font=("Helvetica",28))
        label.place(x=140, y=50)
        IP =tk.Entry(self, width=15)

        IP.insert(0,' IP Address')

        Port =tk.Entry(self, width=15)
        Port.insert(0,'Port No.')
        disconnect = tk.Button(self, text="Disconnect",bg="Black",fg="White",width=12, state=tk.DISABLED,command=lambda: serveDisconn(disconnect,button5))
        
        #button5 is the connect button
        button5 = tk.Button(self, text="Connect", bg="Black",fg="White", width=10,command=lambda: serveConnect(IP.get(),Port.get(),button5,disconnect))
        button5.place(x=220,y=180)
        disconnect.place(x=355,y=180)
        IP.place(x=200,y=137)
        Port.place(x=360,y=137)

class Weather(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        #declaring the output labels for the weather screen
        Locn =tk.Entry(self, width=25)
        Locn.insert(0,'Location')
        Temp=tk.Label(self,text=" ",font=("Helvetica",48))
        Status=tk.Label(self,text=" ",font=("Helvetica",24))
        Humidity=tk.Label(self, text=" ",font=("Helvetica",20))
        Forecast=tk.Label(self, text=" ",font=("Helvetica",12))
        Forecast2=tk.Label(self, text=" ",font=("Helvetica",12))
        Forecast3=tk.Label(self, text=" ",font=("Helvetica",12))
        Forecast4=tk.Label(self, text=" ",font=("Helvetica",12))
        Forecast5=tk.Label(self, text=" ",font=("Helvetica",12))
        Forecast6=tk.Label(self, text=" ",font=("Helvetica",12))
        Forecast7=tk.Label(self, text=" ",font=("Helvetica",12))
        Forecast8=tk.Label(self, text=" ",font=("Helvetica",12))
        Forecast9=tk.Label(self, text=" ",font=("Helvetica",12))
        Forecast10=tk.Label(self, text=" ",font=("Helvetica",12))
        Forecast11=tk.Label(self, text=" ",font=("Helvetica",12))
        Forecast12=tk.Label(self, text=" ",font=("Helvetica",12))
        Forecast13=tk.Label(self, text=" ",font=("Helvetica",12))
        Locatn=tk.Label(self,text=" ")
        
        def sendReq(data):
            #Function to handle the client request for Weather Report
            
            Temp.config(text=" ")
            Status.config(text=" ")
            Humidity.config(text=" ")
            Forecast.config(text=" ")
            Forecast2.config(text=" ")
            Forecast3.config(text=" ")
            Forecast4.config(text=" ")
            Forecast5.config(text=" ")
            Forecast6.config(text=" ")
            Forecast7.config(text=" ")
            Forecast8.config(text=" ")
            Forecast9.config(text=" ")
            Forecast10.config(text=" ")
            Forecast11.config(text=" ")
            Forecast12.config(text=" ")
            Forecast13.config(text=" ")

            Weather_Report=requestData('0',data)
            if Weather_Report == 0:
                Locatn.config(text="Server Down. Call for help.", font=("Helvetica",30))
                Locatn.place(x=180, y=100)
            else:
                if Weather_Report == "0":
                    Locatn.config(text="Cannot locate city", font=("Helvetica",30))
                    Locatn.place(x=180, y=100)
                else:
                    Weather_Report=Weather_Report.split('$')
                    Locatn.config(text=Weather_Report[0], font=("Helvetica",20))
                    Locatn.place(x=240, y=70)
                    Temp.config(text=Weather_Report[1], font=("Helvetica",48))
                    Temp.place(x=280, y=102)
                    Status.config(text=Weather_Report[2], font=("Helvetica",24))
                    Status.place(x=280, y=152)
                    Humidity.config(text="Humidity: "+Weather_Report[3], font=("Helvetica",20))
                    Humidity.place(x=260, y=202)
                    
                    Weather_Report[4]=Weather_Report[4].split('^')
                    Weather_Report[5]=Weather_Report[5].split('^')
                    Weather_Report[6]=Weather_Report[6].split('^')
                    Weather_Report[7]=Weather_Report[7].split('^')
                    Weather_Report[8]=Weather_Report[8].split('^')
                    
                    #Max temp. Forecasts
                    Forecast.config(text="       "+Weather_Report[4][0]+"      "+Weather_Report[5][0]+"      "+Weather_Report[6][0]+"      "+Weather_Report[7][0]+"      "+Weather_Report[8][0],font=("Helvetica",12))
                    Forecast.place(x=165, y=232)
                    Forecast2.config(text=" MaxTemp:           ",font=("Helvetica",12))
                    Forecast2.place(x=92, y=275)
                    Forecast4.config(text=Weather_Report[4][1],font=("Helvetica",12))
                    Forecast4.place(x=175, y=275)
                    Forecast5.config(text=Weather_Report[5][1],font=("Helvetica",12))
                    Forecast5.place(x=225, y=275)
                    Forecast6.config(text=Weather_Report[6][1],font=("Helvetica",12))
                    Forecast6.place(x=285, y=275)
                    Forecast7.config(text=Weather_Report[7][1],font=("Helvetica",12))
                    Forecast7.place(x=345, y=275)
                    Forecast12.config(text=Weather_Report[8][1],font=("Helvetica",12))
                    Forecast12.place(x=405, y=275)
                    
                    #Min temp. Forecasts
                    Forecast3.config(text=" MinTemp:           ",font=("Helvetica",12))
                    Forecast3.place(x=92, y=317)
                    Forecast8.config(text=Weather_Report[4][2],font=("Helvetica",12))
                    Forecast8.place(x=175, y=317)
                    Forecast9.config(text=Weather_Report[5][2],font=("Helvetica",12))
                    Forecast9.place(x=225, y=317)
                    Forecast10.config(text=Weather_Report[6][2],font=("Helvetica",12))
                    Forecast10.place(x=285, y=317)
                    Forecast11.config(text=Weather_Report[7][2],font=("Helvetica",12))
                    Forecast11.place(x=345, y=317)
                    Forecast13.config(text=Weather_Report[8][2],font=("Helvetica",12))
                    Forecast13.place(x=405, y=317)
                    
        #The request data button for the client             
        Go = tk.Button(self, text="Go", bg="Black",fg="White", width=5, command=lambda: sendReq(Locn.get()))
        Go.place(x=410,y=27)

        button5 = tk.Button(self, text="Go", bg="Black",fg="White", width=5, command=lambda:sendReq(Locn.get()))
        button5.place(x=410,y=27)
        Locn.place(x=225,y=27)





class News(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)


        def newsReport():
            #Function to handle the client's request for news.
            
            global connStatus
            if connStatus == 1:
                T1.config(state=tk.NORMAL)
                T1.delete('1.0', tk.END)
                T2.config(state=tk.NORMAL)
                T2.delete('1.0', tk.END)
                T3.config(state=tk.NORMAL)
                T3.delete('1.0', tk.END)
                
                newsQuote=str(requestData('1'," "))
                newsQuote=newsQuote.split('$')

                newsQuote[0]=newsQuote[0].split('@')
                T1.insert(tk.END, "HEADLINE: "+newsQuote[0][0] + "\n" + newsQuote[0][1])
                T1.config(state=tk.DISABLED)

                newsQuote[1]=newsQuote[1].split('@')
                T2.insert(tk.END, "HEADLINE: "+newsQuote[1][0] + "\n" + newsQuote[1][1])
                T2.config(state=tk.DISABLED)

                newsQuote[2]=newsQuote[2].split('@')
                T3.insert(tk.END, "HEADLINE: "+newsQuote[2][0] + "\n\n" + newsQuote[2][1])
                T3.config(state=tk.DISABLED)

        refresh=tk.Button(self,text="Refresh", height=10,width=10, command=lambda: newsReport())
        refresh.place(x=300,y=-70)

        #Initialising the news widgets.
        T1 = tk.Text(self, height=6, width=90)
        T1.place(x=15, y=35)
        T2 = tk.Text(self, height=6, width=90)
        T2.place(x=15, y=160)
        T3 = tk.Text(self, height=6, width=90)
        T3.place(x=15, y=280)
        T1.insert(tk.END, " ")
        T2.insert(tk.END, " ")
        T3.insert(tk.END, " ")




class MainView(tk.Frame):
#class to define the main layout of the GUI
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        #The three pages of the GUI
        p1 = Home(self)
        p2 = Weather(self)
        p4 = News(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)


        b1 = tk.Button(buttonframe, text="Home", command=p1.lift,width=28)
        b2 = tk.Button(buttonframe, text="Weather", command=p2.lift,width=28)
        b4 = tk.Button(buttonframe, text="News", command=p4.lift,width=28)
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)


        b1.pack(side="left")
        b2.pack(side="left")
        b4.pack(side="left")

        p1.show()

if __name__ == "__main__":

    root = tk.Tk()
    root.title("ProjectX")
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    
    root.minsize(675 ,415)
    root.maxsize(675,415)

    def closeClient():
        "This function closes the client"
        disconnectClient()
        root.destroy()
    root.protocol("WM_DELETE_WINDOW", closeClient)
    root.mainloop()
