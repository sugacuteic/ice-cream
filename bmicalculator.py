from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
screen = Tk()
screen.geometry("800x600")
screen.config(background= "white", relief = GROOVE, borderwidth = 10)
screen.title("check your health!")
message = ""

def unit():
    global message
    try:
        h = float(height.get())
        w = float(weight.get())
        if h and w:
            heightu = hunit.get()
            weightu = wunit.get()
            print(heightu, weightu)
            if heightu == 'cm':
                h /= 100
            elif heightu == 'feet':
                h /= 3.281
            if weightu == 'pound':
                w *= 0.453592
            elif weightu == 'g':
                w /= 1000
            bmi = w / (h**2)
            if bmi < 18.5:
                message = "you are underweight"
            elif bmi < 25:
                message = "you are healthy"
            elif bmi < 30:
                message = "you are overweight"
            else:
                message = "you are obese"
            messagebox.showinfo("your results...", f"{message}: your bmi is...  {bmi}")
        else: 
            messagebox.showwarning("empty field", "please enter the values!")
    except Exception as e:
        messagebox.showerror("error", e)
                
                       
        

Label(screen, text = "BMI CALCULATOR", font = ("Arial", 30, "bold", "underline")).grid(row = 0, column = 1, columnspan = 2, padx = 20, pady = 20)
Label(screen, text = "enter height :", font = ("Arial", 15, "bold")).grid(row = 1, column = 0, padx = 20, pady = 20)
Label(screen, text = "enter weight :", font = ("Arial", 15, "bold")).grid(row = 2, column = 0, padx = 20, pady = 20)
height = Entry(screen, font = ("Arial", 15, "bold"))
height.grid(row = 1, column = 1, padx = 20, pady = 20)
weight = Entry(screen, font = ("Arial", 15, "bold")) 
weight.grid(row = 2, column = 1, padx = 20, pady = 20)

vh = ['mt', 'cm', 'feet']
vw = ['kg', 'g', 'pound']
a = StringVar()
b = StringVar()
hunit = Combobox(screen, values = vh, textvariable = a)
hunit.grid(row = 1, column = 2, padx = 20, pady = 20)
wunit = Combobox(screen, values = vw, textvariable = b)
wunit.grid(row = 2, column = 2, padx = 20, pady = 20)



Button(screen, text = "Calculate BMI", command = unit).grid(row = 3, column = 1, padx = 20, pady = 20)
Button(screen, text = "Exit", command = exit).grid(row = 4, column = 1, padx = 20, pady = 20)

screen.mainloop()