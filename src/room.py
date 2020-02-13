# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    """A room for the adventure

    Public Attributes:
        name(str) : room name
        description(str) : A description of the room
        items(list): Items in the room
        n_to(str): adjacent room in the N direction. defaults to None
        s_to(str): adjacent room in the S direction. defaults to None
        e_to(str): adjacent room in the E direction. defaults to None
        w_to(str): adjacent room in the W direction. defaults to None


    """

    def __init__(self, name, description, items=None, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.items = items or []
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
