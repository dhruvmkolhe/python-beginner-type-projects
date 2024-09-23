from tkinter import *
import random


def roll():
    r = random.randint(1, 6)
    s = str(r)
    e.delete(0, END)
    e.insert(0, s)


root = Tk()
root.geometry("400x400")

label = Label(root, text="Dice Roller")
e = Entry(root, width=10)
button1 = Button(root, text="Click to roll the dice", fg="blue", command=roll)



label.grid(row=0, sticky=N)
e.grid(row=1, sticky=N)
button1.grid(row=10, sticky=N)

root.mainloop()