
from src.room import Room


def test_has_attributes():
    name = 'Cave Entrance'
    des = "You come to a large cave entrance at the bottom of a cliff"
    room = Room(name, des)
    assert room.name == name
    assert room.description == des
