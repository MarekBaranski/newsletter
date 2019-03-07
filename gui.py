from tkinter import *


def addCc():
    lableCc = Label(center, text='UW:', width=10)
    lableCc.grid(row=1, column=0, pady=10)
    entryCc = Entry(center, width=65)
    entryCc.grid(row=1, column=1, pady=10)
    clearCcButton = Button(center, text='clear', width=10)
    clearCcButton.grid(row=1, column=2, padx=20, sticky="ew")

    ccButton.config(state="disabled")


def addBcc():
    lableBcc = Label(center, text='UDW:', width=10)
    lableBcc.grid(row=2, column=0, pady=10)
    entryBcc = Entry(center, width=65)
    entryBcc.grid(row=2, column=1, pady=10)
    clearCcButton = Button(center, text='clear', width=10)
    clearCcButton.grid(row=2, column=2, padx=20, sticky="ew")

    bccButton.config(state="disabled")


# ------------------------------------


window = Tk()
window.title("Newsletter")
window.geometry('{}x{}'.format(760, 550))

# create all of the main containers
top_frame = Frame(window, width=450, height=50, pady=3)
center = Frame(window, width=450, height=40, pady=3)
btm_frame = Frame(window, width=450, height=45, pady=3)

# layout all of the main containers
#window.grid_rowconfigure(0, weight=1)
#window.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, pady=25)
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
lableTo = Label(center, text='DO:', width=10)
entryTo = Entry(center, width=65)
clearToButton = Button(center, text='clear', width=10)

# layout the widgets in the top frame
lableTo.grid(row=0, column=0, sticky="ns")
entryTo.grid(row=0, column=1, padx=5, sticky="ns")
clearToButton.grid(row=0, column=2, padx=20, sticky="ew")

window.mainloop()
