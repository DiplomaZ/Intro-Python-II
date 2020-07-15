from room import Room
from player import Player
import shutil

# Declare all the rooms


def main():

    room = {
        'outside':  Room("Outside Cave Entrance",
                         "North of you, the cave mount beckons"),

        'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
    passages run north and east."""),

        'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
    into the darkness. Ahead to the north, a light flickers in
    the distance, but there is no way across the chasm."""),

        'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
    to north. The smell of gold permeates the air."""),

        'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
    chamber! Sadly, it has already been completely emptied by
    earlier adventurers. The only exit is to the south."""),
    }

    # Link rooms together

    room['outside'].assign_room('s', room['foyer'])
    room['foyer'].assign_room('s', room['overlook'])
    room['foyer'].assign_room('w', room['narrow'])
    room['overlook'].assign_room('n', room['foyer'])
    room['narrow'].assign_room('s', room['treasure'])
    valid_choices = list('newsqi') + ['inventory']
    print(room)
    # room['narrow'].n_to = room['treasure']
    # room['treasure'].s_to = room['narrow']

    #
    # Main
    #

    # Make a new player object that is currently in the 'outside' room.

    # Write a loop that:
    #
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.

    def sanitize_input(user_input: str, choices: list):
        return user_input in choices

    player = Player('zoe', room['outside'])

    screenTuple = shutil.get_terminal_size()
    screenWidth = screenTuple[0]
    screenHeight = screenTuple[1]

    while True:
        print(player.get_room())
        print(player)
        print(f"width: {screenWidth}, \n height: {screenHeight}")
        user_input = input(
            "Where do you want to go?\n\n\tYou can Travel to the 'n' (North), 's' (South), 'e' (East) and 'w' (West)\n\tYou can also check your inventory by typing 'inventory' or 'i' \n\nType Response Here: ")
        valid_input = sanitize_input(user_input, valid_choices)
        if not valid_input:
            print("Invalid entry. Please try again.")
        if user_input == 'q':
            print('Goodbye, Saruman')
            break

        if user_input == 'i' or user_input == 'inventory':
            # Inventoryyyy
            print("hey uh... nothing here yet. Really sorry...")
            continue

        if user_input == 's':
            player.navigate(user_input)

        try:
            player.navigate(user_input)
        except:
            print("wrooooooooooooooooooooooooooong")


if __name__ == "__main__":
    main()
