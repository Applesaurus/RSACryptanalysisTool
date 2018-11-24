from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

"""
A class for the creation and running of the Main GUI Window and its functions.
"""
class MainWindow:

    """
    A method that, upon creation of a MainWindow object, creates all the buttons, labels,
    and checkButtons for the GUI to function
    """
    def __init__(self, master):
        #Set title on title bar
        master.title("RSA Cryptanalysis Tool")

        #Create Menubar and composite menus
        menubar = Menu(master)
        fileMenu = Menu(menubar, tearoff=0)
        editMenu = Menu(menubar, tearoff=0)
        helpMenu = Menu(menubar, tearoff=0)

        #Add composite menu items to proper menubar slot
        menubar.add_cascade(label="File", menu = fileMenu)
        menubar.add_cascade(label="Edit",menu = editMenu)
        menubar.add_cascade(label="Help", menu = helpMenu)
        fileMenu.add_command(label="Exit", command = self.closeWindow)
        editMenu.add_command(label="Change Attack Directory", command = self.changeDirectory)
        helpMenu.add_command(label="About", command = self.displayAbout)
        helpMenu.add_command(label="Help", command = self.displayHelp)

        #Add the final menubar
        master.config(menu=menubar)

        #Create attackFrame to add attack selection widgets
        attackFrame = Frame(master)

        #Create int variables to bind to checkButton widgets. 0 denotes unchecked and 1 denotes checked
        self.isCheckedGroup1 = IntVar()
        self.isCheckedGroup2 = IntVar()
        self.isCheckedAttack1 = IntVar()
        self.isCheckedAttack2 = IntVar()
        self.isCheckedMem = IntVar()
        self.isCheckedTime = IntVar()

        #Add checkboxes for groups of attacks as well as attacks in attack frame
        self.group1Check = ttk.Checkbutton(attackFrame, text = "Group 1",variable=self.isCheckedGroup1)
        self.group2Check = ttk.Checkbutton(attackFrame, text = "Group 2",variable=self.isCheckedGroup2)
        self.attack1 = ttk.Checkbutton(attackFrame, text = "attack 1", variable=self.isCheckedAttack1)
        self.attack2 = ttk.Checkbutton(attackFrame, text = "attack 2",variable=self.isCheckedAttack2)

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
        self.memChkButton = ttk.Checkbutton(constraintFrame, text = "Amount of memory per attack:", variable= self.isCheckedMem)
        self.memChkButton.grid(row = 0, column=0)
        self.memTxtBox = ttk.Entry(constraintFrame)
        self.memTxtBox.grid(row = 0, column=2)

        #Add checkbox, label, and entry field for time constraint specification
        self.timeChkButton = ttk.Checkbutton(constraintFrame, text = "Amount of time per attack:", variable= self.isCheckedTime)
        self.timeChkButton.grid(row = 1, column=0, sticky=W)
        self.timeTxtBox = ttk.Entry(constraintFrame)
        self.timeTxtBox.grid(row=1, column=2)


        #Create run button for running selected attacks
        self.runButton = ttk.Button(master, text="Run", command = self.runAttacks)

        #Add frames and run button to mainwindow
        attackFrame.grid(column = 0)
        constraintFrame.grid(row = 0, column =1)
        self.runButton.grid(row=1, column=1, sticky=NSEW)


    """
    Generates and runs a bash command based on the current GUI state
    """
    def runAttacks(self):
        #TODO make this function actually do things
        var = "This is just a test change this later"

    """
    TODO Document this method
    """
    def changeDirectory(self):
        #TODO make this do stuff
        var = 0


    """
    TODO Document this method
    """
    def displayHelp(self):
        #TODO make this do stuff
        var = 0



    """
    TODO Document this method
    """
    def displayAbout(self):
        #TODO make this do stuff
        var = 0

    """
    A simple wrapper method to allow the program to close without
    closing during initialization
    """
    def closeWindow(self):
        sys.exit()


####### Begin main program #######
root = Tk()
m = MainWindow(root)
root.resizable(False, False )
root.mainloop()