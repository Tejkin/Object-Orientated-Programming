# from character import Character
from character import Enemy

#dave
dave = Enemy("Dave", "A smelly zombie")
dave.describe()
dave.set_conversation("Arghhhhhh...")

dave.talk()

dave.set_weakness("potion")

fight_with = input("What will you fight with? \n")
dave.fight(fight_with)
