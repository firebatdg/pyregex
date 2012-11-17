from State import *

class Link:
    def __init__(self, node, value):
        self.node = node
        self.value = value

    def canUse(self, val):
        return val == self.value

