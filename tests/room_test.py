
from src.room import Room
from src.item import Item
from src.room_data import rooms

testRoom = {
    'name': 'Cave Entrance',
    'description': "A dark and gloomy cave. An underground river runs down the center. Stalactites hang from the ceiling.",
    'n_to': 'Forest',
    's_to': 'Plains',
    'e_to': 'Cave Room 2',
    'w_to': 'Cave Room 3',
}

basicRoom = {
    'name': 'Forest',
    'description': "A lush green forest",
}

sword = Item('Sword', 'A sharp steel sword used to stab things.')


def test_has_attributes():
    global testRoom
    room = Room(**testRoom)
    assert room.name == testRoom["name"]
    assert room.description == testRoom["description"]
    assert room.items == []
    assert room.n_to == testRoom["n_to"]
    assert room.s_to == testRoom["s_to"]
    assert room.e_to == testRoom["e_to"]
    assert room.w_to == testRoom["w_to"]


def test_should_have_None_for_n_to():
    global testRoom
    t2 = testRoom.copy()
    t2.update({'n_to': None})
    room = Room(**t2)
    assert room.n_to == None


def test_add_item():
    sword = Item('Sword', 'A sharp sword')
    r1 = Room('Armoury', "the castle armoury")
    r2 = Room('Forest', "A haunted forest")
    assert len(r1.items) == 0
    assert len(r2.items) == 0
    r1.add_item(sword)
    assert len(r1.items) == 1
    assert r1.items[0] == sword
    assert len(r2.items) == 0


def test_remove_item():
    sword = Item('Sword', 'A sharp sword')
    r1 = Room('Armoury', "the castle armoury", items=[sword])
    assert len(r1.items) == 1
    r1.remove_item(sword)
    assert len(r1.items) == 0
