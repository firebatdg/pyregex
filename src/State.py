from Link import *

class State:

    def __init__(self, accepting=False):
        self.connections=[]
        self.accepting = accepting

    def addLink(self, node, value):
        self.connections.append(Link(node,value))

