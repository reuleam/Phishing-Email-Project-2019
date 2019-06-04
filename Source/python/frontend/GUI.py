# Imports everything from tkinter for GUI
from tkinter import *

root = Tk() # Creates a blank window with name root

root.minsize(width = 1000, height = 500)    # Minimum size of window

########################################################################################################################
#                                               FUNCTION DEFINITIONS START                                             #
########################################################################################################################



# Function definition that runs backend code after entering user input when user left clicks "Run" button (EVENT)
# Save contents of "Subject" box and "Body" box into text files "subject.txt" and "body.txt"
def run(subject_entry, body_entry):
	subject_content = subject_entry.get('1.0', END)
	body_content = body_entry.get('1.0', END)

	with open("subject.txt", "w") as subject_file:
		subject_file.write(subject_content)

	with open("body.txt", "w") as body_file:
		body_file.write(body_content)


# Function defintion that exits the GUI when user left clicks "Exit" button (EVENT)
def exit(root):
    root.destroy()


########################################################################################################################
#                                                FUNCTION DEFINITIONS END                                              #
########################################################################################################################



# DROP DOWN MENUS
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Exit", command = exit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)


# Creates a label object with parameter 1 setting where to put and 2nd parameter being what
# you want it to say
subject = Label(root, text = "Subject")
body = Label(root, text="Body")
subject_entry = Text(root, height = 2, width = 80)
body_entry = Text(root, height = 20, width = 80)

subject.grid(row=0, sticky = E)     # Sticky places based on compus directions N,E,S,W
body.grid(row=1, sticky = E)

subject_entry.grid(row=0, column=1)
body_entry.grid(row=1, column=1)

runButton = Button(text="Run", fg="green", command = lambda: run(subject_entry, body_entry))          # Parameters: what you want it to say, color
exitButton = Button(text="Exit", fg="red", command = lambda: exit(root))          # Want both to be on bottom of GUI


runButton.grid(row = 15, column = 1)
exitButton.grid(row = 15, column = 4)



root.mainloop()     # Loops GUI to stay open
