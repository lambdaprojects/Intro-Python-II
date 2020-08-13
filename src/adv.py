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

# Get the player name
player_name = input("\n Please enter your name: ")
if (len(player_name) == 0 or len(player_name.strip() )== 0):
    player_name = "Darth Vader"

my_smart_player = Player(player_name)

print(f"\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(f"\n         Welcome to the game {player_name}!!")
print(f"\n         >>>>  Let's get started <<<<")
print(f"\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")


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

is_game_on = True


def print_possible_rooms(room):
    print("\n +++++++++ Here are your options for next move! Choose wisely :) +++++++++")
    if (room == 'outside'):
        print("\n <><><>  N -> FOYER  <><><>")
    elif (room == 'foyer'):
        print("\n <><><> \n  N -> OVERLOOK  \n  S -> OUTSIDE  \n  E -> NARROW     \n <><><>")
    elif (room == 'overlook'):
        print("\n <><><> \n  S -> FOYER       \n <><><>")
    elif (room == 'narrow'):
        print("\n <><><> \n  N -> TREASURE  \n  W -> FOYER       \n <><><>")
    elif (room == 'treasure'):
        print("\n <><><> \n  S -> NARROW       \n <><><>")

def get_room_name(room):
    if (room == 'Outside Cave Entrance' or room == 'outside'):
        return 'outside'
    elif (room == 'Foyer'):
        return 'foyer'
    elif (room == 'Grand Overlook'):
        return 'overlook'
    elif (room == 'Narrow Passage'):
        return 'narrow'
    elif (room == 'Treasure Chamber'):
        return 'treasure'

while (is_game_on):
    current_room = get_room_name(my_smart_player.current_room)
    print(f"\n ~~|| You are currently in {current_room}. ||~~")
    print(f"\n ~~|| Room description: {room[current_room].description}. ||~~")
    print_possible_rooms(current_room)
    print("\n \n <><><>  IF YOU ENTER 'Q' or 'q' YOU WILL EXIT THE GAME  <><><>")
    next_move = input("\n What's your next move smarty pal! >> ")
    if (next_move.lower() == 'q'):
        is_game_on = False
        print("\n ***********  Thanks for playing Champ!! *************\n \n")
    elif (next_move.lower() == 'n' and hasattr(room[current_room], 'n_to')):
        print("\n ->->->->-> Great Choice ")
        my_smart_player.set_current_room((room[current_room].n_to).name)
    elif (next_move.lower() == 's' and hasattr(room[current_room], 's_to')):
        print("\n ->->->->-> Go for it!! ")
        my_smart_player.set_current_room((room[current_room].s_to).name)
    elif (next_move.lower() == 'e' and hasattr(room[current_room], 'e_to')):
        print("\n ->->->->-> Wonderful choice!! ")
        my_smart_player.set_current_room((room[current_room].e_to).name)
    elif (next_move.lower() == 'w' and hasattr(room[current_room], 'w_to')):
        print("\n ->->->->-> You chose to go west!! Really?? ")
        my_smart_player.set_current_room((room[current_room].w_to).name) 
    else :
        print("\n  ==================================================================================== ")
        print("  Hey smarty pants!! That's not in your list of choices now.. is it?? Let's try again! ")
        print("  ==================================================================================== \n")
        