from State import *

class Link:
    def __init__(self, state, value):
        self.state = state
        self.value = value

    def canUse(self, val):
        return val == self.value

