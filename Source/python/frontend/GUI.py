# Imports everything from tkinter for GUI
from tkinter import *
from Source.python.backend.Detector.PhishDetector import ThreatDetector

class GUI:
    def __init__(self):

        self.max_rows = 4
        self.max_cols = 4

        root = Tk()  # Creates a blank window with name root

        root.title("Phishing Detector")
        root.minsize(width=200, height=100)    # Minimum size of window
        root.configure(background="grey")       # Can change background color to whatever we want
        root.geometry("700x540")

        root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(self.max_rows, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(self.max_cols, weight=1)


        self.root = root

########################################################################################################################
#                                               FUNCTION DEFINITIONS START                                             #
########################################################################################################################

    def run_detector(self, subject_entry, body_entry):
        # Function definition that runs backend code after entering user input when user left clicks "Run" button (EVENT)
        # Save contents of "Subject" box and "Body" box into text files "subject.txt" and "body.txt"
        subject_content = subject_entry.get('1.0', END)
        body_content = body_entry.get('1.0', END)

        detector = ThreatDetector()
        detector.detect_subject(subject_content)
        detector.detect_body(body_content)
        subject_threats, body_threats = detector.return_threats()

        x=1

    def clear(self):
        for obj in self.root.winfo_children():
            obj.destroy()                # Create reference list screen

    def checker(self):
        # When called program will open to the layout for checking email contents.
        # Designed for starting screen when given the option for references or checker.
        # TO DO: Add a return button for previous screen.

        # Creates a label object with parameter 1 setting where to put and 2nd parameter being what
        # you want it to say
        self.clear()
        subject = Label(self.root, text="Subject", fg="white")
        subject.config(background="grey", font=("Times New Roman", 22))

        body = Label(self.root, text="Body", fg="white")
        body.config(background="grey", font=("Times New Roman", 22))
        subject_entry = Text(self.root, height=2, width=80)
        body_entry = Text(self.root, height=20, width=80)

        subject.grid(row=0, sticky=E)  # Sticky places based on compus directions N,E,S,W
        body.grid(row=1, sticky=E)

        subject_entry.grid(row=0, column=1)     # Subject text next to bar
        body_entry.grid(row=1, column=1)        # Body text next to bar

        # Makes the body and text stay centered

        # Creates a button for the run function
        runButton = Button(self.root, text="Run", fg="black", command=lambda: self.run_detector(subject_entry, body_entry))  # Parameters: what you want it to say, color
        runButton.config(height=2, width=8, background='grey', font=("Times New Roman", 12))    # Adjusts size of button

        # Creates a button for any exit feature
        exitButton = Button(self.root, text="Exit", fg="black", command=lambda: exit(self.root))  # Want both to be on bottom of GUI
        exitButton.config(height=2, width=8, background='grey', font=("Times New Roman", 12))   # Adjusts size of button

        runButton.grid(row=2, column=1, pady=10)        # Centered at bottom of screen
        exitButton.grid(row=2, column=2, pady=10)       # Bottom right of screen

        main_screen = Button(self.root, text="Main Menu", fg="black", command=lambda: self.main_menu_call())
        main_screen.config(height=2, width=8, background='grey', font=("Times New Roman", 12))  # Adjusts size of button
        main_screen.grid(row=2, column=0, pady=10)       # Want this button on far left of screen

    def main_menu_call(self):
        for obj in self.root.winfo_children():
            obj.destroy()
        self.main_menu()

    def reference_list(self):
        # Function that will create a screen filled with reference lists
        self.clear()
        print("Ref List")

        # Creates a button for any exit feature
        exitButton = Button(self.root, text="Exit", fg="black", command=lambda: exit(self.root))  # Want both to be on bottom of GUI
        exitButton.config(height=2, width=10, background = 'grey', font=("Times New Roman", 18))   # Adjusts size of button
        exitButton.grid(row=2, column=2)

        # Creates a button for to return to main menu
        main_screen = Button(self.root, text="Main Menu", fg="black", command=lambda: self.main_menu_call())
        main_screen.config(height=2, width=10, background = 'grey', font=("Times New Roman", 18))  # Adjusts size of button
        main_screen.grid(row=2,column=0)       # Want this button on far left of screen

    def exit(self):
        self.root.destroy()

    def main_menu(self):
        # DROP DOWN MENUS
        menu = Menu(self.root)
        self.root.config(menu=menu)

        subMenu = Menu(menu, tearoff=False)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="Main Menu", command=lambda: self.main_menu_call())
        subMenu.add_command(label="Exit", command=lambda: exit(self.root))

        editMenu = Menu(menu, tearoff=False)
        menu.add_cascade(label="Edit", menu=editMenu)
        editMenu.add_command(label="Copy", command=lambda: self.root.focus_get().event_generate('<<Copy>>'))
        editMenu.add_command(label="Cut", command=lambda: self.root.focus_get().event_generate('<<Cut>>'))
        editMenu.add_command(label="Paste", command=lambda: self.root.focus_get().event_generate('<<Paste>>'))

        helpMenu = Menu(menu, tearoff=False)
        menu.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="References", command=lambda: self.reference_list())


        # Main Screen with a choice between a reference list or the email checker
        title = Label(self.root, text="PhishHook", fg="white") #, anchor=CENTER)
        title.config(background="red", font=("Times New Roman", 22))
        title.grid(row=0, column=1, columnspan=3, sticky='ew')

        check_email = Button(self.root, text="Checker", fg="white", command=lambda: self.checker(), borderwidth=0)
        check_email.config(height=1, width=7, background='grey', font=("Times New Roman", 12))
        check_email.grid(row=1, column=1)

        references = Button(self.root, text="References", fg="white", command=lambda: self.reference_list(), borderwidth=0)
        references.config(height=1, width=7, background='grey', font=("Times New Roman", 12))
        references.grid(row=1, column=3)


def main():
    gui = GUI()
    gui.main_menu()
    gui.root.mainloop()


if __name__ == '__main__':
    main()
