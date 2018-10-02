from room import Room
from player import Player

# Declare all the rooms

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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p = Player(room["outside"])
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

playerName = input('Player Name: ')

while True: 
    print(f"{playerName} is currently at the {p.currentRoom.name}") 
    print(p.currentRoom.description)
    cmd = input("What would you like to do? => ")
    print('\n')
    if cmd.upper() == "N" or cmd.upper() == "NORTH":
        if hasattr(p.currentRoom, "n_to"):
            p.currentRoom = p.currentRoom.n_to
        else:
            print("You can't go that way!")
            print('\n')
    elif cmd.upper() == "E" or cmd.upper() == "EAST":
        if hasattr(p.currentRoom, "e_to"):
            p.currentRoom = p.currentRoom.e_to
        else:
            print("You can't go that way!")
            print('\n')
    elif cmd.upper() == "S" or cmd.upper() == "SOUTH":
        if hasattr(p.currentRoom, "s_to"):
            p.currentRoom = p.currentRoom.s_to
        else:
            print("You can't go that way!")
            print('\n')
    elif cmd.upper() == "W" or cmd.upper() == "WEST":
        if hasattr(p.currentRoom, "w_to"):
            p.currentRoom = p.currentRoom.w_to
        else:
            print("You can't go that way!")
            print('\n')
    elif cmd.upper() == "Q" or cmd.upper() == "QUIT":
        break
    else:
        print("That is not a valid command!")
        print('\n')
