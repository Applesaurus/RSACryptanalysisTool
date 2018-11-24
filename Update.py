import os, pkgutil, sys, json

class Update:

   attackdir = ""

   def __init(self, dir)
       self.attackdir = dir

   def runUpdate()
       moduleList = loadModules(attackdir)
       identifier = {}
       for module in moduleList:
           try:
               identifier = module.identify()
               with open('attackData.txt', 'w') as file:
                   json.dump(identifier, file)
           except:
               with open ('unloadedAttacks.txt', 'w') as file:
                   #json.dump(module, file)


   def loadModules(dirname):
        moduleList = []
        for importer, package_name, _ in pkgutil.iter_modules([dirname]):
            full_package_name = '%s.%s' % (dirname, package_name)
            if full_package_name not in sys.modules:
                module = importer.find_module(package_name).load_module(full_package_name)
                moduleList.append(module)
        return moduleList

   def list(group="")
        if not group
            with open('AttackData.txt') as json_file:
                attackData = json.load(json_file)
                for i in attackData['attack']
                print(p['attackName'])

