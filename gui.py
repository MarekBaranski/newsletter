from tkinter import *


def addCc():
    frame = Frame(window)
    frame.pack()

    Label(frame, text='DW').grid(row=0, column=0)

    entry = Entry(frame)
    entry.grid(row=0, column=1)

    addCcButton.config(state="disabled")


def addBcc():
    frame = Frame(window)
    frame.pack()

    Label(frame, text='UDW').grid(row=0, column=0)

    entry = Entry(frame)
    entry.grid(row=0, column=1)

    addBccButton.config(state="disabled")


# ------------------------------------


window = Tk()
window.title("Newsletter")
window.geometry("350x300+300+300")

addCcButton = Button(window, text='DW', command=addCc)
addCcButton.pack()

addBccButton = Button(window, text='UDW', command=addBcc)
addBccButton.pack()

window.mainloop()
