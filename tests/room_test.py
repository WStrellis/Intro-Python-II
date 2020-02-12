
from src.room import Room

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


def test_has_attributes():
    global testRoom
    room = Room(**testRoom)
    assert room.name == testRoom["name"]
    assert room.description == testRoom["description"]
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


def test_should_return_basicRoom():
    global testRoom
    t2 = testRoom.copy()
    t2.update({'s_to': basicRoom})
    room = Room(**t2)
    assert room.s_to == basicRoom
    assert room.get_adjacent_room('s') == basicRoom
