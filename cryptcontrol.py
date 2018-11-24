import getopt, sys, re, attack, attackrunner


def main():
    try:  # make sure that no nonexistent options are specified
        opts, args = getopt.getopt(sys.argv[1:], "hlua:g:e:t:m:",
                                   ["help", "list", "update", "attacks", "group", "exclude", "time", "memory"])
    except getopt.GetoptError as err:
        # if nonexistent options specified, print help information and exit
        usage()
        sys.exit(2)
    attackArguments = []
    objList = []
    time = ''
    memory = ''
    exclusionList = []
    for opt, args in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        elif opt in ('-l', '--list'):
            # call update
            if args:
                # listthings(args)
            else:
                #listthings()
        # listthings
        elif opt in ('-u', '--update'):
        # call update
        elif opt in ('-a', '--attack', '-g', '-group'):
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
        else:
            usage()
            sys.exit(2)

        if groups:
                objList = attack.list_from_groups(attackArguments, exclusionList)
        if objList:
            # if objList is either a list of groups are a list of attacks, -a or -g must have been specified indicating that an attack should run
                attackrunner(objList, time, memory, exclusionList)



def usage():
    print('help goes here')
