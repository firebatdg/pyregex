
from Container import *

class Or(OneOrMore):

    def __init__(self, cont1):
        self.start = cont1.start
        self.end = cont1.end
        self.start.connections.append(Link(self.end,""))

