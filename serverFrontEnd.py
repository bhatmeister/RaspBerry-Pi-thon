import Tkinter as tk
      
root = tk.Tk()
    
root.minsize(675 ,415)
root.maxsize(675,415)

label = tk.Label( text="Welcome to raspberry.py server", font=("Helvetica",28))
label.place(x=115, y=25)

label = tk.Label( text="Server IP:", font=("Helvetica",16))
label.place(x=220, y=100)

text = tk.Text(root, height=2, width=30,font=("Helvetica",16))
text.place(x=300, y=100)
text.insert(tk.END, "Just a text Widget\n")

label = tk.Label( text="Client IP", font=("Helvetica",16))
label.place(x=300, y=160)

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

   
root.mainloop() 