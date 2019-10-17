x = open("Project_L/Champ_stats.txt")
champ_list = []
for line in x :
    y = line.split()
    if y[1].isalpha() :
        y[0] = y[0] + ' ' + y[1]
        y.pop(1)
    champ_list.append(y)

class champion ():
    level = 1
    def __init__(self,stats = [0]*19) :
        self.champ = stats.copy()
        self.name = stats[0]
        self.HP = float(stats[1])
        self.HPp = float(stats[2])
        self.HP5 = float(stats[3])
        self.HP5p = float(stats[4])
        self.MP = float(stats[5])
        self.MPp = float(stats[6])
        self.MP5 = float(stats[7])
        self.MP5p = float(stats[8])
        self.AD = float(stats[9])
        self.ADp = float(stats[10])
        self.AS = float(stats[11])
        self.ASp = float(stats[12])
        self.AR = float(stats[13])
        self.ARp = float(stats[14])
        self.MR = float(stats[15])
        self.MRp = float(stats[16])
        self.MS = float(stats[17])
        self.range = float(stats[18])
    def level_up (self,level = 1) :
        if self.level+level <= 18 :
            self.level += level
            self.HP = self.HP + level*self.HPp
            self.HP5 = self.HP5 + level*self.HP5p
            self.MP = self.MP + level*self.MPp
            self.MP5 = self.MP5 + level*self.MP5p
            self.AD = self.AD + level*self.ADp
            self.AS = self.AS * (1 + level*(self.ASp/100))
            self.AR = self.AR + level*self.ARp
            self.MR = self.MR + level*self.MRp
        elif self.level < 18 :
            self.level_up(18-self.level)
    def print_stats(self):
        print('''Champion:{}
        Health:{}
        Mana:{}
        AD:{}
        AS:{}
        AR:{}
        MR:{}
        '''.format(self.name,self.HP,self.MP,self.AD,self.AS,self.AR,self.MR))
    def set_level(self,level=1):
        self.level = 1
        self.__init__(self.champ)
        self.level_up(level-1)
def search_champ(name):
    for a in champ_list :
        if name in a :
            return champ_list.index(a)
            break
def define_champ(name):
    return champion(champ_list[search_champ(name)])

champ_class = []
for champ in champ_list :
    champ_class.append(champion(champ))

best_champ = champion()
for index in range(5) :
    cDps = 0
    for champs in champ_class :
        champs.set_level(1)
        dps = champs.AD/champs.AS
        if dps > cDps :
            best_champ = champs
            cDps = dps
    else :
        print(cDps)
        best_champ.print_stats()
        champ_class.pop(champ_class.index(best_champ))

