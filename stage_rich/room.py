from rich import print
from rich.panel import Panel

class Room():
    
    def __init__(self,room_name):
        # initialises the room object
        self.name = room_name.lower()
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        
    def describe(self):
        # sends a description of the room to the terminal
        description = ""
        description += f"You are in the {self.name}."
        description += f"\n{self.description}"
        if self.character is not None:
            description += f"\n{self.character.describe()}"
        if self.item is not None:
            description += f"\n{self.item.describe()}"
        description += "\n"    
        for direction in self.linked_rooms.keys():
            description += f"\nTo the {direction} is the {self.linked_rooms[direction].name}"
        print(Panel(description))
    
    def link_rooms(self, room, direction):
        # links the provided room, in the provided direction
        self.linked_rooms[direction.lower()] = room
        
    def move(self, direction):
        # returns the room linked in the given direction
        if direction in self.linked_rooms.keys():
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self