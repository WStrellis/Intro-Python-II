from adv import take_item, drop_item
from src.player import Player
from src.room import Room
from src.item import Item
from src.room_data import rooms


def test_take():
    sword = Item('Sword', 'A sharp sword')
    room = Room('Armoury', "the castle armoury", items=[sword])
    player = Player('Ned', room)

    assert len(room.items) == 1
    assert len(player.items) == 0
    take_item(player, ['take', 'sword'])
    assert len(room.items) == 0
    assert len(player.items) == 1
    assert player.items[0] == sword


def test_drop():
    sword = Item('Sword', 'A sharp sword')
    room = Room('Armoury', "the castle armoury", )
    player = Player('Ned', room, items=[sword])

    assert len(room.items) == 0
    assert len(player.items) == 1
    drop_item(player, ['take', 'sword'])
    assert len(room.items) == 1
    assert room.items[0] == sword
    assert len(player.items) == 0
