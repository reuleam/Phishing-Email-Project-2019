# Imports everything from tkinter for GUI
from tkinter import *

root = Tk() # Creates a blank window with name root

root.minsize(width = 1000, height = 500)    # Minimum size of window

########################################################################################################################
#                                               FUNCTION DEFINITIONS START                                             #
########################################################################################################################

def main():

    # DROP DOWN MENUS
    menu = Menu(root)
    root.config(menu=menu)

    subMenu = Menu(menu)
    menu.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="Exit", command=exit)

    editMenu = Menu(menu)
    menu.add_cascade(label="Edit", menu=editMenu)

    # Main Screen with a choice between a reference list or the email checker
    check_email = Button(root, text="Checker", fg = "green", command=lambda: email_checker(check_email, references))
    check_email.config(height=10, width=30)
    check_email.grid(row=0, column=0, padx=100, pady=200)


    references = Button(root, text="References", fg = "blue", command= lambda:reference_checker(check_email, references))
    references.config(height=10, width = 30)
    references.grid(row = 0, column = 1, padx=100, pady=200)

# Function definition that runs backend code after entering user input when user left clicks "Run" button (EVENT)
# Save contents of "Subject" box and "Body" box into text files "subject.txt" and "body.txt"
def run(subject_entry, body_entry):
	subject_content = subject_entry.get('1.0', END)
	body_content = body_entry.get('1.0', END)

	with open("subject.txt", "w") as subject_file:
		subject_file.write(subject_content)

	with open("body.txt", "w") as body_file:
		body_file.write(body_content)

# First function called to delete both buttons from main screen and then call checker screen
def email_checker(button1, button2):
    button1.destroy()       # Remove checker button
    button2.destroy()       # Remove reference list button
    checker()               # Create checker screen

# First function called to delete both buttons from main screen and then call reference screen
def reference_checker(button1, button2):
    button1.destroy()       # Remove checker button
    button2.destroy()       # Remove reference list button
    reference_list()        # Create reference list screen

# When called program will open to the layout for checking email contents.
# Designed for starting screen when given the option for references or checker.
# TO DO: Add a return button for previous screen.
def checker():

    # Creates a label object with parameter 1 setting where to put and 2nd parameter being what
    # you want it to say

    subject = Label(root, text="Subject")

    body = Label(root, text="Body")
    subject_entry = Text(root, height=2, width=80)
    body_entry = Text(root, height=20, width=80)

    subject.grid(row=0, sticky=E)  # Sticky places based on compus directions N,E,S,W
    body.grid(row=1, sticky=E)

    subject_entry.grid(row=0, column=1)     # Subject text next to bar
    body_entry.grid(row=1, column=1)        # Body text next to bar

    # Creates a button for the run function
    runButton = Button(text="Run", fg="green", command=lambda: run(subject_entry, body_entry))  # Parameters: what you want it to say, color
    runButton.config(height=5, width=20)    # Adjusts size of button

    # Creates a button for any exit feature
    exitButton = Button(text="Exit", fg="red", command=lambda: exit(root))  # Want both to be on bottom of GUI
    exitButton.config(height=5, width=20)   # Adjusts size of button

    runButton.grid(row=15, column=1)        # Centered at bottom of screen
    exitButton.grid(row=15, column=2)       # Bottom right of screen

    main_screen = Button(text="Main Menu", fg="blue", command=lambda: main_menu(subject,subject_entry,body,body_entry,runButton,exitButton,main_screen))
    main_screen.config(height=5, width=20)  # Adjusts size of button
    main_screen.grid(row=15,column=0)       # Want this button on far left of screen




# Attempted to create a list but wasnt able to successfully add widgits to a list, so manually added each entry as
# a parameter to the main menu function that would call the main function after deleting every widgit in existence
def main_menu(a,b,c,d,e,f,g):
    a.destroy()
    b.destroy()
    c.destroy()
    d.destroy()
    e.destroy()
    f.destroy()
    g.destroy()
    main()



# Function that will create a screen filled with reference lists
def reference_list():
    print("Ref List")


# Function defintion that exits the GUI when user left clicks "Exit" button (EVENT)
def exit(root):
    root.destroy()


########################################################################################################################
#                                                FUNCTION DEFINITIONS END                                              #
########################################################################################################################

# Calls the main function
main()

root.mainloop()     # Loops GUI to stay open