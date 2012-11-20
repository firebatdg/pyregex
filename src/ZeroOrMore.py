
from Container import *

class ZeroOrMore(Container):

    def __init__(self, cont1):
        self.start = cont1.start
        self.end = State(True)
        cont1.end.accepting = False
        cont1.end.connections.append(Link(self.start,""))
        self.start.connections.append(Link(self.end,""))

