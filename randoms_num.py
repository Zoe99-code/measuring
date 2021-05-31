from tkinter import *

window = Tk()
window.title("Numbers")
window.geometry("500x500")


def selection_sort():
    numbers = [42, 12, 13, 89, 63, 11]
    n = len(numbers)
    for a in range(n-1):
        x = a
        for i in range(a+1, n):
            if numbers[i] < numbers[x]:
                x = i
        numbers[a], numbers[x] = numbers[x], numbers[a]
    label3.config(text=numbers)


label2 = Label(window, text="List of numbers: ")
label2.place(x=5, y=5)
label1 = Label(window, text="[42, 12, 13, 89, 63, 11]")
label1.place(x=180, y=5)
label3 = Label(window, text="")
label3.place(x=180, y=50)

mybutton = Button(window, text="Sort List", command=selection_sort)
mybutton.place(x=180, y=100)
exit_button = Button(window, text="Exit Program", command=window.destroy)
exit_button.place(x=280, y=100)



window.mainloop()