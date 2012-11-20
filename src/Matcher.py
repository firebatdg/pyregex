from State import *
from Link import *

class Matcher:

    def __init__(self, initState, word):
        self.initState = initState
        self.activeNodes = []
        self.word = word
        self.currentChar = None

    def searchMatch(self, word):
        self.setActiveNode(self.initState)
        while len(word) != 0:
            self.currentChar = word[0]
            word = word[1:]
            self.getPossiblePaths()
            if len(self.activeNodes) == 0:
                return False
        if self.isAcceptingState():
            return True
        else:
            return False

    def getPossiblePaths (self):
        self.getEpsilons(self.activeNodes)
        tempActiveNodes = self.activeNodes
        self.activeNodes = []
        for state in tempActiveNodes:
            for link in state.connections:
                if link.value == self.currentChar or link.value=="":
                    self.setActiveNode(link.state)
        
    
    def getEpsilons(self, newNodes):
        tempNewNodes = []
        for state in newNodes:
            for link in state.connections:
                if link.value=="":
                    tempNewNodes.append(link.state)
                    self.setActiveNode(link.state)
        if len(newNodes) == 0:
            return
        newNodes = self.getEpsilons(tempNewNodes)
        

    def isAcceptingState(self):
        for state in self.activeNodes:
            if state.accepting:
                return True
        return False

    def setActiveNode(self, state):
        if state not in self.activeNodes:
            self.activeNodes.append(state)

