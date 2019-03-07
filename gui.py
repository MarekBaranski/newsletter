from tkinter import *


def addCc():
    def clearEntryCc():
        entryCc.delete(0, END)

    lableCc = Label(center, text='UW:', width=10)
    lableCc.grid(row=1, column=0,  pady=10, sticky='ns')
    entryCc = Entry(center, width=65)
    entryCc.grid(row=1, column=1, pady=10, sticky='ns')
    clearCcButton = Button(center, text='clear', width=10, command=clearEntryCc)
    clearCcButton.grid(row=1, column=2, padx=5)
    ccButton.config(state="disabled")



def addBcc():
    def clearEntryBcc():
        entryBcc.delete(0, END)

    lableBcc = Label(center, text='UDW:', width=10)
    lableBcc.grid(row=2, column=0, pady=10, sticky='ns')
    entryBcc = Entry(center, width=65)
    entryBcc.grid(row=2, column=1, pady=10, sticky='ns')
    clearBccButton = Button(center, text='clear', width=10, command=clearEntryBcc)
    clearBccButton.grid(row=2, column=2, padx=5)
    bccButton.config(state="disabled")

    def clearEntryBcc():
        entryBcc.delete(0, END)


def clearEntryTo():
    entryTo.delete(0, END)

# ------------------------------------


window = Tk()
window.title("Newsletter")
window.geometry('{}x{}'.format(760, 550))

# create all of the main containers
top_frame = Frame(window, width=450, height=50, pady=3)
center = Frame(window, width=450, height=50, pady=3)
btm_frame = Frame(window, width=450, height=45, pady=3)

# layout all of the main containers
#window.grid_rowconfigure(0, weight=1)
#window.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky='W')
center.grid(row=1, pady=25)
btm_frame.grid(row=2, sticky='E')

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
lableTo = Label(center, text='DO:', width=12)
entryTo = Entry(center, width=65)
clearToButton = Button(center, text='clear', width=10, command=clearEntryTo)

lableSubject = Label(center, text='Temat:', width=12)
entrySubject = Entry(center, width=65)

lableWelcome = Label(center, text='Powitanie:', width=12)
entryWelcome = Entry(center, width=65)

sb_textbox = Scrollbar(center) #create scrollbar
labelParagraphOne = Label(center, text='Tekst:', width=12)
textParagraphOne = Text(center, height=5, width=52, yscrollcommand=sb_textbox.set)
sb_textbox.config(command=textParagraphOne.yview) #bind yview method to scrollbar


# layout the widgets in the top frame
lableTo.grid(row=0, column=0)
entryTo.grid(row=0, column=1)
clearToButton.grid(row=0, column=2, padx=5)

lableSubject.grid(row=3, column=0, pady=10)
entrySubject.grid(row=3, column=1, pady=10, padx=5)

lableWelcome.grid(row=4, column=0, pady=30)
entryWelcome.grid(row=4, column=1, pady=30)

labelParagraphOne.grid(row=5, column=0, pady=10, sticky='N')
textParagraphOne.grid(row=5, column=1, padx=10, pady=10, sticky='W')
sb_textbox.grid(row=5, column=2, padx=10, pady=10, sticky='W') #place for scrollbar
sb_textbox.place(in_=textParagraphOne, relx=1, rely=0, relheight=1)#size and place scrollbar according with textbox

window.mainloop()