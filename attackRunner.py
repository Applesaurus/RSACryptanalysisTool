import datetime, time, multiprocessing, threading, pkgutil, sys, imp

class attackRunner:
   attackDir = "/Users/jackie/Desktop/pythontest"

   def __init__(self, directory):
       self.attackDir = directory

   def start(self, attackList, timeLimit, memoryLimit, parameters):
      for i in range (0, len(attackList)):
         module = imp.load_source('attackList[i].attackName', '%s/%s.py' % (self.attackDir, attackList[i].attackName)) #for python 2
         attackProcess = multiprocessing.Process(module.launch(parameters)) #create process for the attack
         memThread = threading.Thread(self.lauchMemCheck(memoryLimit, attackProcess))
         attackProcess.start() #start process
         memThread.start()
         timeStart = datetime.datetime.now()
         timeEnd = timeStart + datetime.time(timeLimit, 0, 0, 0)

         time.sleep(timeEnd - timeStart)
         attackProcess.shutdown()

   #def loadAttack(self, package_name):

       #full_package_name = '%s.%s' % (self.attackDir, package_name)
       #print(full_package_name)
       #if full_package_name not in sys.modules:
       #    print(full_package_name)
    #   importer = pkgutil.get_loader(full_package_name)
        #   print(importer)
       #    module = importer.find_module(package_name).load_module(full_package_name)
      # return module

   #def launchMemCheck(self):
