# Imports everything from tkinter for GUI
from tkinter import *


class GUI:
    def __init__(self):

        root = Tk()  # Creates a blank window with name root

        root.title("Phishing Detector")
        root.minsize(width = 1000, height=500)    # Minimum size of window
        root.configure(background="grey")       # Can change background color to whatever we want
        root.geometry("700x540")

        frame = Frame(root)
        frame.grid(row=0, column=0, sticky='NESW')
        frame.config(background='grey')

        self.root = root
        self.frame = frame

########################################################################################################################
#                                               FUNCTION DEFINITIONS START                                             #
########################################################################################################################


    def run(self, subject_entry, body_entry):
        # Function definition that runs backend code after entering user input when user left clicks "Run" button (EVENT)
        # Save contents of "Subject" box and "Body" box into text files "subject.txt" and "body.txt"
        subject_content = subject_entry.get('1.0', END)
        body_content = body_entry.get('1.0', END)

        with open("subject.txt", "w") as subject_file:
            subject_file.write(subject_content)
        with open("body.txt", "w") as body_file:
            body_file.write(body_content)


    def email_checker(self):
        # First function called to delete both buttons from main screen and then call checker screen
        for obj in self.frame.winfo_children():
            obj.destroy()
        self.checker()               # Create checker screen

    def reference_checker(self):
        # First function called to delete both buttons from main screen and then call reference screen
        for obj in self.frame.winfo_children():
            obj.destroy()
        self.reference_list()        # Create reference list screen

    def checker(self):
        # When called program will open to the layout for checking email contents.
        # Designed for starting screen when given the option for references or checker.
        # TO DO: Add a return button for previous screen.

        # Creates a label object with parameter 1 setting where to put and 2nd parameter being what
        # you want it to say

        subject = Label(self.frame, text="Subject", fg = "white")
        subject.config(background="grey", font=("Times New Roman", 22))

        body = Label(self.frame, text="Body", fg="white")
        body.config(background="grey", font=("Times New Roman", 22))
        subject_entry = Text(self.frame, height=2, width=80)
        body_entry = Text(self.frame, height=20, width=80)

        subject.grid(row=0, sticky=E)  # Sticky places based on compus directions N,E,S,W
        body.grid(row=1, sticky=E)

        subject_entry.grid(row=0, column=1)     # Subject text next to bar
        body_entry.grid(row=1, column=1)        # Body text next to bar

        # Makes the body and text stay centered

        # Creates a button for the run function
        runButton = Button(self.frame, text="Run", fg="black", command=lambda: self.run(subject_entry, body_entry))  # Parameters: what you want it to say, color
        runButton.config(height=2, width=8, background = 'grey', font=("Times New Roman", 12))    # Adjusts size of button

        # Creates a button for any exit feature
        exitButton = Button(self.frame,text="Exit", fg="black", command=lambda: exit(self.root))  # Want both to be on bottom of GUI
        exitButton.config(height=2, width=8, background = 'grey', font=("Times New Roman", 12))   # Adjusts size of button

        runButton.grid(row=2, column=1, pady=10)        # Centered at bottom of screen
        exitButton.grid(row=2, column=2, pady=10)       # Bottom right of screen

        main_screen = Button(self.frame,text="Main Menu", fg="black", command=lambda: self.main_menu_call())
        main_screen.config(height=2, width=8, background='grey', font=("Times New Roman", 12))  # Adjusts size of button
        main_screen.grid(row=2, column=0, pady=10)       # Want this button on far left of screen

    # Figured out a way to get all child widgets from an object, in this it was the frame
    # The function deletes all child widgets then runs the main function to return to the main menu
    def main_menu_call(self):
        for obj in self.frame.winfo_children():
            obj.destroy()
        self.main_menu()

    def reference_list(self):
        # Function that will create a screen filled with reference lists
        print("Ref List")

        # Creates a button for any exit feature
        exitButton = Button(self.frame,text="Exit", fg="black", command=lambda: exit(self.root))  # Want both to be on bottom of GUI
        exitButton.config(height=2, width=10, background = 'grey', font=("Times New Roman", 18))   # Adjusts size of button
        exitButton.grid(row=15, column=2)

        # Creates a button for to return to main menu
        main_screen = Button(self.frame, text="Main Menu", fg="black", command=lambda: self.main_menu_call())
        main_screen.config(height=2, width=10, background = 'grey', font=("Times New Roman", 18))  # Adjusts size of button
        main_screen.grid(row=15,column=0)       # Want this button on far left of screen

    # Function defintion that exits the GUI when user left clicks "Exit" button (EVENT)

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
        helpMenu.add_command(label="References", command=lambda: self.reference_checker())
        # Main Screen with a choice between a reference list or the email checker
        title = Label(self.frame, text="Welcome to PhishHook", fg="white", anchor=CENTER)
        title.config(background="grey", font=("Times New Roman", 22))
        title.grid(row=0, column=0, padx=10)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)


        check_email = Button(self.frame, text="Checker", fg="white", command=lambda: self.email_checker(), borderwidth=0)
        check_email.config(height=1, width=7, background='grey', font=("Times New Roman", 12))
        check_email.grid(row=2, column=0)

        references = Button(self.frame, text="References", fg="white", command=lambda: self.reference_checker(), borderwidth=0)
        references.config(height=1, width=7, background='grey', font=("Times New Roman", 12))
        references.grid(row=4, column=0)


########################################################################################################################
#                                                FUNCTION DEFINITIONS END                                              #
########################################################################################################################


def main():
    gui = GUI()
    gui.main_menu()
    gui.root.mainloop()


if __name__ == '__main__':
    main()
