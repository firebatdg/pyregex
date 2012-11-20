
from Container import *

class Or(Container):

    def __init__(self, cont1, cont2):
        self.start = cont1.start
        for c in cont2.start.connections:
            start.connections.append(c)
        cont1.end.accepting = False
        cont2.end.accepting = False
        self.end = State(True)
        cont1.end.connections.append(Link(self.end,""))
        cont2.end.connections.append(Link(self.end,""))

