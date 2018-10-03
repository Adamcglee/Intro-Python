from room import Room
from player import Player

class Item:
    def __init__(self, name):
        self.name = name
    def takeItem(self, player):
            player.items.append(self)
            player.currentRoom.items.remove(self)
    def dropItem(self, player):
            player.items.remove(self)
            player.currentRoom.items.append(self)