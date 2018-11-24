import getopt, sys, re

def main():
    attackArguments = []
    objList = []
    time = ''
    memory = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hlua:g:e:t:m:", ["help", "list", "update", "attacks", "group", "exclude", "time", "memory"])
    except getopt.GetoptError as err:
        # print help information and exit
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for opts, args in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        elif opt in ('-l', '--list'):
            #call update
            if args:
               #listthings(args)
            else:
               #listthings
        elif opt in ('-u', '--update'):
            #call update
        elif opt in ('-a', '--attack', '-g', '-group'):
            arguments = re.split(',',args)
            elif opt in ("-e", "--exclusions"):
               attackArguments = re.split(',',args)
            for i in range (0 len(attackArguments):
                   if opt in ('-a', '--attack'):
                       objList[i] = attack.getAttackObj(attackArguments[i])
                   else:
                       objList[i] = group.getGroupObj(attackArguments[i])
        elif opt in ('-e', '--exclusions'):
            exclusionList = re.split(',',args)
        elif opt in ('-t', '--time'):
            time = args
        elif opt in ('-m', '--memory'):
            memory = args
        else:
            usage()
            sys.exit(2)

    if objList:
        attackrunner(objList,time,memory,exclusions)

