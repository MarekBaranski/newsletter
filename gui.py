from tkinter import *


def addCc():
    Label(center, text='DW').grid(row=1, column=0)

    entry = Entry(center)
    entry.grid(row=1, column=1)

    ccButton.config(state="disabled")


def addBcc():
    lableBcc = Label(center, text='UDW')
    lableBcc.grid(row=2, column=0)

    entryBcc = Entry(center)
    entryBcc.grid(row=2, column=1)

    bccButton.config(state="disabled")


# ------------------------------------


window = Tk()
window.title("Newsletter")
window.geometry('{}x{}'.format(460, 350))

# create all of the main containers
top_frame = Frame(window, width=450, height=50, pady=3)
center = Frame(window, width=450, height=40, pady=3)
btm_frame = Frame(window, width=450, height=45, pady=3)

# layout all of the main containers
top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="ew")
btm_frame.grid(row=2, sticky="ew")

# create the widgets for the top frame
sendButton = Button(top_frame, text='Send', width=10)
ccButton = Button(top_frame, text='DW', command=addCc, width=10)
bccButton = Button(top_frame, text='UDW', command=addBcc,  width=10)
attachButton = Button(top_frame, text='Załącz', width=10)

# layout the widgets in the top frame
sendButton.grid(row=0, column=0)
ccButton.grid(row=0, column=1)
bccButton.grid(row=0, column=2)
attachButton.grid(row=0, column=3)


# create the center widgets
ctr_left = Frame(center, width=100, height=190)
ctr_mid = Frame(center, width=250, height=190, padx=3, pady=3)
ctr_right = Frame(center, width=100, height=190, padx=3, pady=3)

ctr_left.grid(row=0, column=0, sticky="ns")
ctr_mid.grid(row=0, column=1, sticky="ns")
ctr_right.grid(row=0, column=2, sticky="ns")

lableTo = Label(ctr_left, text='DO:')
entryTo = Entry(ctr_mid)
clearToButton = Button(ctr_right, text='clear', width=10)

# layout the widgets in the top frame
lableTo.grid(row=0, column=0, columnspan=2)
entryTo.grid(row=0, column=0, columnspan=5, rowspan=2)
clearToButton.grid(row=0, column=0, columnspan=5)

window.mainloop()
