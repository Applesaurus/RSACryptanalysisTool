import getopt, sys, re, attack
from update import update
from attackRunner import attackRunner


def main():
    attackDir = "/Users/jackie/Desktop/pythontest"
    updater = update(attackDir)
    runAttack = attackRunner(attackDir)
    try:  # make sure that no nonexistent options are specified
        opts, args = getopt.getopt(sys.argv[1:], "hlua:g:e:t:m:p:s:",
                                   ["help", "list", "update", "attacks=", "group=", "exclude=", "time=", "memory=", "parameters=", "directory="])
    except getopt.GetoptError as err:
        # if nonexistent options specified, print help information and exit
        usage()
        sys.exit(2)
    attackArguments = []
    atkObjList = []
    time = ''
    memory = ''
    exclusionList = []
    groups = False
    for opt, args in opts:
        #handle all options and arguments
        #iterate through opts and handle each option and argument accordingly
        if opt in ('-h', '--help'): #print usage
            usage()
            sys.exit()
        elif opt in ('-l', '--list', '-u', '--update'): #update the stored identifying information for all attack files in the attack directory
            updater.runUpdate()
            if opt in ('-l', '--list'): #list all valid attacks in the attack directory
                if args:
                     updater.list(args)
                else:
                     updater.list()
        elif opt in ('-a', '--attack', '-g', '--group'):
            #use the attack or group names to make a list of attack objects
            #because groups must be checked for exclusions, the full list of attack objects if '-g' is assembled after all opts have been iterated through
            attackArguments = re.split(',', args)  # multiple arguments for the same opt should be comma seperated; split them into an array
            print(attackArguments)
            for i in range(0, len(attackArguments)):
                if opt in ('-a', '--attack'):
                    atkObjList.append(attack.attack(attackArguments[i]))
                else: groups = True
        elif opt in ('-e', '--exclusions'):
            exclusionList = re.split(',', args)
        elif opt in ('-t', '--time'): #specify max time for each attack to run
            time = args
        elif opt in ('-m', '--memory'): #specify max memory each attack allowed to use
            memory = args
        elif opt in ('-p', '--parameters'): #specify parameters in order: publicexponent, modulus, cyphertext, plaintext
            #handle the parameters
            #if re.match('.txt', args):
                #read json
            parameters = re.split(',', args)
        elif opt in ('-s', '--directory'): #change attack directory
            attackDir = args
            updater = update(attackDir)
            runAttack = attackRunner(attackDir)
        else:
            usage()
            sys.exit(2)

    if groups: #create the list of attack objects using the group names and the excluded attacks from the groups
        atkObjList = attack.list_from_groups(attackArguments, exclusionList)
    if atkObjList:
        try:
            runAttack.start(atkObjList, parameters, time, memory)
        except:
            usage()
            sys.exit(2)


def usage():
    print('help goes here')

if __name__ == "__main__":
    main()
