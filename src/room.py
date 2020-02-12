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

    def get_n_to(self) -> str:
        return self.n_to

    def get_s_to(self) -> str:
        return self.s_to

    def get_e_to(self) -> str:
        return self.e_to

    def get_w_to(self) -> str:
        return self.w_to

    def get_adjacent_room(self, direction: str) -> str:
        """Returns the next room in the specified direction or None if there is not a room

        Arguments:
            direction {str} -- [description]

        Returns:
            Room -- An instance of class Room
            or
            None

        """
        adjacent = {'n': self.get_n_to(), 's': self.get_s_to(),
                    'e': self.get_e_to(), 'w': self.get_w_to()}
        return adjacent[direction]
