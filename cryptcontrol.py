import getopt, sys, re, attack, Update


def main():
    try:  # make sure that no nonexistent options are specified
        opts, args = getopt.getopt(sys.argv[1:], "hlua:g:e:t:m:p:",
                                   ["help", "list", "update", "attacks=", "group=", "exclude=", "time=", "memory=", "parameters="])
    except getopt.GetoptError as err:
        # if nonexistent options specified, print help information and exit
        usage()
        sys.exit(2)
    attackArguments = []
    objList = []
    time = ''
    memory = ''
    exclusionList = []
    groups = False
    for opt, args in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        elif opt in ('-l', '--list'):
             Update.runUpdate()
             if args:
                 Update.list(args)
             else:
                 Update.list()
        elif opt in ('-u', '--update'):
            Update.runUpdate()
        elif opt in ('-a', '--attack', '-g', '--group'):
            attackArguments = re.split(',',args)  # multiple arguments for the same opt should be comma seperated; split them into an array
            for i in range(0, len(attackArguments)):
                if opt in ('-a', '--attack'):
                    objList[i] = attack(attackArguments[i])
                else: groups = True
        elif opt in ('-e', '--exclusions'):
            exclusionList = re.split(',', args)
        elif opt in ('-t', '--time'):
            time = args
        elif opt in ('-m', '--memory'):
            memory = args
        elif opt in ('-p', '--parameters'):
            if re.match('.txt', args):
                #read json
            parameters = re.split(',', args)
        else:
            usage()
            sys.exit(2)

    if groups:
        objList = attack.list_from_groups(attackArguments, exclusionList)
    if objList:
        # if objList is either a list of groups are a list of attacks, -a or -g must have been specified indicating that an attack should run
        attackRunner(objList, time, memory, parameters)



def usage():
    print('help goes here')

if __name__ == "__main__":
    main()
