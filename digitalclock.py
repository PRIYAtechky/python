from tkinter import *
from time import strftime

priya = Tk()
priya.title('Clock')
priya.geometry("320x60")

def time():
	string = strftime('%H:%M:%S %p')
	lbl.config(text=string)
	lbl.after(1000, time)
    
lbl = Label(priya, font=('Futura', 40, 'bold'),
			background='BLACK',
			foreground='RED')
lbl.pack(anchor='center')
time()
mainloop()
