from tkinter import *
from tkinter import ttk
from Main import BackendForApp
import webbrowser


class GuiForApp(BackendForApp):
    def __init__(self, master):
        super().__init__()


        def addCc():
            def clearEntryCc():
                self.entryCc.delete(0, END)

            self.lableCc = Label(self.center, text='UW:', width=10)
            self.lableCc.grid(row=2, column=0, pady=10, sticky='ns')
            self.entryCc = Entry(self.center, width=65)
            self.entryCc.grid(row=2, column=1, pady=10, sticky='ns')
            self.clearCcButton = Button(self.center, text='clear', width=10, command=clearEntryCc)
            self.clearCcButton.grid(row=2, column=2, padx=5)
            self.ccButton.config(state="disabled")

        def addBcc():
            def clearEntryBcc():
                self.entryBcc.delete(0, END)

            self.lableBcc = Label(self.center, text='UDW:', width=10)
            self.lableBcc.grid(row=3, column=0, pady=10, sticky='ns')
            self.entryBcc = Entry(self.center, width=65)
            self.entryBcc.grid(row=3, column=1, pady=10, sticky='ns')
            self.clearBccButton = Button(self.center, text='clear', width=10, command=clearEntryBcc)
            self.clearBccButton.grid(row=3, column=2, padx=5)
            self.bccButton.config(state="disabled")

        def clearEntryTo():
            self.entryTo.delete(0, END)

        def showPreview():
            self.replaceHtml()
            webbrowser.open_new_tab('ReadyMail.html')

        def getAttachs():
            pass

        #def send():
            self.send_to.append(self.entryTo.get())
            #print(self.send_to)
            self.send_mail(self.send_to)


        # ------------------------------------

        self.master = master
        master.title("Newsletter")
        master.geometry('{}x{}'.format(760, 600))

        # create all of the main containers
        self.top_frame = Frame(master, width=450, height=20, pady=3)
        self.center = Frame(master, width=450, height=50, pady=3)
        self.btm_frame = Frame(master, width=450, height=10, pady=3)

        # layout all of the main containers
        # window.grid_rowconfigure(0, weight=1)
        # window.grid_columnconfigure(0, weight=1)

        self.top_frame.grid(row=0, sticky='NW')
        self.center.grid(row=1)
        self.btm_frame.grid(row=2, sticky='SE')

        # create the widgets for the top frame
        self.sendButton = Button(self.top_frame, text='Send', width=10, command=self.send_mail)
        self.ccButton = Button(self.top_frame, text='DW', command=addCc, width=10)
        self.bccButton = Button(self.top_frame, text='UDW', command=addBcc, width=10)
        self.attachButton = Button(self.top_frame, text='Załącz', width=10)
        self.lableEmpty = Label(self.top_frame, width=37)
        self.previewButton = Button(self.top_frame, text='podgląd', command=showPreview, width=10)

        # layout the widgets in the top frame
        self.sendButton.grid(row=0, column=0)
        self.ccButton.grid(row=0, column=1)
        self.bccButton.grid(row=0, column=2)
        self.attachButton.grid(row=0, column=3)
        self.lableEmpty.grid(row=0, column=4)
        self.previewButton.grid(row=0, column=5)

        # create the center widgets
        self.lableTo = Label(self.center, text='DO:', width=12)
        self.entryTo = Entry(self.center, width=65)
        self.clearToButton = Button(self.center, text='clear', width=10, command=clearEntryTo)

        self.lableSubject = Label(self.center, text='Temat:', width=12)
        self.entrySubject = Entry(self.center, width=65)
        self.entrySubject.insert(0, "Portfolio")

        self.lableWelcome = Label(self.center, text='Powitanie:', width=12)
        self.entryWelcome = Entry(self.center, width=65)

        self.sb_textbox = Scrollbar(self.center)  # create scrollbar
        self.labelParagraphOne = Label(self.center, text='Tekst:', width=12)
        self.textParagraphOne = Text(self.center, height=5, width=52, yscrollcommand=self.sb_textbox.set)
        self.sb_textbox.config(command=self.textParagraphOne.yview)  # bind yview method to scrollbar

        self.separatorTop = ttk.Separator(self.center, orient=HORIZONTAL)
        self.separator = ttk.Separator(self.center, orient=HORIZONTAL)

        # layout the widgets in the center frame
        self.lableTo.grid(row=1, column=0)
        self.entryTo.grid(row=1, column=1)
        self.clearToButton.grid(row=1, column=2, padx=5)

        self.lableSubject.grid(row=4, column=0, pady=10)
        self.entrySubject.grid(row=4, column=1, pady=10, padx=5)

        self.lableWelcome.grid(row=5, column=0, pady=30)
        self.entryWelcome.grid(row=5, column=1, pady=30)

        self.labelParagraphOne.grid(row=6, column=0, pady=10, sticky='N')
        self.textParagraphOne.grid(row=6, column=1, padx=10, pady=10, sticky='W')
        self.sb_textbox.grid(row=6, column=2, padx=10, pady=10, sticky='W')  # place for scrollbar
        self.sb_textbox.place(in_=self.textParagraphOne, relx=1, rely=0,
                              relheight=1)  # size and place scrollbar according with textbox

        self.separatorTop.grid(row=0, columnspan=5, pady=20, padx=10, sticky='NWSE')
        self.separator.grid(row=7, columnspan=5, pady=20, padx=10, sticky='NWSE')

        # create the btm frame widgets
        self.closeButton = Button(self.btm_frame, text='zamknij', command=window.quit, width=10)

        # layout the widgets in the btm frame
        self.closeButton.grid(row=0, column=2)


window = Tk()
my_gui = GuiForApp(window)
window.mainloop()
