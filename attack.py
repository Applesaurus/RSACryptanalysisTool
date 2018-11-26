import json, re

class attack:
    attackName = ""
    groupName = ""
    whichArgs = [False, False, False, False] #whichArgs specifies which of the arguments publicexponent, modulus, cyphertext, plaintext an attack takes
    numSets = None #numSets specifies the minimum number of sets of arguments an attack takes

    def __init__(self, atkName):
        #generate attack object from json
        self.attackName = atkName
        with open('AttackData.txt') as json_file:
            attackData = json.load(json_file)
            for i in attackData['attack']:
                if i == atkName:
                    self.groupName = i['group']
                    self.whichArgs = i['Args']
                    self.numSets = i['Sets']


    def list_from_group(self, groups, exclusions):
        #generate the list of attack objects when given a list of groups and a list of attacks to exlcude
        attackList = []
        with open('AttackData.txt') as json_file:
            attackData = json.load(json_file)
            for i in attackData['attack']:
                for group in groups:
                    if group == i['group']:
                        attackList = self.append_attack(attackList, i, exclusions)
        return attackList

    def append_attack(attackList, attackName, exclusions):

        for excludedAttack in exclusions:
            if attackName == excludedAttack:
                return attackList
        attackList.append(attack(attackName));
        return attackList
