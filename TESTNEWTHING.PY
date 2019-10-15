import re

class champ1() :
    def __init__(self,name,ad,ap,armor,mg) :
        self.name = name
        self.AD = ad
        self.AP = ap 
        self.Armor = armor
        self.magicR = mg
    def get_info(self) :
        print('Name : ',self.name)
        print('Attack Damge : ',self.AD)
        print('Abilty power : ',self.AP)
        print('Armor : ',self.Armor)
        print('magicR : ',self.magicR)

c = open('TEST.TXT', 'r+') 
      

champ = []

for index in range(10) :
    read_champ = c.readline()
    champ.append(read_champ)
    champ[index] = champ[index][:-1]

c.close()


f = open('stats.txt', 'r+')

chaplistloop = []

for stats in range(3) :
    read_f = f.readline()
    statlist = read_f.split()
    chaplistloop.append(champ1(champ[stats],statlist[0],statlist[1],statlist[2],statlist[3]))

print(chaplistloop[0].name)
f.close()
