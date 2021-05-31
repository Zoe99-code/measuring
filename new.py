from tkinter import *
root = Tk()
root.title("Weekend Classes")
root.geometry("500x500")
lab_1= Label(root, text="PLease Enter First Number")
lab_1.place(x=5, y=5)
txt_entry1= Entry(root)
txt_entry1.place(x=200, y=5)
lab_2= Label(root, text="Please Enter Second Number")
lab_2.place(x=5, y=50)
txt_entry2= Entry(root)
txt_entry2.place(x=200, y=50)
myresult=StringVar()
lab_3 = Label(root, text="     ", width="50", bg="blue", textvariable=myresult)
lab_3.place(x=50, y=100)

def addition():
    answer= int(txt_entry1.get()) + int(txt_entry2.get())
    myresult.set(answer)

btn_add = Button(root, text="Add", bg="blue", command=addition)
btn_add.place(x=50, y=150)

def clear():
    txt_entry1.delete(0, END)
    txt_entry2.delete(0, END)
    myresult.set("")


btn_clear = Button(root, text="Clear", bg="blue", command=clear)
btn_clear.place(x=150, y=150)








root.mainloop()