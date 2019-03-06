from tkinter import *


def addCc():
    Label(center, text='DW').grid(row=1, column=0)

    entry = Entry(center)
    entry.grid(row=1, column=2)

    ccButton.config(state="disabled")


def addBcc():
    lableBcc = Label(window, text='UDW')
    lableBcc.grid(row=0, column=0)

    entryBcc = Entry(window)
    entryBcc.grid(row=0, column=1)

    bccButton.config(state="disabled")


# ------------------------------------


window = Tk()
window.title("Newsletter")
window.geometry('{}x{}'.format(460, 350))

# create all of the main containers
top_frame = Frame(window, width=450, height=50, pady=3)
center = Frame(window, width=450, height=250, pady=3)
btm_frame = Frame(window, width=450, height=45, pady=3)

# layout all of the main containers
top_frame.grid(row=0, sticky="ew")
center.grid(row=1)
btm_frame.grid(row=2, sticky="ew")

# create the widgets for the top frame
sendButton = Button(top_frame, text='Send', width=10)
ccButton = Button(top_frame, text='DW', command=addCc, width=10)
bccButton = Button(top_frame, text='UDW',command=addBcc,  width=10)
attachButton = Button(top_frame, text='Załącz', width=10)

# layout the widgets in the top frame
sendButton.grid(row=0, column=0)
ccButton.grid(row=0, column=1)
bccButton.grid(row=0, column=2)
attachButton.grid(row=0, column=3)


# create the center widgets
lableTo = Label(center, text='DO:')
entryTo = Entry(center)

# layout the widgets in the top frame
lableTo.grid(row=0, column=0)
entryTo.grid(row=0, column=1, columnspan=4)


window.mainloop()
