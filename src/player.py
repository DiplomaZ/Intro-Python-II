class Player:
    def __init__(self, name, room, inventory=[]):
        self.name = name
        self.current_room = room
        self.inventory = inventory

    def __str__(self):
        room = self.current_room
        return f'''Player: {self.name}, currently in room: {self.current_room}
        \t\t\t Map View:
        \n
        \t\t\t\t{room.n}
        \n\t\t\t\t\t|
        \n\t\t\t\t\t|
        \t{room.w}\t------\t{room}\t------\t{room.e}
        \n\t\t\t\t\t|
        \n\t\t\t\t\t|
        \t\t\t\t{room.s}
        Other info:
        Items: {', '.join([str(item) for item in room.items])}'''

    def get_room(self):
        return self.current_room

    def navigate(self, direction):
        next_room = getattr(self.current_room, direction)
        if not next_room:
            raise ValueError()
        self.current_room = next_room
