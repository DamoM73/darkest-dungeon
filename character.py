class Character:
    def __init__(self, name):
        # initialises the character object
        self.name = name
        self.description = None
        self.conversation = None

    def describe(self):
        # sends a description of the character to the terminal
        return f"{self.name} is here, {self.description}"

    def talk(self):
        # send converstation to the terminal
        if self.conversation is not None:
            return f"{self.name}: {self.conversation}"
        else:
            return f"{self.name} doesn't want to talk to you"

    def hug(self):
        # the character responds to a hug
        return f"{self.name} doesn't want to hug you"

    def fight(self, item):
        # the character response to a threat
        return (f"{self.name} doesn't want to fight you", True)


class Friend(Character):
    def __init__(self, name):
        # initialise the Friend object by calling the character initialise
        super().__init__(name)

    def hug(self):
        # the friend responds to a hug
        return f"{self.name} hugs you back."


class Enemy(Character):

    num_of_enemy = 0

    def __init__(self, name):
        # initialise the Enemy object by calling the character initialise
        super().__init__(name)
        self.weakness = None
        Enemy.num_of_enemy += 1

    def fight(self, item):
        if item != self.weakness:
            return (f"{self.name} crushes you. Puny adventurer", False)
        Enemy.num_of_enemy -= 1
        return (f"You strike {self.name} down with {item}.", True)

    def get_num_of_enemy():
        return Enemy.num_of_enemy
