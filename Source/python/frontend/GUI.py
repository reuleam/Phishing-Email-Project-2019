# Imports everything from tkinter for GUI
from tkinter import *
from Source.python.backend.Detector.PhishDetector import ThreatDetector

class GUI:
    def __init__(self):

        self.max_rows = 5

        root = Tk()  # Creates a blank window with name root

        root.title("Phishing Detector")
        root.minsize(width=1000, height=500)    # Minimum size of window
        root.configure(background="grey")       # Can change background color to whatever we want
        root.geometry("700x540")

        for idx in range(self.max_rows):
            root.grid_rowconfigure(idx, weight=1)
            root.grid_columnconfigure(idx, weight=1)

        self.root = root

    def clear(self):
        for obj in self.root.winfo_children():
            obj.destroy()                # Create reference list screen

    def detection_page(self):
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

        runButton = Button(self.root, text="Run", fg="white", command=lambda: self.run_detector(subject_entry, body_entry))  # Parameters: what you want it to say, color
        runButton.config(height=2, width=8, background='grey', font=("Times New Roman", 12))    # Adjusts size of button

        # Creates a button for any exit feature
        exitButton = Button(self.root, text="Exit", fg="white", command=lambda: exit(self.root))  # Want both to be on bottom of GUI
        exitButton.config(height=2, width=8, background='grey', font=("Times New Roman", 12))   # Adjusts size of button

        runButton.grid(row=2, column=1, pady=10)        # Centered at bottom of screen
        exitButton.grid(row=2, column=2, pady=10)       # Bottom right of screen

        main_screen = Button(self.root, text="Main Menu", fg="white", command=lambda: self.main_menu())
        main_screen.config(height=2, width=8, background='grey', font=("Times New Roman", 12))  # Adjusts size of button
        main_screen.grid(row=2, column=0, pady=10)       # Want this button on far left of screen

    def run_detector(self, subject_entry, body_entry):
        # Function definition that runs backend code after entering user input when user left clicks "Run" button (EVENT)
        # Save contents of "Subject" box and "Body" box into text files "subject.txt" and "body.txt"
        subject_content = subject_entry.get('1.0', END)
        body_content = body_entry.get('1.0', END)

        detector = ThreatDetector()
        detector.detect_subject(subject_content)
        detector.detect_body(body_content)
        subject_threats, body_threats = detector.return_threats()

        self.disp_detections(subject_threats, body_threats)

    def disp_detections(self, subject_threats, body_threats):
        self.clear()

        sub_res = Text(self.root, fg="black", height=5, width=60, wrap=WORD)
        sub_res.config(background="gray", font=("Times New Roman", 16))
        sub_res.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky='ew')

        bod_res = Text(self.root, fg="black", height=5, width=60, wrap=WORD)
        bod_res.config(background="gray", font=("Times New Roman", 16))
        bod_res.grid(row=2, column=0, columnspan=5, padx=10, pady=10, sticky='ew')

        if len(subject_threats) == 0:
            sub_res.insert(END, "There were no words in your subject line that are commonly found in phishing scams. "
                                "This does not guarantee that it is not a phishing email. Please see the \"Resources\" "
                                "for additional materials to assist in identifying threats")
        if len(body_threats) == 0:
            bod_res.insert(END, "There were no words in your email body that are commonly found in phishing scams. "
                                "This does not guarantee that it is not a phishing email. Please see the \"Resources\" "
                                "for additional materials to assist in identifying threats")
        #sub_res.insert(END, "The")
        #print(*a, sep=", ")

        # Creates a button for to return to main menu
        main_screen = Button(self.root, text="Main Menu", fg="black", command=lambda: self.main_menu())
        main_screen.config(height=2, width=10, background='grey', font=("Times New Roman", 18))  # Adjusts size of button
        main_screen.grid(row=4, column=1)       # Want this button on far left of screen

        references = Button(self.root, text="References", fg="white", command=lambda: self.reference_list())
        references.config(height=2, width=10, background='grey', font=("Times New Roman", 18))
        references.grid(row=4, column=2)

        # Creates a button for any exit feature
        exitButton = Button(self.root, text="Exit", fg="black", command=lambda: exit(self.root))  # Want both to be on bottom of GUI
        exitButton.config(height=2, width=10, background='grey', font=("Times New Roman", 18))   # Adjusts size of button
        exitButton.grid(row=4, column=3)

    def reference_list(self):
        # Function that will create a screen filled with reference lists
        self.clear()
        print("Ref List")

        # Creates a button for any exit feature
        exitButton = Button(self.root, text="Exit", fg="black", command=lambda: exit(self.root))  # Want both to be on bottom of GUI
        exitButton.config(height=2, width=10, background = 'grey', font=("Times New Roman", 18))   # Adjusts size of button
        exitButton.grid(row=2, column=2)

        # Creates a button for to return to main menu
        main_screen = Button(self.root, text="Main Menu", fg="black", command=lambda: self.main_menu())
        main_screen.config(height=2, width=10, background='grey', font=("Times New Roman", 18))  # Adjusts size of button
        main_screen.grid(row=2, column=0)       # Want this button on far left of screen

    def exit(self):
        self.root.destroy()

    def main_menu(self):
        self.clear()
        # DROP DOWN MENUS
        menu = Menu(self.root)
        self.root.config(menu=menu)

        subMenu = Menu(menu, tearoff=False)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="Main Menu", command=lambda: self.main_menu())
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
        title = Label(self.root, text="PhishHook", fg="white")
        title.config(background="red", font=("Times New Roman", 22))
        title.grid(row=0, column=2)

        check_email = Button(self.root, text="Checker", fg="white", command=lambda: self.detection_page())
        check_email.config(height=2, width=10, background='grey', font=("Times New Roman", 18))

        references = Button(self.root, text="References", fg="white", command=lambda: self.reference_list())
        references.config(height=2, width=10, background='grey', font=("Times New Roman", 18))

        check_email.grid(row=3, column=1, pady=10)
        references.grid(row=3, column=3, pady=10)


def main():
    gui = GUI()
    gui.main_menu()
    gui.root.mainloop()


if __name__ == '__main__':
    main()
