
from src.player import Player
from src.item import Item
from src.room_data import rooms


def test_add_item():
    player = Player('Joe', rooms['outside'])
    sword = Item('Sword', 'A sharp steel sword used to stab things.')

    assert len(player.items) == 0
    player.add_item(sword)
    assert len(player.items) == 1
    assert player.items[0] == sword


def test_remove_item():
    sword = Item('Sword', 'A sharp steel sword used to stab things.')
    player = Player('Joe', rooms['outside'], [sword])

    assert len(player.items) == 1
    assert player.items[0] == sword
    player.drop_item(sword)
    assert len(player.items) == 0
