# python modules
import textwrap

# app modules
from src.player import Player
from src.room_data import rooms
from src.item import Item


MOVE_DIRS = ['n', 's', 'e', 'w']

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']


# Create items
sword = Item('Sword', 'A sharp steel sword used to stab things.')
# add items to rooms
rooms['outside'].add_item(sword)

#
# Main


def main():
    print(f"{'*'*14}\nAdventure Game\n{'*' * 14}")
    # Make a new player object that is currently in the 'outside' room.
    pName = input('What is your character\'s name? ')
    player = Player(pName, rooms['outside'])
    # start game loop
    play_game(player)


def move_player(direction: str, player):
    # check if there is another room in the specified direction
    has_next_room = player.current_room.get_adjacent_room(direction)
    if has_next_room:
        # if yes, move player to that room
        player.current_room = has_next_room
        print(f"\n{player.name} moves to {has_next_room.name}")
    # if no, print error message
    else:
        print(f"\n*** {player.name} cannot move in that direction. ***")


def show_current_location(p):
    des = textwrap.wrap(p.current_room.description)

    # * Prints the current room name
    print(f"\n-- {p.name} --\nLocation: {p.current_room.name}\n")
    # * Prints the current description
    for i in des:
        print(i)

    print(f"""\nAvailable Items:\n""")
    for i in p.current_room.items:
        print(f"{i.name} - {i.description}")


def play_game(p):
    is_running = True

    while is_running:
        show_current_location(p)
        # * Waits for user input and decides what to do.
        action = input('\n~~~> ')

       # If the user enters a cardinal direction, attempt to move to the room there.
        if action.lower() in MOVE_DIRS:
            move_player(action, p)
        # If the user enters "q", quit the game.
        elif type(action) == str and action.lower() == 'q':
            print(f"\nGoodbye, {p.name}")
            is_running = False
        else:
            print('*** Invalid Command ***')


if __name__ == '__main__':
    main()
