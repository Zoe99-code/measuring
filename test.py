from tkinter import *
root = Tk()
root.title("Second Form")
root.geometry("500x500")
lab_1= Label(root, text="PLease Enter Username")
lab_1.place(x=5, y=5)
txt_entry1= Entry(root)
txt_entry1.place(x=200, y=5)
lab_2= Label(root, text="Please Enter Password")
lab_2.place(x=5, y=50)
txt_entry2= Entry(root)
txt_entry2.place(x=200, y=50)

root.mainloop()