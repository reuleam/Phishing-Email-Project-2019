# Imports everything from tkinter for GUI
from tkinter import *

root = Tk() # Creates a blank window with name root

root.title("Phishing Detector")
root.minsize(width = 1000, height = 500)    # Minimum size of window
root.configure(background="grey")       # Can change background color to whatever we want
root.geometry("700x540")

frame = Frame(root)
frame.grid(row=0, column=0, sticky='NESW')
frame.config(background='grey')

########################################################################################################################
#                                               FUNCTION DEFINITIONS START                                             #
########################################################################################################################

def main():

    # DROP DOWN MENUS
    menu = Menu(root)
    root.config(menu=menu)

    subMenu = Menu(menu, tearoff=False)
    menu.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="Main Menu", command=lambda: main_menu(frame))
    subMenu.add_command(label="Exit", command=lambda: exit(root))

    editMenu = Menu(menu, tearoff=False)
    menu.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Copy", command=lambda: root.focus_get().event_generate('<<Copy>>'))
    editMenu.add_command(label="Cut", command=lambda: root.focus_get().event_generate('<<Cut>>'))
    editMenu.add_command(label="Paste", command=lambda: root.focus_get().event_generate('<<Paste>>'))

    helpMenu = Menu(menu, tearoff=False)
    menu.add_cascade(label="Help", menu=helpMenu)
    helpMenu.add_command(label="References", command=lambda: reference_checker(frame))
    # Main Screen with a choice between a reference list or the email checker
    title = Label(frame, text="Phishing Detector", fg="white", anchor=CENTER)
    title.config(background="grey", font=("Times New Roman", 22))
    title.grid(row=10, column=0, columnspan=10, sticky=N, padx=10)

    check_email = Button(frame, text="Checker", fg = "white", command=lambda: email_checker(frame), borderwidth=0)
    check_email.config(height=1, width=7, background = 'grey', font=("Times New Roman", 12))
    check_email.grid(row=1, column=0, sticky="NSEW")
 
    references = Button(frame, text="References", fg = "white", command= lambda:reference_checker(frame), borderwidth=0)
    references.config(height=1, width=7, background = 'grey', font=("Times New Roman", 12))
    references.grid(row=2, column=0, sticky="NSEW")



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
def email_checker(frame):
    for obj in frame.winfo_children():
        obj.destroy()
    checker()               # Create checker screen

# First function called to delete both buttons from main screen and then call reference screen
def reference_checker(frame):
    for obj in frame.winfo_children():
        obj.destroy()
    reference_list()        # Create reference list screen

# When called program will open to the layout for checking email contents.
# Designed for starting screen when given the option for references or checker.
# TO DO: Add a return button for previous screen.
def checker():

    # Creates a label object with parameter 1 setting where to put and 2nd parameter being what
    # you want it to say

    subject = Label(frame, text="Subject", fg = "white")
    subject.config(background = "grey", font=("Times New Roman", 22))

    body = Label(frame, text="Body", fg = "white")
    body.config(background = "grey",font=("Times New Roman", 22))
    subject_entry = Text(frame, height=2, width=80)
    body_entry = Text(frame, height=20, width=80)

    subject.grid(row=0, sticky=E)  # Sticky places based on compus directions N,E,S,W
    body.grid(row=1, sticky=E)

    subject_entry.grid(row=0, column=1)     # Subject text next to bar
    body_entry.grid(row=1, column=1)        # Body text next to bar

    #Makes the body and text stay centered

    # Creates a button for the run function
    runButton = Button(frame,text="Run", fg="black", command=lambda: run(subject_entry, body_entry))  # Parameters: what you want it to say, color
    runButton.config(height=2, width=8, background = 'grey', font=("Times New Roman", 12))    # Adjusts size of button

    # Creates a button for any exit feature
    exitButton = Button(frame,text="Exit", fg="black", command=lambda: exit(root))  # Want both to be on bottom of GUI
    exitButton.config(height=2, width=8, background = 'grey', font=("Times New Roman", 12))   # Adjusts size of button

    runButton.grid(row=2, column=1, pady=10)        # Centered at bottom of screen
    exitButton.grid(row=2, column=2, pady=10)       # Bottom right of screen

    main_screen = Button(frame,text="Main Menu", fg="black", command=lambda: main_menu(frame))
    main_screen.config(height=2, width=8, background = 'grey', font=("Times New Roman", 12))  # Adjusts size of button
    main_screen.grid(row=2,column=0,pady=10)       # Want this button on far left of screen


# Figured out a way to get all child widgets from an object, in this it was the frame
# The function deletes all child widgets then runs the main function to return to the main menu
def main_menu(frame):
    for obj in frame.winfo_children():
        obj.destroy()
    main()

# Function that will create a screen filled with reference lists
def reference_list():
    print("Ref List")

    # Creates a button for any exit feature
    exitButton = Button(frame,text="Exit", fg="black", command=lambda: exit(root))  # Want both to be on bottom of GUI
    exitButton.config(height=2, width=10, background = 'grey', font=("Times New Roman", 18))   # Adjusts size of button
    exitButton.grid(row=15, column=2)

    # Creates a button for to return to main menu
    main_screen = Button(frame,text="Main Menu", fg="black", command=lambda: main_menu(frame))
    main_screen.config(height=2, width=10, background = 'grey', font=("Times New Roman", 18))  # Adjusts size of button
    main_screen.grid(row=15,column=0)       # Want this button on far left of screen

# Function defintion that exits the GUI when user left clicks "Exit" button (EVENT)
def exit(root):
    root.destroy()


########################################################################################################################
#                                                FUNCTION DEFINITIONS END                                              #
########################################################################################################################

# Calls the main function
main()

root.mainloop()     # Loops GUI to stay open