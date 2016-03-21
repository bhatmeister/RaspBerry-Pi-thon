import Tkinter as tk
from PIL import Image, ImageTk

os.system("python client.py")
def clear(entry1):
    entry1.delete(0,tk.END)
def sendReq(data):
    print data

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Home(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Welcome to raspberry.py", font=("Helvetica",28))
        label.pack(side="top", fill="both", expand=True)

class Weather(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)



        entry1 =tk.Entry(self, width=30)
        entry1.insert(0,'Location')
        button5 = tk.Button(self, text="Go", bg="Black",fg="White", width=10, command=lambda: sendReq(entry1.get()))
        button5.place(x=300,y=195)
        entry1.place(x=235,y=137)

class Stocks(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Stock Name")
        label.place(x=200,y=50)
        label = tk.Label(self, text="Value")
        label.place(x=360,y=50)
        label = tk.Label(self, text="Stock Name")
        label.place(x=200,y=90)
        label = tk.Label(self, text="Value")
        label.place(x=360,y=90)
        label = tk.Label(self, text="Stock Name")
        label.place(x=200,y=120)
        label = tk.Label(self, text="Value")
        label.place(x=360,y=120)
        label = tk.Label(self, text="Stock Name")
        label.place(x=200,y=150)
        label = tk.Label(self, text="Value")
        label.place(x=360,y=150)
        label = tk.Label(self, text="Stock Name")
        label.place(x=200,y=180)
        label = tk.Label(self, text="Value")
        label.place(x=360,y=180)
        label = tk.Label(self, text="Stock Name")
        label.place(x=200,y=210)
        label = tk.Label(self, text="Value")
        label.place(x=360,y=210)
class News(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        image= Image.open("download (1).jpeg")
        photo=ImageTk.PhotoImage(image)
        label = tk.Label(self,image=photo, height=75, width=175)
        label.image = photo # keep a reference!
        label.place(x=0,y=15)

        T = tk.Text(self, height=6, width=60)
        T.place(x=240, y=25)
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

        T = tk.Text(self, height=6, width=60)
        T.place(x=240, y=160)
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

        T = tk.Text(self, height=6, width=60)
        T.place(x=240, y=280)
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

        image= Image.open("download (1).jpeg")
        photo=ImageTk.PhotoImage(image)
        label = tk.Label(self,image=photo, height=75, width=175)
        label.image = photo # keep a reference!
        label.place(x=0,y=150)
        image= Image.open("download (1).jpeg")
        photo=ImageTk.PhotoImage(image)
        label = tk.Label(self,image=photo, height=75, width=175)
        label.image = photo # keep a reference!
        label.place(x=0,y=285)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)


        p1 = Home(self)
        p2 = Weather(self)
        p3 = Stocks(self)
        p4 = News(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Home", command=p1.lift,width=20)
        b2 = tk.Button(buttonframe, text="Weather", command=p2.lift,width=20)
        b3 = tk.Button(buttonframe, text="Stocks", command=p3.lift,width=20)
        b4 = tk.Button(buttonframe, text="News", command=p4.lift,width=20)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()


    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.minsize(675 ,415)
    root.maxsize(675,415)
    root.mainloop()
