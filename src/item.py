
class Item:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return self.__name

    def __repr__(self):
        return f"{self.__name}"

    @property
    def name(self):
        return self.__name

    def on_take(self):
        print(f'You have picked up {self.__name}')

    def on_drop(self):
        print(f'You have dropped {self.__name}')

    def get_name(self):
        return f"{self.__name}"
