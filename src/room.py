# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    """A room for the adventure

    Public Attributes:
        name(str) : room name
        description(str) : A description of the room
        n_to(str): adjacent room in the N direction. defaults to None
        s_to(str): adjacent room in the S direction. defaults to None
        e_to(str): adjacent room in the E direction. defaults to None
        w_to(str): adjacent room in the W direction. defaults to None


    Private Attributes:
        __adjacent_rooms(obj) : used to map direction input to self.x_to properties
    """

    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def get_adjacent_room(self, direction: str):
        """Returns the next room in the specified direction or None if there is not a room

        Arguments:
            direction {str} -- [description]

        Returns:
            Room -- An instance of class Room
            or
            None

        """
        if direction == 'n':
            return self.n_to
        elif direction == 's':
            return self.s_to
        elif direction == 'e':
            return self.e_to
        elif direction == 'w':
            return self.w_to
        else:
            return None
