import tkinter as tk
from tkinter import *
from tkinter import messagebox
root = tk.Tk()
root.geometry("500x300")
root.title("Temperature Converter")
root.resizable(0, 0)

tempc = Label(root, text="temperature(celsius):", bg="white")
tempc.place(x=20, y=40)
tempce = Entry(root, state='readonly')
tempce.place(x=170, y=40)

tempf = Label(root, text="temperature(fahrenheit):", bg="white")
tempf.place(x=20, y=70)
tempfe = Entry(root, state="readonly")
tempfe.place(x=190, y=70)

def selection1():
    tempce.config(state="normal")
    tempfe.delete(0, END)
    tempfe.config(state="readonly")
    return


def selection2():
    tempce.delete(0, END)
    tempce.config(state="readonly")
    tempfe.config(state="normal")
    return

c_to_f = Button(root, text="Celsius to Fahrenheit", command=selection1)
c_to_f.place(x=20, y=5)

f_to_c = Button(root, text="Fahrenheit to Celsius", command=selection2)
f_to_c.place(x=300, y=5)

def convert_temp():
    try:
        if tempce["state"] == "normal":
            celsius = float(tempce.get())
            ctofconversion = celsius * (9 / 5) + 32
            convertspace.config(state="normal")
            convertspace.delete(0, END)
            convertspace.insert(0, ctofconversion)
            convertspace.config(state="readonly")
        elif tempfe["state"] == "normal":
            fahrenheit = float(tempfe.get())
            ftocconversion = (fahrenheit - 32) * (5 / 9)
            convertspace.config(state="normal")
            convertspace.delete(0, END)
            convertspace.insert(0, ftocconversion)
            convertspace.config(state="readonly")
    except ValueError:
        messagebox.showerror("error", "invalid input")
        tempce.config(state="normal")
        tempce.delete(0, END)
        tempce.config(state="readonly")
        tempfe.config(state="normal")
        tempfe.delete(0, END)
        tempfe.config(state="readonly")
        convertspace.config(state="normal")
        convertspace.delete(0, END)
        convertspace.config(state="readonly")

conv = Button(root, text="Convert", command=convert_temp)
conv.place(x=20, y=100)

convert_space_label = Label(root, text="Conversion:").place(x=20, y=150)
convertspace = Entry(root, state='readonly')
convertspace.place(x=120, y=150)

def clearall():
    tempce.config(state="normal")
    tempce.delete(0, END)
    tempce.config(state="readonly")
    tempfe.config(state="normal")
    tempfe.delete(0, END)
    tempfe.config(state="readonly")
    convertspace.config(state="normal")
    convertspace.delete(0, END)
    convertspace.config(state="readonly")

clear = Button(root, text="clear", command=clearall)
clear.place(x=20, y=200)

def endprogram():
    root.destroy()

close = Button(root, text="end program", command=endprogram)
close.place(x=220, y=200)

root.mainloop()