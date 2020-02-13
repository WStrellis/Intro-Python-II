class Item:
    """ Items the player can interact with"""

    def __init__(self, name, description):
        self.name = name
        self.name_index = name.lower()
        self.description = description

    def on_take(self, p) -> str:
        return f"*** {p.name} picked up the {self.name}. ***"

    def on_drop(self, p) -> str:
        return f"*** {p.name} dropped the {self.name}. ***"
