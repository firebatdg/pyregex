from State import *

class Link:
    def __init__(self, state, value):
        self.state = state
        self.value = value

    def canUse(self, val):
        return val == self.value

    def __str__(self):
        return "(%s) -> (%s)" % (self.value, self.state)

    def __repr__(self):
        return self.__str__()
