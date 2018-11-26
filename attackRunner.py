import datetime, time, multiprocessing, threading, pkgutil, sys, imp, psutil, os, re

class attackRunner:
   attackDir = ""

   def __init__(self, directory):
       self.attackDir = directory

   def start(self, attackList, parameters, timeLimit=None, memoryLimit = None):
      #run the attacks from the attack files
      #first, load the attack file as a module
      #then, create a new process for the attack that can have its memory usage and time managed
      for i in range (0, len(attackList)):
         module = imp.load_source('attackList[i].attackName', '%s/%s.py' % (self.attackDir, attackList[i].attackName)) #for python 2
         attackProcess = multiprocessing.Process(self.finalprep(parameters,module, memoryLimit, timeLimit)) #create process for the attack
         attackProcess.start() #start process
         #attackProcess.shutdown()


   def finalprep(self, parameters, module, memoryLimit=None, timeLimit=None):
       # call launch() from the attack file to run the attack
       #spin off a new thread from the new process to monitor memory usage
       #spin off a new thread to kill the process when time limit is up
       #end checking for time and memory usage if attack is finished (in progress)
       attackThread = threading.Thread(module.launch(parameters))
       memThread = threading.Thread(self.memCheck(memoryLimit))
       timeThread = threading.Thread(self.timeCheck(timeLimit))
       memThreadStop = threading.Event()
       attackThread.start()
       memThread.start()
       timeThread.start()
       #while True:
       #    if not attackThread.isAlive():



   def memCheck(self, memoryLimit):
       #shutdown current process when memory limit reached (in progress)
       checkProc = psutil.Process(os.getpid()).memory_info()

   def timeCheck(self, timeLimit):
       #shutdown current process when time limit reached
       if not timeLimit:
           # timeEnd = timeStart + datetime.timedelta(days=2)
           timetoWait = 172800
       if re.search('d', timeLimit):
           timeLimit = re.sub('d', '', timeLimit)
           timetoWait = int(timeLimit) * 86400
       elif re.search('h', timeLimit):
           timeLimit = re.sub('h', '', timeLimit)
           timetoWait = int(timeLimit) * 3600
       elif re.search('m', timeLimit):
           timeLimit = re.sub('m', '', timeLimit)
           timetoWait = int(timeLimit) * 60
       elif re.search('s', timeLimit):
           timeLimit = re.sub('s', '', timeLimit)
           timetoWait = int(timeLimit)
       time.sleep(timetoWait)
       currentProcess = psutil.Process(os.getpid())
       currentProcess.terminate()
