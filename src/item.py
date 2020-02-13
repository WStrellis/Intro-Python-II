class Item:
    """ Items the player can interact with"""

    def __init__(self, name, description):
        self.name = name
        self.name_index = name.lower()
        self.description = description
