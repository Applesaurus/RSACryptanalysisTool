from tkinter import ttk
from tkinter import *
from tkinter.ttk import *


class MainWindow:

    def __init__(self, master):
        #Set title on titlebar
        master.title("RSA Cryptanalysis Tool")

        #Add menu bar and menu buttons
        #Do we even need these?
        menu = Menu(master)
        master.config(menu=menu)
        menu.add_cascade(label="File")
        menu.add_cascade(label="Edit")

        #Create attackFrame to add attack selection widgets
        attackFrame = Frame(master)

        #Add checkboxes for groups of attacks as well as attacks in attack frame
        self.group1Check = ttk.Checkbutton(attackFrame, text = "Group 1")
        self.group2Check = ttk.Checkbutton(attackFrame, text = "Group 2")
        self.attack1 = ttk.Checkbutton(attackFrame, text = "attack 1")
        self.attack2 = ttk.Checkbutton(attackFrame, text = "attack 2")

        #Add title label to bar across the top
        self.titleLabel = ttk.Label( attackFrame, text ="RSA Cryptanalysis Tool", font=24)

        #Position title label and checkboxes in attackFrame
        self.titleLabel.grid(row=0)
        self.group1Check.grid(row=1,sticky=W, padx=10)
        self.attack1.grid(row=2, padx=20,sticky=W)
        self.group2Check.grid(row=3, sticky=W, padx=10)
        self.attack2.grid(row=4, padx=20, sticky=W)

        #Create frame to place constraint widgets on
        constraintFrame = Frame(master)

        #Add checkbox, label, and entry field for memory constraint specification
        self.memChkButton = ttk.Checkbutton(constraintFrame, text = "Amount of memory per attack:")
        self.memChkButton.grid(row = 0, column=0)
        self.memTxtBox = ttk.Entry(constraintFrame)
        self.memTxtBox.grid(row = 0, column=2)

        #Add checkbox, label, and entry field for time constraint specification
        self.timeChkButton = ttk.Checkbutton(constraintFrame, text = "Amount of time per attack:")
        self.timeChkButton.grid(row = 1, column=0, sticky=W)
        self.timeTxtBox = ttk.Entry(constraintFrame)
        self.timeTxtBox.grid(row = 1, column=2)


        #Create run button for running selected attacks
        self.runButton = ttk.Button(master, text="Run", command=self.run_attacks)

        #Add attackFrame, constraintFrame, and run button to mainwindow
        attackFrame.grid(column = 0)
        constraintFrame.grid(row = 0, column =1)
        self.runButton.grid(row=1, column=1, sticky=NSEW, columnspan=2)

    def run_attacks(self):
        #TODO make this function actually do things
        var = "This is just a test change this later"



####### Begin main program #######
root = Tk()
m = MainWindow(root)
root.mainloop()