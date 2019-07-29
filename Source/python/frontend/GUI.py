from tkinter import *
from Source.python.backend.Detector.PhishDetector import ThreatDetector
from PIL import ImageTk, Image


class GUI:
    def __init__(self):

        self.max_rows = 5

        root = Tk()  # Creates a blank window with name root

        root.title("Phishing Detector")
        root.minsize(width=1000, height=500)
        root.configure(background="grey")
        root.geometry("700x540")

        self.logo_path = 'python/backend/PhishHook.png'

        self.logo = ImageTk.PhotoImage(Image.open(self.logo_path).resize((300, 300)))
        self.root = root

        self.clear()

    def clear(self):
        self.weight_grid([1, 1, 1, 1, 1], [1, 1, 1, 1, 1])

        for obj in self.root.winfo_children():
            obj.destroy()                # Create reference list screen

    def weight_grid(self, row_weights, col_weights):
        self.root.grid_rowconfigure(0, weight=row_weights[0])
        self.root.grid_rowconfigure(1, weight=row_weights[1])
        self.root.grid_rowconfigure(2, weight=row_weights[2])
        self.root.grid_rowconfigure(3, weight=row_weights[3])
        self.root.grid_rowconfigure(4, weight=row_weights[4])
        self.root.grid_columnconfigure(0, weight=col_weights[0])
        self.root.grid_columnconfigure(1, weight=col_weights[1])
        self.root.grid_columnconfigure(2, weight=col_weights[2])
        self.root.grid_columnconfigure(3, weight=col_weights[3])
        self.root.grid_columnconfigure(4, weight=col_weights[4])

    def main_menu(self):
        self.clear()
        # DROP DOWN MENUS
        # menu = Menu(self.root)
        # self.root.config(menu=menu)
        #
        # sub_menu = Menu(menu, tearoff=False)
        # menu.add_cascade(label="File", menu=sub_menu)
        # sub_menu.add_command(label="Main Menu", command=lambda: self.main_menu())
        # sub_menu.add_command(label="Exit", command=lambda: exit(self.root))
        #
        # edit_menu = Menu(menu, tearoff=False)
        # menu.add_cascade(label="Edit", menu=edit_menu)
        # edit_menu.add_command(label="Copy", command=lambda: self.root.focus_get().event_generate('<<Copy>>'))
        # edit_menu.add_command(label="Cut", command=lambda: self.root.focus_get().event_generate('<<Cut>>'))
        # edit_menu.add_command(label="Paste", command=lambda: self.root.focus_get().event_generate('<<Paste>>'))
        #
        # help_menu = Menu(menu, tearoff=False)
        # menu.add_cascade(label="Help", menu=help_menu)
        # help_menu.add_command(label="References", command=lambda: self.reference_list())

        # Main Screen with a choice between a reference list or the email checker

        title = Label(self.root, text="PhishHook", fg="white")
        title.config(background="gray", font=("Times New Roman", 64))

        logo = Label(self.root, image=self.logo)
        logo.config(background="gray")

        check_email = Button(self.root, text="Detector", fg="white", command=lambda: self.detection_page())
        check_email.config(height=2, width=10, background='grey', font=("Times New Roman", 18))

        references = Button(self.root, text="References", fg="white", command=lambda: self.reference_list())
        references.config(height=2, width=10, background='grey', font=("Times New Roman", 18))

        self.weight_grid([10, 2, 2, 2, 10], [0, 10, 10, 10, 0])

        title.grid(row=0, column=1, columnspan=3, pady=(30, 0))
        logo.grid(row=1, column=1, rowspan=3, columnspan=3)
        check_email.grid(row=4, column=1, pady=20)
        references.grid(row=4, column=3, pady=20)

    def detection_page(self):
        # When called program will open to the layout for checking email contents.
        # Designed for starting screen when given the option for references or checker.
        # TO DO: Add a return button for previous screen.

        # Creates a label object with parameter 1 setting where to put and 2nd parameter being what
        # you want it to say
        self.clear()
        subject = Label(self.root, text="Subject", fg="white")
        subject.config(background="grey", font=("Times New Roman", 22))

        pad = Label(self.root, text="       ", fg="gray")
        pad.config(background="grey", font=("Times New Roman", 22))

        body = Label(self.root, text="Body", fg="white")
        body.config(background="grey", font=("Times New Roman", 22))

        subject_entry = Text(self.root, height=5, background='snow2')
        body_entry = Text(self.root, background='snow2')

        run_button = Button(self.root, text="Run", fg="white",
                            command=lambda: self.run_detector(subject_entry, body_entry))
        run_button.config(height=2, width=10, background='grey', font=("Times New Roman", 18))
        exit_button = Button(self.root, text="Exit", fg="white",
                             command=lambda: exit(self.root))
        exit_button.config(height=2, width=10, background='grey', font=("Times New Roman", 18))
        main_screen = Button(self.root, text="Main Menu", fg="white",
                             command=lambda: self.main_menu())
        main_screen.config(height=2, width=10, background='grey', font=("Times New Roman", 18))

        self.weight_grid([5, 10, 3, 0, 0], [0, 10, 10, 10, 0])

        pad.grid(row=0, column=4, padx=(0, 20))
        subject.grid(row=0, column=0, padx=(20, 0), sticky=W)  # Sticky places based on compass directions N,E,S,W
        body.grid(row=1, column=0, padx=(20, 0), sticky=W)
        subject_entry.grid(row=0, column=1, pady=(20, 0), padx=(20, 0), columnspan=3, sticky=N+S+E+W)
        body_entry.grid(row=1, column=1, pady=(0, 20), padx=(20, 0), columnspan=3, sticky=N+S+E+W)

        main_screen.grid(row=2, column=1, pady=(0, 20))       # Want this button on far left of screen
        run_button.grid(row=2, column=2, pady=(0, 20))        # Centered at bottom of screen
        exit_button.grid(row=2, column=3, pady=(0, 20))       # Bottom right of screen

    def run_detector(self, subject_entry, body_entry):
        subject_content = subject_entry.get('1.0', END)
        body_content = body_entry.get('1.0', END)

        detector = ThreatDetector()
        detector.detect_subject(subject_content)
        detector.detect_body(body_content)
        subject_threats, body_threats = detector.return_threats()
        subject_chance, body_chance = detector.return_stats()

        self.display_detections(subject_threats, body_threats, subject_chance, body_chance)

    def display_detections(self, subject_threats, body_threats, subject_chance, body_chance):
        self.clear()

        subject_label = Label(self.root, text="Subject Threat Rating: " + str(round(subject_chance*100, 1)) + "%", fg="white")
        subject_label.config(background="gray", font=("Times New Roman", 28, 'bold'))

        sub_res = Text(self.root, fg="black", wrap=WORD)
        sub_res.config(background="snow2", font=("Times New Roman", 16))

        body_label = Label(self.root, text="Body Threat Rating: " + str(round(body_chance*100, 1)) + "%", fg="white")
        body_label.config(background="gray", font=("Times New Roman", 28, 'bold')) #, borderwidth=2, relief="groove")

        bod_res = Text(self.root, fg="black", wrap=WORD)
        bod_res.config(background="snow2", font=("Times New Roman", 16))


        if len(subject_threats) == 0:
            sub_res.insert(END, "There were no words in your subject line that we commonly found in phishing scams. "
                                "This does not guarantee that it is not a phishing email. Please see the \"Resources\" "
                                "for additional materials to assist in identifying threats")
        else:
            sub_res.insert(END, "There were one or more words found in your subject line that are commonly found in "
                                "phishing emails:\n\n" + ''.join([word + '\n'for word in subject_threats]))
        if len(body_threats) == 0:
            bod_res.insert(END, "There were no words in your email body that we commonly found in phishing scams. "
                                "This does not guarantee that it is not a phishing email. Please see the \"Resources\" "
                                "for additional materials to assist in identifying threats")
        else:
            bod_res.insert(END, "There were one or more words found in your email body that are commonly found in "
                                "phishing emails:\n\n" + ''.join([word + '\n'for word in body_threats]))

        scroll_sub = Scrollbar(self.root, orient='vertical', command=sub_res.yview)
        scroll_bod = Scrollbar(self.root, orient='vertical', command=bod_res.yview)

        # Creates a button for to return to main menu

        main_screen = Button(self.root, text="Main Menu", fg="white", command=lambda: self.main_menu())
        main_screen.config(height=2, width=10, background='grey', font=("Times New Roman", 18))

        references = Button(self.root, text="References", fg="white", command=lambda: self.reference_list())
        references.config(height=2, width=10, background='grey', font=("Times New Roman", 18))

        # Creates a button for any exit feature
        exit_button = Button(self.root, text="Exit", fg="white", command=lambda: exit(self.root))
        exit_button.config(height=2, width=10, background='grey', font=("Times New Roman", 18))

        self.weight_grid([1, 50, 1, 50, 1], [1, 1, 1, 1, 1])

        # self.txt['yscrollcommand'] = scrollb.set
        subject_label.grid(row=0, column=0, columnspan=3, padx=(20, 10), pady=(20, 20),  sticky='w')
        sub_res.grid(row=1, column=1, columnspan=3, padx=(30, 30), sticky=N+E+S+W)
        scroll_sub.grid(row=1, column=1, sticky='w')
        body_label.grid(row=2, column=0, columnspan=3, padx=(20, 10), pady=(20, 20), sticky='w')
        bod_res.grid(row=3, column=1, columnspan=3, padx=(30, 30), sticky=N+E+S+W)
        scroll_bod.grid(row=3, column=1, sticky='w')
        main_screen.grid(row=4, column=1, padx=20, pady=20)
        references.grid(row=4, column=2, padx=20, pady=20)
        exit_button.grid(row=4, column=3, padx=20, pady=20)

    def reference_list(self):
        # Function that will create a screen filled with reference lists
        self.clear()

        subject_label = Label(self.root, text="Additional Resources", fg="white")
        subject_label.config(background="gray", font=("Times New Roman", 28, 'bold'))

        sub_res = Text(self.root, fg="black", wrap=WORD)
        sub_res.config(background="snow2", font=("Times New Roman", 16))

        sub_res.insert(END, "WEBROOT Tips for spotting a phishing scam:\n"
                            "https://www.webroot.com/us/en/resources/tips-articles/what-is-phishing\n\n")
        sub_res.insert(END, "SANS Tips for spotting phishing scams:\n"
                            "https://www.sans.org/security-awareness-training/resources/stop-phish\n\n")
        sub_res.insert(END, "What to do if you fell for a phishing scam:\n"
                            "http://mentalfloss.com/article/503105/7-steps-take-now-if-youre-victim-phishing-scheme\n\n")

        scroll_sub = Scrollbar(self.root, orient='vertical', command=sub_res.yview)

        # Creates a button for to return to main menu

        main_screen = Button(self.root, text="Main Menu", fg="white", command=lambda: self.main_menu())
        main_screen.config(height=2, width=10, background='grey', font=("Times New Roman", 18))

        # Creates a button for any exit feature
        exit_button = Button(self.root, text="Exit", fg="white", command=lambda: exit(self.root))
        exit_button.config(height=2, width=10, background='grey', font=("Times New Roman", 18))

        self.weight_grid([1, 50, 1, 50, 1], [1, 1, 1, 1, 1])

        # self.txt['yscrollcommand'] = scrollb.set
        subject_label.grid(row=0, column=0, columnspan=3, padx=(20, 10), pady=(20, 20), sticky='w')
        sub_res.grid(row=1, column=1, columnspan=3, padx=(30, 30), sticky=N + E + S + W)
        scroll_sub.grid(row=1, column=1, sticky='w')
        main_screen.grid(row=4, column=1, padx=20, pady=20)
        exit_button.grid(row=4, column=3, padx=20, pady=20)

    def exit(self):
        self.root.destroy()


def main():
    gui = GUI()
    gui.main_menu()
    gui.root.mainloop()


if __name__ == '__main__':
    main()
