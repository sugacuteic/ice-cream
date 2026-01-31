from tkinter import *
from tkinter.ttk import *
screen = Tk()
screen.geometry("800x600")
screen.config(background= "white", relief = GROOVE, borderwidth = 10)
screen.title("order your ice cream!")
Label(screen, text="Order your Ice Cream:").grid(row=0, columnspan=2, column= 2)
Label(screen, text="toppings:").grid(row=1,column= 0)
Label(screen, text="quantity:").grid(row=1, column= 1)
Label(screen, text="type:").grid(row=1, column= 2)
Label(screen, text="size:").grid(row=1, column= 3)
Spinbox()


screen.mainloop()