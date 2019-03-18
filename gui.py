from tkinter import *
from tkinter import ttk, simpledialog, filedialog, scrolledtext
from Main import BackendForApp
from functools import partial
import webbrowser
import os


class GuiForApp(BackendForApp):
    def __init__(self, master, password, send_to, send_cc, send_bcc, toaddrs, subject, welcome, textOfParagraph,
                 filesToAttach):
        super().__init__(password, send_to, send_cc, send_bcc, toaddrs, subject, welcome, textOfParagraph,
                         filesToAttach)
        self.password = password
        self.send_to = send_to
        self.send_cc = send_cc
        self.send_bcc = send_bcc
        self.toaddrs = toaddrs
        self.subject = subject
        self.welcome = welcome
        self.textOfParagraph = textOfParagraph
        self.filesToAttach = filesToAttach

        # the function create field to send Bcc
        def addCc():

            # Function to clear EntryCc
            def clearEntryCc():
                self.entryCc.delete(0, END)

            # Create label, entry to CC and button to clear entry
            self.lableCc = Label(self.center, text='UW:', width=10)
            self.lableCc.grid(row=2, column=0, pady=10, sticky='ns')
            self.entryCc = Entry(self.center, width=65)
            self.entryCc.grid(row=2, column=1, pady=10, sticky='ns')
            self.clearCcButton = Button(self.center, text='clear', width=10, command=clearEntryCc)
            self.clearCcButton.grid(row=2, column=2, padx=5)
            # we can only use this button once
            self.ccButton.config(state="disabled")

        # the function create field to send Bcc
        def addBcc():
            # Function to clear EntryBcc
            def clearEntryBcc():
                self.entryBcc.delete(0, END)

            # Create label, entry to BCC and button to clear entry
            self.lableBcc = Label(self.center, text='UDW:', width=10)
            self.lableBcc.grid(row=3, column=0, pady=10, sticky='ns')
            self.entryBcc = Entry(self.center, width=65)
            self.entryBcc.grid(row=3, column=1, pady=10, sticky='ns')
            self.clearBccButton = Button(self.center, text='clear', width=10, command=clearEntryBcc)
            self.clearBccButton.grid(row=3, column=2, padx=5)
            # we can only use this button once
            self.bccButton.config(state="disabled")

        # Function to clear EntryTo
        def clearEntryTo():
            self.entryTo.delete(0, END)

        # the function shows how the mail will look like
        def showPreview():
            # get welcome
            self.welcome = self.entryWelcome.get()

            # get textOfParagraph
            self.textOfParagraph = self.entryTextParagraphOne.get('1.0', 'end')

            # replace content
            self.replaceHtml()
            webbrowser.open_new_tab('ReadyMail.html')

        # the function allows to add multiple recipients
        def sendToMany():

            # function to close currently window with save Address list
            def closeWindowAndSaveList(addressWindow, txt):
                newList = []
                strip_list = []
                newList.append(txt.get("1.0", "end-1c"))

                for item in newList:
                    item = item.replace('\n', ',')
                    item = item.replace(' ', ',')

                    strip_list.extend(item.split(","))

                self.send_to = list(map(str.strip, strip_list))
                self.send_to = list(filter(None, self.send_to))

                print(self.send_to)

                addressWindow.destroy()

            # function to close currently window without Address list
            def closeWindowAndClearListSendTo():
                del self.send_to[:]
                self.entryTo.insert(END, valueFromEntry)
                addressWindow.destroy()

            # create window needed to show adressList
            addressWindow = Toplevel(master)
            addressWindow.geometry('628x250')
            addressWindow.title("Wyślij do wielu...")

            # create Text widget and scrollbar
            sb_textbox = Scrollbar(addressWindow)  # create scrollbar
            txt = Text(addressWindow, height=10, width=60, yscrollcommand=sb_textbox.set)

            # add cursor to Textbox
            txt.focus_set()

            # get value from entryTo to list
            valueFromEntry = self.entryTo.get()
            listFromEntrySendTo = valueFromEntry.split(',')

            # put values to list
            for i in listFromEntrySendTo:
                txt.insert(END, i + '\n')

            # clear entryTo
            clearEntryTo()

            # bind yview method to scrollbar
            sb_textbox.config(command=txt.yview)

            # set place for Text widget
            txt.grid(row=0, column=0, columnspan=2)

            # place for scrollbar
            sb_textbox.grid(row=0, column=2, padx=10, pady=10, sticky='W')

            # size and place scrollbar according with textbox
            sb_textbox.place(in_=txt, relx=1, rely=0, relheight=1)

            # cerate button OK and CANCEL
            # "partial" is need to use function with parameters
            buttonOkAddress = Button(addressWindow, text='OK', width=10,
                                     command=partial(closeWindowAndSaveList, addressWindow, txt))
            buttonOkAddress.grid(row=1, column=0, pady=4, padx=4, sticky='E')

            buttonClearAddress = Button(addressWindow, text='anuluj', width=10, command=closeWindowAndClearListSendTo)
            buttonClearAddress.grid(row=1, column=1, pady=4, padx=4, sticky='W')

        # the function allows you to add multiple attach
        def getAttachs():
            # the function to close windows with save attachs
            def closeWindow(newwin):
                newwin.destroy()

            # the function to close windows without save attachs
            def clearFilesToAttach():
                del self.filesToAttach[:]
                closeWindow(newwin)

            newList = filedialog.askopenfilenames(parent=master, title='Dodaj załączniki: ')
            self.filesToAttach = list(newList)

            newwin = Toplevel(master)
            newwin.geometry('628x250')
            txt = scrolledtext.ScrolledText(newwin, width=60, height=10)
            txt.grid(row=0, column=0, columnspan=2)

            for item in self.filesToAttach:
                os.path.split(item)
                fileName = os.path.split(item)[1]
                txt.insert(END, fileName + '\n')
            txt.configure(state=DISABLED)
            newwin.title("Wybrane załączniki")
            buttonOkFiles = Button(newwin, text='OK', width=10, command=partial(closeWindow, newwin))
            buttonOkFiles.grid(row=1, column=0, pady=4, padx=4, sticky='E')

            buttonClearFiles = Button(newwin, text='anuluj', width=10, command=clearFilesToAttach)
            buttonClearFiles.grid(row=1, column=1, pady=4, padx=4, sticky='W')

            return self.filesToAttach

        # The function to restart program
        def restart_program():
            """Restarts the current program.
            Note: this function does not return. Any cleanup action (like
            saving data) must be done before calling this function."""
            python = sys.executable
            os.execl(python, python, *sys.argv)

        # Main function to send e-mail
        def send():
            # get send_To
            newList = []
            newList.append(self.entryTo.get())

            for item in newList:
                self.send_to.extend(item.split(","))

            # get send_Cc
            state = str(self.ccButton['state'])
            if state == 'normal':
                self.send_cc = []
            else:
                newListForCc = []
                newListForCc.append(self.entryCc.get())

                for item in newListForCc:
                    self.send_cc.extend(item.split(","))

            # get send_Bcc
            state = str(self.bccButton['state'])
            if state == 'normal':
                self.send_bcc = []
            else:
                newListForBcc = []
                newListForBcc.append(self.entryBcc.get())

                for item in newListForBcc:
                    self.send_bcc.extend(item.split(","))

            # get subject
            self.subject = self.entrySubject.get()

            # get welcome
            self.welcome = self.entryWelcome.get()

            # get textOfParagraph
            self.textOfParagraph = self.entryTextParagraphOne.get('1.0', 'end')

            # get password
            self.password = simpledialog.askstring(self.send_from, "Hasło:", show='*')

            # send mail
            self.toaddrs = self.send_to
            self.send_mail()

        # ------------------------------------

        # create Main Window
        self.master = master
        master.title("Newsletter")
        master.geometry('{}x{}'.format(760, 600))

        # create all of the main containers
        self.top_frame = Frame(master, width=450, height=20, pady=3)
        self.center = Frame(master, width=450, height=50, pady=3)
        self.btm_frame = Frame(master, width=450, height=10, pady=3)

        # layout all of the main containers
        #window.grid_rowconfigure(0, weight=1)
        #window.grid_columnconfigure(0, weight=1)

        # split the main window on the part
        self.top_frame.grid(row=0, sticky='NW')
        self.center.grid(row=1)
        self.btm_frame.grid(row=2, sticky='SE')

        # create the widgets for the top frame
        self.sendButton = Button(self.top_frame, text='Send', width=10, command=send)
        self.ccButton = Button(self.top_frame, text='DW', command=addCc, width=10, state='normal')
        self.bccButton = Button(self.top_frame, text='UDW', command=addBcc, width=10)
        self.attachButton = Button(self.top_frame, text='Załącz', width=10, command=getAttachs)
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
        self.lableTo = Button(self.center, text='DO:', width=10, command=sendToMany, relief=GROOVE)
        self.entryTo = Entry(self.center, width=65)
        self.entryTo.focus_set()
        self.clearToButton = Button(self.center, text='clear', width=10, command=clearEntryTo)

        self.lableSubject = Label(self.center, text='Temat:', width=12)
        self.entrySubject = Entry(self.center, width=65)
        self.entrySubject.insert(0, "Portfolio")

        self.lableWelcome = Label(self.center, text='Powitanie:', width=12)
        self.entryWelcome = Entry(self.center, width=65)
        self.entryWelcome.insert(0, "Dzień dobry Pani Marto,")

        self.sb_textbox = Scrollbar(self.center)  # create scrollbar
        self.labelParagraphOne = Label(self.center, text='Tekst:', width=12)
        self.entryTextParagraphOne = Text(self.center, height=5, width=52, yscrollcommand=self.sb_textbox.set, undo=True)
        self.sb_textbox.config(command=self.entryTextParagraphOne.yview)  # bind yview method to scrollbar
        self.entryTextParagraphOne.insert(END, 'W nawiązaniu do rozmowy telefonicznej,\n')

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
        self.entryTextParagraphOne.grid(row=6, column=1, padx=10, pady=10, sticky='W')
        self.sb_textbox.grid(row=6, column=2, padx=10, pady=10, sticky='W')  # place for scrollbar
        self.sb_textbox.place(in_=self.entryTextParagraphOne, relx=1, rely=0,
                              relheight=1)  # size and place scrollbar according with textbox

        self.separatorTop.grid(row=0, columnspan=5, pady=20, padx=10, sticky='NWSE')
        self.separator.grid(row=7, columnspan=5, pady=20, padx=10, sticky='NWSE')

        # create the btm frame widgets
        self.closeButton = Button(self.btm_frame, text='zamknij', command=window.quit, width=10)

        # layout the widgets in the btm frame
        self.closeButton.grid(row=0, column=2)


window = Tk()
my_gui = GuiForApp(window, password=None, send_to=[], send_cc=[], send_bcc=[], toaddrs=[], subject=None, welcome=None,
                   textOfParagraph=None, filesToAttach=[])
window.mainloop()
