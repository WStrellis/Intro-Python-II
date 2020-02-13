
from src.player import Player
from src.item import Item
from src.room_data import rooms


def test_on_take():
    p = Player('Ulrich', rooms['outside'])
    sword = Item('Sword', 'A sharp steel sword used to stab things.')
    msg = sword.on_take(p)
    assert msg == '*** Ulrich picked up the Sword. ***'


def test_on_drop():
    p = Player('Ulrich', rooms['outside'])
    sword = Item('Sword', 'A sharp steel sword used to stab things.')
    msg = sword.on_drop(p)
    assert msg == '*** Ulrich dropped the Sword. ***'
