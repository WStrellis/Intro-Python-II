# python modules
import textwrap
import re

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
    has_next_room = getattr(player.current_room, f'{direction}_to', None)

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

    print(f"""\nItems In Room:\n""")
    for i in p.current_room.items:
        print(f"{i.name} - {i.description}")


def take_item(p, a):
    # check if item item is in room
    room_item = includes(p.current_room.items, a[1])
    # if yes add to p inventory and remove from room
    if room_item:
        p.current_room.remove_item(room_item)
        p.add_item(room_item)
        print('\n' + room_item.on_take(p))
    # if no show err
    else:
        print(f"\nThere is not a {a[1]} in this room.")


def drop_item(p, a):
    # check if item item is in player's inventory
    p_item = includes(p.items, a[1])
    # if yes add to room and remove from p inventory
    if p_item:
        p.drop_item(p_item)
        p.current_room.add_item(p_item)
        print('\n' + p_item.on_drop(p))
    # if no show err
    else:
        print(f"\n{p.name} is not carrying a {a[1]}.")


def includes(arr, s):
    has_s = None
    if len(arr) == 0:
        return has_s
    for i in range(0, len(arr)):
        item = arr[i]
        if getattr(item, 'name_index', None) == s:
            has_s = item
    return has_s


def play_game(p):
    is_running = True

    while is_running:
        show_current_location(p)
        # * Waits for user input and decides what to do.
        action = input('\n~~~> ').lower().split(' ')

        # If the user enters a cardinal direction, attempt to move to the room there.
        if len(action) == 1:
            if action[0] in MOVE_DIRS:
                move_player(action[0], p)
            # If the user enters "q", quit the game.
            elif action[0] == 'q':
                print(f"\nGoodbye, {p.name}")
                is_running = False
            # show players inventory
            elif action[0] in ['i', 'inventory']:
                p.list_items()
            else:
                print('*** Invalid Command ***')
        elif len(action) == 2:
            if action[0] in ['get', 'take']:
                take_item(p, action)
            elif action[0] == 'drop':
                drop_item(p, action)
            else:
                print('*** Invalid Command ***')


if __name__ == '__main__':
    main()
