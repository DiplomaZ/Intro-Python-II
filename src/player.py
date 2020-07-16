from utils.utils import mapFormatter, three_args_center


class Player:
    def __init__(self, name, room, inventory=[]):
        self.name = name
        self.current_room = room
        self.inventory = inventory

    def __str__(self):
        room = self.current_room
        return f'''\nPlayer: \033[1;32;40m{self.name}\033[0m, currently in room: {self.current_room}\n
        {mapFormatter("Map View:")}
        \n
        {mapFormatter(str(room.n))}\n
        {mapFormatter("|")}\n
        {mapFormatter("|")}\n
        {three_args_center([str(room.w), str(room), str(room.e)])}\n
        {mapFormatter("|")}\n
        {mapFormatter("|")}\n
        {mapFormatter(str(room.s))}\n
        \033[1;32;40m Other info: \033[0m
        \033[1;32;40m Items: \033[0m {', '.join([str(item) for item in room.items])}\n'''

    def get_room(self):
        return self.current_room

    def navigate(self, direction):
        next_room = getattr(self.current_room, direction)
        if not next_room:
            raise ValueError()
        self.current_room = next_room

    def get_item(self, item: str):
        if(item in self.current_room):
            self.inventory += [item]
            print(self.current_room.items)
            self.current_room.remove_item(item)
            print(self.current_room.items)

    def get_inventory(self):
        return self.inventory

    def drop_item(self, item: str):
        if(item in self.inventory):
            print("We found it boss")
            self.current_room.add_item(item)
            self.inventory.remove(item)
