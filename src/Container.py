
from State import *
from Link import *

class Container:

    def __init__(self,string):
        s = State()
        e = State(True)
        s.addLink(e,string)
        self.start = s
        self.end = e



