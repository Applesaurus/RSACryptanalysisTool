from __future__ import print_function
import os, pkgutil, sys, json, re


## Written by Jackie Bowers

class update:

    attackDir = "/Users/jackie/Desktop/pythontest"

    def __init__(self, directory):
        self.attackDir = directory

    def loadModules(self, dirname):
        #dynamically load all python modules from the attack directory and return them in a list
        moduleList = []
        for importer, package_name, _ in pkgutil.iter_modules([dirname]):
            full_package_name = '%s.%s' % (dirname, package_name)
            if full_package_name not in sys.modules:
                module = importer.find_module(package_name).load_module(full_package_name)
                moduleList.append(module)
        return moduleList

    def runUpdate(self):
        #run the identify function on all modules in the attack directory
        #if it works, add the returned identifiers in json format to attackData.txt
        moduleList = self.loadModules(self.attackDir)
        badModList = ""
        identifier = {}
        for module in moduleList:
            try:
                identifier = module.identify()
                with open('attackData.txt', 'w') as file:
                    json.dump(identifier, file)
            except:
                #modules that could not be called properly should have their names stored seperately
                with open ('unloadedAttacks.txt', 'w') as file:
                    badModList += '\n%s' % str(module)
                    file.write(badModList)

    def list(group=None):
        #list all attacks saved in AttackData.txt
        #if not group:
        with open('AttackData.txt') as json_file:
            attackData = json.load(json_file)
            for i in attackData["attack"]:
                print(i[0], end='')
        print('\n')
