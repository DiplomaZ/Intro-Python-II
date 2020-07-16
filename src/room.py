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
        return self.description.rstrip()

    def __contains__(self, item):
        for i in self.items:
            if str(i) == item:
                return True

    def remove_item(self, item: str):

        for index in range(len(self.items)):
            print(f"currently in index {index}")

            if str(self.items[index]) == item:
                item_location = index
                break
            # if(item.upper() == str(self.items[index]).upper()):
        # print(f"tasty times tasty tastes {self.items.index(item)}")
        self.items[0].on_take()
        print(f"items before: {self.items}")
        print(item_location)
        self.items = self.items[0:item_location] + \
            self.items[item_location+1:]
        print(f"items after: {self.items}")

    def add_item(self, item: str):
        item = Item(item)
        self.items.append(item)
        item.on_drop()

    def __eq__(self, value):
        return self.name == value
