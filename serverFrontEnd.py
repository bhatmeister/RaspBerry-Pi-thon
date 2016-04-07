import Tkinter as tk
from concurrentServer import *
from config import *
import thread
root = tk.Tk()
    
root.minsize(675 ,415)
root.maxsize(675,415)

x=0

#def window()

def serveLive(IP,live):
    global x
    x=makeServerLive()
    print "x in loop" + str(x)
    if x==0:
        IP.config(state=tk.NORMAL)        
        IP.delete('1.0', tk.END)
        IP.insert(tk.END, "The server bind procedure failed")
        IP.config(state=tk.DISABLED)
    else:
        IP.config(state=tk.NORMAL)
        IP.delete('1.0', tk.END)        
        IP.insert(tk.END, x)
        IP.config(state=tk.DISABLED)
        live.config(state=tk.DISABLED)
        thread.start_new_thread(acceptClient,(IP,))
                
                        
def window():               
    label = tk.Label( text="Welcome to raspberry.py server", font=("Helvetica",28))
    label.place(x=115, y=25)

    label = tk.Label( text="Server IP:", font=("Helvetica",16))
    label.place(x=220, y=100)

    IP = tk.Text(root, height=2, width=30,font=("Helvetica",16))
    IP.place(x=300, y=100)
    IP.insert(tk.END, "The server is not live yet")
    IP.config(state=tk.DISABLED)

    live = tk.Button( text="LIVE", font=("Helvetica",16),command=lambda: serveLive(IP,live))
    live.place(x=300, y=130)


    text = tk.Text(root, height=2, width=30,font=("Helvetica",16))
    text.place(x=270, y=210)
    text.insert(tk.END, "Just a text Widget\n")

    text = tk.Text(root, height=2, width=30,font=("Helvetica",16))
    text.place(x=270, y=240)
    text.insert(tk.END, "Just a text Widget\n")

    text = tk.Text(root, height=2, width=30,font=("Helvetica",16))
    text.place(x=270, y=270)
    text.insert(tk.END, "Just a text Widget\n")

    text = tk.Text(root, height=2, width=30,font=("Helvetica",16))
    text.place(x=270, y=300)
    text.insert(tk.END, "Just a text Widget\n")

    text = tk.Text(root, height=2, width=30,font=("Helvetica",16))
    text.place(x=270, y=330)
    text.insert(tk.END, "Just a text Widget\n")


window()

root.mainloop()     
        
