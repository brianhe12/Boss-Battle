import random
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Initalize Everything
class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic", "Heal"]



# Will generate and return random damage between atkl and atkh
    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

# Will generate and return random spell damage between mgl and mgh
    def generate_spell_damage(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl,mgh)

# Allows Person to take damage, HP not allowed to be under 0
    def take_damage(self,dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0
          # print(bcolors.FAIL + bcolors.BOLD + "Game Over. You have Died" + bcolors.ENDC)
        return self.hp

# Get Functions
    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    # Reduce MP when we use spells
    def reduce_mp(self, cost):
        self.mp = self.mp - cost

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print("Choose your Action!")
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

    def choose_spell(self):
        i = 1
        print("Magic")
        for spell in self.magic:
            print(str(i) + ":", spell["name"], "(cost:", str(spell["cost"]) + ")")
            i += 1
    def heal(self):
        health = random.randrange(13,40)
        mana = random.randrange(4,8)
        self.hp = self.hp + health
        self.mp = self.mp + mana
        print("Healed:", health, "points and", mana, "Mana")

    def enemy_heal(self):
        health = random.randrange(45,60)
        self.hp = self.hp + health
        print("Enemy Regenerated:", health, "points")








