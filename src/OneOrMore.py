
from Container import *

class Or(OneOrMore):

    def __init__(self, cont1):
        cont1.end.connections.append(Link(cont1.start,""))
        self.start = cont1.start
        self.end = cont1.end

