from room import Room
from character import Enemy, Friend
from item import Item
from rich import print


# create rooms
cavern = Room("Cavern")
cavern.description = ("A room so big that the light of your torch doesn’t reach the walls.")

armoury = Room("Armoury")
armoury.description = ("The walls are lined with racks that once held weapons and armour.")

lab = Room("Laboratory")
lab.description = ("A strange odour hangs in a room filled with unknownable contraptions.")

# link rooms
cavern.link_rooms(armoury,"south")
armoury.link_rooms(cavern,"north")
armoury.link_rooms(lab,"east")
lab.link_rooms(armoury,"west")

# create characters
ugine = Enemy("Ugine")
ugine.description = "a huge troll with rotting teeth."
ugine.weakness = "cheese"

nigel = Friend("Nigel")
nigel.description = "a burly dwarf with golden bead in woven through his beard."
nigel.conversation = "Well youngan, what are you doing here?"

# add characters to rooms
armoury.character = ugine
lab.character = nigel

# create items
cheese = Item("Cheese")
cheese.description = "super smelly"

chair = Item("Chair")
chair.description = "designed to be sat on"

elmo = Item("Elmo")
elmo.description = "wanting to be tickled"

# add items to rooms
cavern.item = chair
armoury.item = elmo
lab.item = cheese

# initialise variables
running = True
current_room = cavern
backpack = []

# ----- MAIN LOOP -----
while running:
    current_room.describe()
    
    command = input("> ").lower()
    
    # move
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
        print(f"[magenta]You travel {command}[/magenta]")
    # talk
    elif command == "talk":
        if current_room.character is not None:
            current_room.character.talk()
        else:
            print("[magenta]There is no one here to talk to[/magenta]")
    # hug
    elif command == "hug":
        if current_room.character is not None:
            current_room.character.hug()
        else:
            print("[magenta]There is no one here to hug[/magenta]")
    # fight
    elif command== "fight":
        if current_room.character is not None:
            weapon = input("[magenta]What will you fight with? > [/magenta]").lower()
            available_weapons = []
            for item in backpack:
                available_weapons.append(item.name)
            if weapon in available_weapons:
                if current_room.character.fight(weapon):
                    current_room.character = None
                    if Enemy.num_of_enemy == 0:
                        print("[magenta]You have slain the enemy. You are victorious![/magenta]")
                        running = False
                else:
                    running = False
            else:
                print(f"[magenta]You don't have {weapon}[/magenta]")
                print(f"[magenta]{current_room.character.name} strikes you down.[/magenta]")
                running = False
        else:
            print("[magenta]There is no one here to fight[/magenta]")
    # take
    elif command == "take":
        if current_room.item is not None:
            backpack.append(current_room.item)
            print(f"[magenta]You put {current_room.item.name} into your backpack[/magenta]")
            current_room.item = None
        else:
            print("[magenta]There is nothing here to take[/magenta]")
    # backpack
    elif command == "backpack":
        if backpack == []:
            print("[magenta]It is empty[/magenta]")
        else:
            print("[magenta]You have:[magenta]")
            for item in backpack:
                print(f"[magenta]- {item.name.capitalize()}[/magenta]")
    # help
    elif command == "help":
        print("[magenta]Type which direction you wish to move,[/magenta]")
        print("[magenta]or use one of these commands:[/magenta]")
        print("[magenta]- Talk[/magenta]")
        print("[magenta]- Fight[/magenta]")
        print("[magenta]- Hug[/magenta]")
        print("[magenta]- Take[/magenta]")
        print("[magenta]- Backpack[/magenta]")
    # quit
    elif command == "quit":
        running = False
    # incorrect command
    else:
        print("[magenta]Enter 'help' for list of commands[/magenta]")
    
print("[magenta]Thank you for playing Darkest Dungeon[/magenta]")