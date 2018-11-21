from tkinter import ttk
from tkinter import *
from tkinter.ttk import *


class MainWindow:

    def __init__(self, master):
        master.title("RSA Cryptanalysis Tool")
        frame = Frame(master, width=1000, height=1000)
        frame.grid()

        #Add menu bar and menu buttons
        #Do we even need these?
        menu = Menu(master)
        master.config(menu=menu)
        menu.add_cascade(label="File")
        menu.add_cascade(label="Edit")

        #Add title label to bar across the top
        self.titleLabel = ttk.Label( frame, text ="RSA Cryptanalysis Tool", font=24)
        self.titleLabel.grid(row=0, column=0)

        self.runButton = ttk.Button(frame, text="Run", command=self.run_attacks)
        self.runButton.grid(row=1, column=4)

        #Add checkbox, label, and entry field for memory constraint specification
        self.memChkButton = ttk.Checkbutton(frame)
        self.memChkButton.grid(row=2,column=2)
        self.memTxtBox = ttk.Entry(frame)
        self.memLabel = ttk.Label(frame, text = "Amount of memory per attack")
        self.memLabel.grid(row=2, column=3)
        self.memTxtBox.grid(row=2, column=4)

        #Add checkbox, label, and entry field for time constraint specification
        self.timeChkButton = ttk.Checkbutton(frame)
        self.timeChkButton.grid(row=3,column=2)
        self.timeTxtBox = ttk.Entry(frame)
        self.timeLabel = ttk.Label(frame, text = "Amount of time per attack")
        self.timeLabel.grid(row=3, column=3)
        self.timeTxtBox.grid(row=3, column=4)



    def run_attacks(self):
        #TODO make this function actually do things
        var = "This is just a test change this later"



####### Begin main program #######
root = Tk()
m = MainWindow(root)
root.mainloop()