class Room:
    def __init__(self, room_name):
        # initialises the room object
        self.name = room_name.lower()
        self.description = None
        self.linked_rooms = {}
        self.inhabitant = None
        self.item = None

    def describe(self):
        # sends a description of the room to the terminal
        text = f"You are in the {self.name}"
        text += "\n" + self.description
        if self.inhabitant is not None:
            text += "\n" + self.inhabitant.describe()
        if self.item is not None:
            text += "\n" + self.item.describe()
        for direction in self.linked_rooms.keys():
            text += (
                "\n" + f"To the {direction} is the {self.linked_rooms[direction].name}"
            )

        return text

    def link_rooms(self, room, direction):
        # links the provided room, in the provided direction
        self.linked_rooms[direction.lower()] = room

    def move(self, direction):
        # returns the room linked in the given direction
        if direction in self.linked_rooms.keys():
            return (f"You travel {direction}", self.linked_rooms[direction])
        else:
            return ("You can't go that way", self)
