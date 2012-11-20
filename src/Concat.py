
from Container import *

class Concat(Container):

    def __init__(self, cont1, cont2):
        self.start = cont1.start
        self.end = cont2.end
        for c in cont2.start.connections:
            cont1.end.connections.append(c)
        self.end.accepting = True
        cont1.end.accepting = False
        cont2.connections = []

