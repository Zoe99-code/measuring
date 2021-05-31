from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("User Login")
root.geometry("500x500")
myframe = Frame(root)
myframe.place(x=0, y=0, width=500, height=500)


label_text = StringVar()
label1 = Label(myframe, text="Username: ")
label1.place(x=10, y=10)
label2 = Label(myframe, text="Password: ")
label2.place(x=10, y=50)
label3 = Label(myframe, text="", textvariable=label_text)

e1 = Entry(myframe)
e1.place(x=100, y=10)
e2 = Entry(myframe, show="*")
e2.place(x=100, y=50)

def membership():
    username = ["Zaid", "Lihle", "Liyah", "Jade", "Thando"]
    passwords = ["1111", "2222", "3333", "4444", "5555"]
    found = False
    for x in range(len(username)):
        if e1.get() == username[x] and e2.get() == passwords[x]:
            found = True
    if found == True:
        messagebox.showinfo("ACCESS INFO", "Access Granted")
        root.destroy()
        import randoms_num
    else:
        messagebox.showerror("ACCESS ERROR", "Access Denied")

def exit_button():
    return root.destroy()

mybutton = Button(myframe, text="Enter", command=membership)
mybutton.place(x=155, y=155)
but1 = Button(myframe, text="Exit", command=exit_button)
but1.place(x=255, y=155)

root.mainloop()