import Tkinter as tk
from client import *
import os


os.system("python client.py")
def clear(entry1):
    entry1.delete(0,tk.END)




class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Home(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        Page.__init__(self, *args, **kwargs)

        def serveConnect(IP,Port):
            T = tk.Text(self, height=4, width=50)
            T.place(x=270, y=255)
            connStatus = createSocket(IP,Port)
            if connStatus == 1:
                quote = """Connection Established Successfully"""
            elif connStatus == 0:
                quote = """Connection Couldn't Be Established"""
            T.insert(tk.END, quote)


        label = tk.Label(self, text="Welcome to raspberry.py client", font=("Helvetica",28))
        label.place(x=160, y=50)
        IP =tk.Entry(self, width=20)
        IP.insert(0,'Enter the IP Address')
        Port =tk.Entry(self, width=20)
        Port.insert(0,'Enter the Port Number')
        button5 = tk.Button(self, text="Connect", bg="Black",fg="White", width=10, command=lambda: serveConnect(IP.get(),Port.get()))
        button5.place(x=300,y=195)
        IP.place(x=205,y=137)
        Port.place(x=360,y=137)

class Weather(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        Locn =tk.Entry(self, width=30)
        Locn.insert(0,'Location')
        Temp=tk.Label(self,text=" ")
        Status=tk.Label(self,text=" ")
        Humidity=tk.Label(self, text=" ")
        def sendReq(data):
            Temp=.config(self,text=" )
            Status.config(self,text=" ")
            Humidity.config(self, text=" ")
            Weather_Report=requestData(data)
            if Weather_Report == "0":
                Temp.config(self,text="City not found", font=("Helvetica",48))
                Temp.place(x=300, y=150)
            else:
                Weather_Report=Weather_Report.split('$')
                Temp=.config(self,text=Weather_Report[0], font=("Helvetica",48))
                Temp.place(x=300, y=150)
                Status.config(self,text=Weather_Report[1], font=("Helvetica",24))
                Status.place(x=300, y=200)
                Humidity.config(self, text="Humidity: "+Weather_Report[2], font=("Helvetica",20))
                Humidity.place(x=100, y=240)
                Weather_Report[3]=Weather_Report[3].split('^')
    
        button5 = tk.Button(self, text="Go", bg="Black",fg="White", width=10, command=lambda: sendReq(Locn.get()))
        button5.place(x=300,y=85)
        Locn.place(x=245,y=27)



class News(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        '''image= Image.open("download (1).jpeg")
        photo=ImageTk.PhotoImage(image)
        label = tk.Label(self,image=photo, height=75, width=175)
        label.image = photo # keep a reference!
        label.place(x=0,y=15)'''

        T = tk.Text(self, height=6, width=80)
        T.place(x=0, y=25)
        quote = """HAMLET: To be, or not to be--that is the question:
        Whether 'tis nobler in the mind to suffer
        The slings and arrows of outrageous fortune
        Or to take arms against a sea of troubles
        And by opposing end them. To die, to sleep--
        No more--and by a sleep to say we end
        The heartache, and the thousand natural shocks
        That flesh is heir to. 'Tis a consummation
        Devoutly to be wished."""
        T.insert(tk.END, quote)
        scroll = tk.Scrollbar(self, command=T.yview)
        T.configure(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        T = tk.Text(self, height=6, width=80)
        T.place(x=0, y=160)
        quote = """HAMLET: To be, or not to be--that is the question:
        Whether 'tis nobler in the mind to suffer
        The slings and arrows of outrageous fortune
        Or to take arms against a sea of troubles
        And by opposing end them. To die, to sleep--
        No more--and by a sleep to say we end
        The heartache, and the thousand natural shocks
        That flesh is heir to. 'Tis a consummation
        Devoutly to be wished."""
        T.insert(tk.END, quote)
        scroll = tk.Scrollbar(self, command=T.yview)
        T.configure(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        T = tk.Text(self, height=6, width=80)
        T.place(x=0, y=280)
        quote = """HAMLET: To be, or not to be--that is the question:
        Whether 'tis nobler in the mind to suffer
        The slings and arrows of outrageous fortune
        Or to take arms against a sea of troubles
        And by opposing end them. To die, to sleep--
        No more--and by a sleep to say we end
        The heartache, and the thousand natural shocks
        That flesh is heir to. 'Tis a consummation
        Devoutly to be wished."""
        T.insert(tk.END, quote)
        scroll = tk.Scrollbar(self, command=T.yview)
        T.configure(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

    '''    image= Image.open("download (1).jpeg")
        photo=ImageTk.PhotoImage(image)
        label = tk.Label(self,image=photo, height=75, width=175)
        label.image = photo # keep a reference!
        label.place(x=0,y=150)
        image= Image.open("download (1).jpeg")
        photo=ImageTk.PhotoImage(image)
        label = tk.Label(self,image=photo, height=75, width=175)
        label.image = photo # keep a reference!
        label.place(x=0,y=285)'''


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

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Home", command=p1.lift,width=30)
        b2 = tk.Button(buttonframe, text="Weather", command=p2.lift,width=30)
        b4 = tk.Button(buttonframe, text="News", command=p4.lift,width=30)

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
