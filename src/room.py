# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = [Item(item) for item in items]
        self.n = None
        self.s = None
        self.e = None
        self.w = None

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"Room({self.name})"

    def assign_room(self, direction, room):
        opposite_direction = {
            's': 'n',
            'n': 's',
            'w': 'e',
            'e': 'w'
        }
        setattr(self, direction, room)
        setattr(room, opposite_direction[direction], self)

    def get_room(self, direction):
        return self[direction]

    def get_description(self):
        return self.description

    def __contains__(self, item):
        for i in self.items:
            if str(i) == item:
                return True

    # def remove_item(self, item):
    #     item_location = 0
    #     for index in range(len(self.items)):
