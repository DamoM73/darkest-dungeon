from room import Room
from character import Enemy, Friend
from item import Item
from console import UI

ui = UI()

# create rooms
cavern = Room("Cavern")
cavern.description = (
    "A room so big that the light of your torch doesn’t reach the walls."
)

armoury = Room("Armoury")
armoury.description = (
    "The walls are lined with racks that once held weapons and armour."
)

lab = Room("Laboratory")
lab.description = (
    "A strange odour hangs in a room filled with unknownable contraptions."
)

# link rooms
cavern.link_rooms(armoury, "south")
armoury.link_rooms(cavern, "north")
armoury.link_rooms(lab, "east")
lab.link_rooms(armoury, "west")

# create characters
ugine = Enemy("Ugine")
ugine.description = "a huge troll with rotting teeth."
ugine.weakness = "cheese"

nigel = Friend("Nigel")
nigel.description = "a burly dwarf with golden bead in woven through his beard."
nigel.conversation = "Well youngan, what are you doing here?"

# add characters to rooms
armoury.inhabitant = ugine
lab.inhabitant = nigel

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
    ui.display_description(current_room.describe())

    command = input("> ").lower()

    # move
    if command in ["north", "south", "east", "west"]:
        descript, current_room = current_room.move(command)
        ui.display_action(descript)
    elif command == "talk":
        if current_room.inhabitant is not None:
            ui.display_action(current_room.inhabitant.talk())
        else:
            ui.display_action("There is no one here to talk to")
    elif command == "hug":
        if current_room.inhabitant is not None:
            ui.display_action(current_room.inhabitant.hug())
        else:
            ui.display_action("There is no one here to hug")
    elif command == "fight":
        if current_room.inhabitant is not None:
            weapon = input("What will you fight with? > ").lower()
            available_weapons = [item.name for item in backpack]
            if weapon in available_weapons:
                fight_descript, survive = current_room.inhabitant.fight(weapon)
                if survive:
                    current_room.inhabitant = None
                    if Enemy.num_of_enemy == 0:
                        fight_descript += (
                            "\nYou have slain the enemy. You are victorious!"
                        )
                        running = False
                else:
                    running = False
                ui.display_action(fight_descript)
            else:
                ui.display_action(
                    f"You don't have {weapon}\n{current_room.inhabitant.name} strikes you down."
                )
                running = False
        else:
            ui.display_action("There is no one here to fight")
    elif command == "take":
        if current_room.item is not None:
            backpack.append(current_room.item)
            ui.display_action(f"You put {current_room.item.name} into your backpack")
            current_room.item = None
        else:
            ui.display_action("There is nothing here to take")
    elif command == "backpack":
        if not backpack:
            ui.display_action("It is empty")
        else:
            contents = "You have:"
            for item in backpack:
                contents += "\n" + f"- {item.name.capitalize()}"

    elif command == "help":
        ui.display_action(
            "Type which direction you wish to move,\nor use one of these commands:\n- Talk\n- Fight\n- Hug\n- Take\n- Backpack\n- quit"
        )
    elif command == "quit":
        running = False
    else:
        ui.display_action("Enter 'help' for list of commands")
    """
    if running:
        input("\nPress <Enter> to continue")"""

ui.display_action("Thank you for playing Darkest Dungeon")
