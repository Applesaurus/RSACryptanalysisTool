from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox


"""
A class for the creation and running of the Main GUI Window and its functions.
"""
class MainWindow:

    """
    A method that, upon creation of a MainWindow object, creates all the buttons, labels,
    and checkButtons necessary for the GUI to function
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
        self.group1Check = ttk.Checkbutton(attackFrame, text = "Group 1",variable=self.isCheckedGroup1, command = self.checkBoxHandling)
        self.group2Check = ttk.Checkbutton(attackFrame, text = "Group 2",variable=self.isCheckedGroup2, command = self.checkBoxHandling)
        self.attack1Check = ttk.Checkbutton(attackFrame, text ="attack 1", variable=self.isCheckedAttack1, command = self.checkBoxHandling)
        self.attack2Check = ttk.Checkbutton(attackFrame, text ="attack 2", variable=self.isCheckedAttack2, command = self.checkBoxHandling)

        #Add large font title label
        self.titleLabel = ttk.Label( attackFrame, text ="RSA Cryptanalysis Tool", font=24)

        #Position title label and checkboxes in attackFrame
        self.titleLabel.grid(row=0, pady=(0,20))
        self.group1Check.grid(row=1,sticky=W, padx=10)
        self.attack1Check.grid(row=2, padx=20, sticky=W)
        self.group2Check.grid(row=3, sticky=W, padx=10)
        self.attack2Check.grid(row=4, padx=20, sticky=W)

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
    Creates a folder select window to allow the user to select
    a new folder to serve as the attack directory.
    """
    def changeDirectory(self):
        #TODO make this do stuff
        folderSelected = filedialog.askdirectory()
        bashString = "RSATool.py -s " + folderSelected

        #TODO figure out the exact wording of the bash command above
        #and add the code to call the main program


    """
    Creates a messagebox displaying information about how to
    use this program. I.e. how to access the different capabilities
    like running attacks with constraints as well as the more
    miscellaneous capabilities such as changing the attack directory.
    """
    def displayHelp(self):
        helpString = "In order to run a number of attacks click the checkbox next " \
                     "to each attack you would like to run and then hit the \"Run\" " \
                     "button. You can run any number of attacks in this way.\n\n" \
                     "Similarly you may run a group of attacks by clicking the checkbox next " \
                     "to the group of attacks you wish to run. Note that you may exclude certain " \
                     "attacks from being run with the group by unchecking the undesired attacks. \n\n" \
                     "You may change the attack directory through the \"Edit\" menu.\n\n" \
                     "You may specify time or memory constraints by clicking the relevant checkbox " \
                     "and entering in the value along with units (s/m/h) or (MB\GB\MiB\GiB)."
        messagebox.showinfo("Help", helpString)



    """
    Creates a messagebox displaying information about the program.
    I.e. what it is, what it does, what it is supposed to be used for.
    """
    def displayAbout(self):
        aboutString = "This program is designed for the cryptanalysis of RSA public key encryption. " \
                      "It includes several attacks by default and is open to expansion by allowing " \
                      "users to import their own attacks. This program is intended for use by anyone " \
                      "attempting to implement RSA in their own project. It is our hope that this tool " \
                      "will help weed out some of the especially bad RSA implementations out there and " \
                      "in the end make the web safer for everyone to use.\n\nThis GUI is included for the convenience " \
                      "of those who are not familiar with a more traditional command line interface. " \
                      "In fact, this GUI is just a hollow shell that generates the necessary Bash commands"  \
                      "to run the command line program with the proper command line arguments."
        messagebox.showinfo("About this program", aboutString)


    """
    A simple wrapper method to allow the program to close without
    closing during initialization
    """
    def closeWindow(self):
        sys.exit()


    """
    This function handles the behaviour of the checkbuttons
    auto selecting and deselecting attacks when their group is clicked
    """
    def checkBoxHandling(self):
        var = 1
        #TODO probably just hardcode this when we get all our attacks


####### Begin main program #######

root = Tk()
mainWindow = MainWindow(root)
root.resizable(False, False)
root.mainloop()