# Write a class to hold player information, e.g. what room they are in
# currently.

# Player can have a name, items he collects, room he is in

class Player:

    def __init__(self, name):
        self.name = name
        self.items = []
        self.current_room = 'outside'

    def __str__(self):
        str_rep = f"-->> {self.name} is in {self.current_room} with the items :: {self.items} ::<<--"
        return str_rep


