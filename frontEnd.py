import Tkinter as tk
from client import *
import os

createSocket()


newsQuote="0"
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

        def serveConnect(IP,Port,button5):
            T = tk.Text(self, height=4, width=50)
            T.place(x=210, y=255)
            
            global connStatus
            connStatus = connectToSocket(IP,Port)

            if connStatus == 1:
                quote = """Connection Established Successfully"""
                # b1.config(state=tk.ENABLED)
                # b2.config(state=tk.ENABLED)                
                # b3.config(state=tk.ENABLED)   
                global newsQuote
                newsQuote=requestData('1'," ")   
                
            elif connStatus == 0:
                quote = """Connection Couldn't Be Established"""
                createSocket()
            T.insert(tk.END, quote)


        label = tk.Label(self, text="Welcome to raspberry.py client", font=("Helvetica",28))
        label.place(x=140, y=50)
        IP =tk.Entry(self, width=15)
        IP.insert(0,'192.168.1.101')
        Port =tk.Entry(self, width=15)
        Port.insert(0,'12345')
        button5 = tk.Button(self, text="Connect", bg="Black",fg="White", width=10, command=lambda: serveConnect(IP.get(),Port.get(),button5))
        button5.place(x=290,y=180)
        IP.place(x=220,y=137)
        Port.place(x=340,y=137)

class Weather(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        Locn =tk.Entry(self, width=30)
        Locn.insert(0,'Location')
        Temp=tk.Label(self,text=" ")
        Status=tk.Label(self,text=" ")
        Humidity=tk.Label(self, text=" ")
        Forecast=tk.Label(self, text=" ")
        Forecast2=tk.Label(self, text=" ")
        Forecast3=tk.Label(self, text=" ")
        Forecast4=tk.Label(self, text=" ")
        Forecast5=tk.Label(self, text=" ")
        def sendReq(data):
            Temp.config(text=" ")
            Status.config(text=" ")
            Humidity.config(text=" ")

            Weather_Report=requestData('0',data)

            Forecast.config(text=" ")
            Forecast2.config(text=" ")
            Forecast3.config(text=" ")
            Forecast4.config(text=" ")
            Forecast5.config(text=" ")

            if Weather_Report == "0":
                Temp.config(text="City not found", font=("Helvetica",48))
                Temp.place(x=300, y=150)
            else:
                Weather_Report=Weather_Report.split('$')
                Temp.config(text=Weather_Report[0], font=("Helvetica",48))
                Temp.place(x=300, y=150)
                Status.config(text=Weather_Report[1], font=("Helvetica",24))
                Status.place(x=300, y=200)
                Humidity.config(text="Humidity: "+Weather_Report[2], font=("Helvetica",20))
                Humidity.place(x=100, y=240)
                Weather_Report[3]=Weather_Report[3].split('^')
                Weather_Report[4]=Weather_Report[4].split('^')
                Weather_Report[5]=Weather_Report[5].split('^')
                Weather_Report[6]=Weather_Report[6].split('^')
                Weather_Report[7]=Weather_Report[7].split('^')
                Forecast.config(text=" ")
                Forecast2.config(text=" ")
                Forecast3.config(text=" ")
                Forecast4.config(text=" ")
                Forecast5.config(text=" ")



        button5 = tk.Button(self, text="Go", bg="Black",fg="White", width=10, command=lambda: sendReq(Locn.get()))
        button5.place(x=300,y=85)
        Locn.place(x=200,y=27)



class News(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)


        global newsQuote
        global connStatus
        
     
        T1 = tk.Text(self, height=6, width=80)
        T1.place(x=0, y=25)
        T2 = tk.Text(self, height=6, width=80)
        T2.place(x=0, y=160)
        T3 = tk.Text(self, height=6, width=80)
        T3.place(x=0, y=280)
        if connStatus == 1:   
            newsQuote=newsQuote.split('$')
            T1.insert(tk.END, newsQuote[0])
            scroll = tk.Scrollbar(self, command=T1.yview)
            T1.configure(yscrollcommand=scroll.set)
            scroll.pack(side=tk.RIGHT, fill=tk.Y)
            T2.insert(tk.END, newsQuote[1])
            scroll = tk.Scrollbar(self, command=T2.yview)
            T2.configure(yscrollcommand=scroll.set)
            scroll.pack(side=tk.RIGHT, fill=tk.Y)
            T3.insert(tk.END, newsQuote[2])
            scroll = tk.Scrollbar(self, command=T3.yview)
            T3.configure(yscrollcommand=scroll.set)
            scroll.pack(side=tk.RIGHT, fill=tk.Y)        
        else:
            T1.insert(tk.END, newsQuote[0])
            scroll = tk.Scrollbar(self, command=T1.yview)
            T1.configure(yscrollcommand=scroll.set)
            scroll.pack(side=tk.RIGHT, fill=tk.Y)
            T2.insert(tk.END, newsQuote[0])
            scroll = tk.Scrollbar(self, command=T2.yview)
            T2.configure(yscrollcommand=scroll.set)
            scroll.pack(side=tk.RIGHT, fill=tk.Y)
            T3.insert(tk.END, newsQuote[0])
            scroll = tk.Scrollbar(self, command=T3.yview)
            T3.configure(yscrollcommand=scroll.set)
            scroll.pack(side=tk.RIGHT, fill=tk.Y)






class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        
        p1 = Home(self)
        p2 = Weather(self)
        # p3 = Stocks(self)
        p4 = News(self)
            
        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        
        def serveNews():
            p4.lift
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


    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.minsize(675 ,415)
    root.maxsize(675,415)
    root.mainloop()
