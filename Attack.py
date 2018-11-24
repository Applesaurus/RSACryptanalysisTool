import json

class Attack:
    attackName = ""
    groupName = ""
    whichArgs = [false, false, false, false]
    numSets = None

    def __init__(self, atkName):
        self.attackName = atkName
        with open('AttackData.txt) as json_file:
            attackData = json.load(json_file)
            for i in attackData['attack']:
                if i == atkName:
                    self.groupName = i['group']
                    self.whichArgs = i['Args']
                    self.numSets = i['Sets']


    def ListFromGroup(groups, exclusions)
        with open('AttackData.txt) as json_file:
            attackData = json.load(json_file)
            for i in attackData['attack']:
                for group in groups:
                    if group == i['group']:
                        appendAttack(AttackList,i, exclusions)
        return AttackList

    def appendAttack(AttackList, attack, exclusions)
        for excludedAttack in exclusions:
            if attack == excludedAttack:
                return AttackList
        AttackList.append(Attack(i));
        return AttackList
