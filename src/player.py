class Player:
    def __init__(self, name, current_room,  items=None):
        self.name = name
        self.current_room = current_room
        self.items = items or []

    def add_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)

    def list_items(self) -> str:
        print(f"""\n*** {self.name}'s Inventory ***\n""")
        if len(self.items) == 0:
            print('( Empty )')
        else:
            for i in self.items:
                print(f'{i.name} - {i.description}')
