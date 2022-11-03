from room import Room
from item import Item
from character import Enemy, Friend


##rooms
kitchen = Room("kitchen")
ballroom = Room("ballroom")
dining_hall = Room("dining hall")

kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom.set_description("A dusty ballroom soiled by blood")
dining_hall.set_description("The stench of rotten food covers the long hall")

ballroom.link_room(dining_hall, "east")
dining_hall.link_room(ballroom, "west")
dining_hall.link_room(kitchen, "north")
kitchen.link_room(dining_hall, "south")

## enemies

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Arghhhhhh...")
dave.set_weakness("potion")

dining_hall.set_character(dave)


## friends
bob = Friend("Bob", "A friendly slime")
bob.set_conversation("Blob blob")
bob.set_favourite("hug")
bob.set_favourite("flowers")

kitchen.set_character(bob)

## items
sword = Item("sword")
potion = Item("potion")

sword.set_descrtiption("Rusty chipped sword looted from a fallen soldier")
potion.set_descrtiption("Small potion gleaming with red light")

potion.get_details()

## travelling through rooms
current_room = kitchen

dead = False

while dead == False:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("You can only talk to yourself in this room")
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            fight_with = input("What would you like to fight with? ")
            if inhabitant.fight(fight_with) == False:
                print("You have died")
                dead = True
        else:
            print("There is no one to fight with in this room")

    elif command == "hug":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print(inhabitant.name + " looks at you with disgust")
            if isinstance(inhabitant, Friend):
                inhabitant.hug()
        else:
            print("You can only hug the air in this room..")
    elif command ==  "gift":
        if inhabitant is not None and isinstance(inhabitant, Friend):
            gift = input("What would you like to gift " + inhabitant.name + "? ")
            inhabitant.gift(gift)

