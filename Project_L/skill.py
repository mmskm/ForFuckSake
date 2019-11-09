import stats_manager as champ
class monster():
    def __init__(self,HP,AR,AD,AS,MR,exp):
        self.HP = HP
        self.AD = AD
        self.AS = AS
        self.MR = MR
        self.AR = AR
        self.exp = exp
    def receive_damege(self,dmg):
        dmg = dmg * (1-(self.AR/(100+self.AR)))
        return dmg

def battle(monter,champ):
    t = (monter.HP/(monter.receive_damege(champ.AD)+35))/champ.AS
    champ.HP -= (t*monter.AS)*monter.AD
    
    champ.HP += t*(champ.HPp/5)
    champ.exp_gain(monter.exp)


blue = monster(2100,10,82,0.493,15,115+50)
red = monster(2100,15,82,0.5,10,115+50)
gromp = monster(1800,0,70,1.004,15,115+50)
wolf = monster(1300,10,42,0.625,0,65+50)
wolf1 = monster(450,0,16,1.004,10,25)
wolf2 = monster(450,0,16,1.004,10,25)
Krug  = monster(1250,10,80,0.613,15,100+50)
Krug1  = monster(500,0,25,0.613,0,35)
Krug11  = monster(500,0,25,0.613,0,35)
Krug12  = monster(500,0,25,0.613,0,35)
Krug21  = monster(60,0,17,0.613,0,7)
Krug22  = monster(60,0,17,0.613,0,7)
Krug23  = monster(60,0,17,0.613,0,7)
Krug24  = monster(60,0,17,0.613,0,7)
Krug25  = monster(60,0,17,0.613,0,7)
Krug26  = monster(60,0,17,0.613,0,7)


Garen = champ.define_champ('Jax')
print(Garen.AD)
battle(blue,Garen)
Garen.current_exp += 120
battle(red,Garen)
battle(gromp,Garen)
battle(wolf,Garen)
battle(wolf1,Garen)
battle(wolf2,Garen)
battle(Krug,Garen)
battle(Krug1,Garen)
battle(Krug11,Garen)
battle(Krug12,Garen)
battle(Krug21,Garen)
battle(Krug22,Garen)
battle(Krug23,Garen)
battle(Krug24,Garen)
battle(Krug25,Garen)
battle(Krug26,Garen)

print(Garen.HP)
print(Garen.level)
