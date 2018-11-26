from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from ttkthemes import themed_tk as tk
from tkinter import filedialog
from tkinter import messagebox
from cryptcontrol import *
from attackRunner import *
import subprocess


"""
A class for the creation and running of the Main GUI Window and its functions.
"""
class MainWindow:

    """
    A method that, upon creation of a MainWindow object, creates all the buttons, labels,
    dropdown menus, and checkButtons necessary for the GUI to function
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
        editMenu.add_command(label="Add Attack", command = self.addAttack)
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
        self.group1Check = ttk.Checkbutton(attackFrame, text = "Stereotyped Message Attacks",variable=self.isCheckedGroup1, takefocus=0)
        self.group2Check = ttk.Checkbutton(attackFrame, text = "Common Plaintext Attacks",variable=self.isCheckedGroup2, takefocus=0)
        self.attack1Check = ttk.Checkbutton(attackFrame, text ="attack 1", variable=self.isCheckedAttack1, takefocus=0)
        self.attack2Check = ttk.Checkbutton(attackFrame, text ="attack 2", variable=self.isCheckedAttack2, takefocus=0)

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
        self.memChkButton = ttk.Checkbutton(constraintFrame, text = "Amount of memory per attack:", variable= self.isCheckedMem, takefocus=0)
        self.memChkButton.grid(row = 0, column=0)
        self.memTxtBox = ttk.Entry(constraintFrame)
        self.memTxtBox.grid(row = 0, column=2)

        #Add checkbox, label, and entry field for time constraint specification
        self.timeChkButton = ttk.Checkbutton(constraintFrame, text = "Amount of time per attack:", variable= self.isCheckedTime, takefocus=0)
        self.timeChkButton.grid(row = 1, column=0, sticky=W)
        self.timeTxtBox = ttk.Entry(constraintFrame)
        self.timeTxtBox.grid(row=1, column=2)

        #Create run button for running selected attacks and pad out the text because the style left justifies and its
        #easier to just pad this one string than change the entire style
        self.runButton = ttk.Button(master, text="                             " \
                                                 "Run Attack(s)", command = self.runAttacks, takefocus=0)

        #Add frames and run button to mainWindow
        bgFrame = Frame(root)
        bgFrame.grid(columnspan=100, rowspan=100, sticky=NSEW)      #Add a blank frame at bottom of all widgets so that everything is a uniform color
        bgFrame.lower()
        attackFrame.grid(row=0, column = 0, sticky=N)
        constraintFrame.grid(row = 0, column =1, pady=(60,70))
        self.runButton.grid(row=2, column=1, sticky=EW)


    """
    Generates and runs a bash command based on the current GUI state
    """
    def runAttacks(self):
        fileSelected = filedialog.askopenfile()
        bashString = "Python cryptcontrol.py"
        subprocess.run(bashString.Split())
        #TODO figure out the right command line arguments to append to above


    """
    Creates a folder select window to allow the user to select
    a new folder to serve as the attack directory.
    """
    def changeDirectory(self):
        folderSelected = filedialog.askdirectory()
        bashString = "Python cryptcontrol.py" + folderSelected
        subprocess.run(bashString.Split())
        #TODO figure out the exact wording of the bash command above


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
                      "In fact, this GUI is just a hollow shell that generates the necessary Bash commands "  \
                      "to run the command line program with the proper command line arguments."
        messagebox.showinfo("About this program", aboutString)


    """
    A simple wrapper method to allow the program to close without
    closing during initialization
    """
    def closeWindow(self):
        sys.exit()


    """
    A method that creates a file select pop up window to allow
    the user to add a new file to the list of available attacks
    """
    def addAttack(self):
        fileSelected = filedialog.askopenfile()
        bashString = "Python cryptcontrol.py"
        subprocess.run(bashString.Split())
        #TODO figure out the command line arguments for the above


####### Begin main program #######

root = tk.ThemedTk()
root.get_themes()
root.set_theme("black")
GUI = MainWindow(root)
root.resizable(False, False)
root.mainloop()