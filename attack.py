import json

class attack:
    attackName = ""
    groupName = ""
    whichArgs = [False, False, False, False]
    numSets = None

    def __init__(self, atkName):
        self.attackName = atkName
        with open('AttackData.txt') as json_file:
            attackData = json.load(json_file)
            for i in attackData['attack']:
                if i == atkName:
                    self.groupName = i['group']
                    self.whichArgs = i['Args']
                    self.numSets = i['Sets']


    def list_from_group(self, groups, exclusions):
        attackList = []
        with open('AttackData.txt') as json_file:
            attackData = json.load(json_file)
            for i in attackData['attack']:
                for group in groups:
                    if group == i['group']:
                        attackList = self.append_attack(attackList, i, exclusions)
        return attackList

    def append_attack(attackList, attack, exclusions):
        for excludedAttack in exclusions:
            if attack == excludedAttack:
                return attackList
        attackList.append(attack(attack));
        return attackList
