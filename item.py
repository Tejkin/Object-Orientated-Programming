class Item():

    def __init__(self, item_name):
        self.name = item_name
        self.description = None

    def get_name(self):
        return self.name

    def set_name(self, room_name):
        self.name = room_name

    def get_description(self):
        return self.description

    def set_descrtiption(self, item_description):
        self.description = item_description

    def describe(self):
        print(self.description)

    def get_details(self):
        print(self.name)
        print(self.description)