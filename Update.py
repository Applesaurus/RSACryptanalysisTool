import os, pkgutil, sys, json

## Written by Jackie Bowers

class Update:

    attackdir = ""

    def __init__(self, directory):
        self.attackdir = directory

    def loadModules(dirname):
        moduleList = []
        for importer, package_name in pkgutil.iter_modules([dirname]):
            full_package_name = '%s.%s' % (dirname, package_name)
            if full_package_name not in sys.modules:
                module = importer.find_module(package_name).load_module(full_package_name)
                moduleList.append(module)
        return moduleList

    def runUpdate(self):
        moduleList = self.loadModules(attackdir)
        identifier = {}
        for module in moduleList:
            try:
                identifier = module.identify()
                with open('attackData.txt', 'w') as file:
                    json.dump(identifier, file)
            except:
                with open ('unloadedAttacks.txt', 'w') as file:
                    print("IGNORE ME") #json.dump(module, file)

    def list(group=""):
        if not group:
            with open('AttackData.txt') as json_file:
                attackData = json.load(json_file)
                for i in attackData['attack']:
                    print(p['attackName'])
