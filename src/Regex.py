import sys
import re
import datetime
from State import *
from Link import *
from Matcher import *
from Concat import *
from Container import *
from Or import *
from ZeroOrOne import *
from ZeroOrMore import *
from OneOrMore import *

class Regex:

    def __init__(self, regex_str):
        self.regex_str = regex_str
        self.nfa = None
        self.init_nfa()

    def init_nfa(self):
        expr = self.get_postfix(self.regex_str)

    def add_concatenation(self, regexstr):
        tmp = ".".join(list(regexstr)).replace("(.","(").replace(".)",")")
        tmp = tmp.replace(".+","+")
        tmp = tmp.replace(".*","*")
        tmp = tmp.replace(".?","?")
        tmp = tmp.replace(".|","|")
        tmp = tmp.replace("|.","|")
        return tmp

    def get_postfix(self, regexstr):
        output=""
        stack = []
        ops = {
                "*" : 3,
                "+" : 3,
                "?" : 3,
                "." : 2,
                "|" : 1
        }

        while len(regexstr) != 0:
            if self.is_char(regexstr[0]):
                output = output + regexstr[0]
                regexstr=regexstr[1:]

            else:
                char = regexstr[0]
                regexstr = regexstr[1:]
                if char == '(':
                    stack.append(char)
                elif char == ')':
                    while True:
                        stackchar = stack.pop()
                        if stackchar == '(':
                            break
                        else:
                            output = output + stackchar
                else:
                    while len(stack) > 0 and self.is_operator(stack[-1]) and  ops[char] <= ops[stack[-1]]:
                            output = output + stack.pop()
                    stack.append(char)

        while len(stack) >0:
            output = output + stack.pop()
        return output

    def is_char(self, char):
        return char not in ('(', ')', '*', '+', '?', '|', '.')
    def is_operator(self, char):
        return char in ('*', '+', '?', '.', '|')


    def get_nfa(self, postfix_regex):
        stack = []
        unary = ("*","+","?")
        binary = ("|",".")
        while len(postfix_regex) > 0:
            char = postfix_regex[0]
            postfix_regex = postfix_regex[1:]
            if self.is_char(char):
                stack.append(Container(char))
            elif char in unary:
                op = stack.pop()
                if char == "*":
                    stack.append(ZeroOrMore(op))
                elif char == "+":
                    stack.append(OneOrMore(op))
                elif char == "?":
                    stack.append(ZeroOrOne(op))
            elif char in binary:
                op2 = stack.pop()
                op1 = stack.pop()
                if char == ".":
                    stack.append(Concat(op1,op2))
                elif char == "|":
                    stack.append(Or(op1,op2))
        #print("Stack!")
        return stack.pop()

    def to_str(self, nfa):
        #print("Connections: %s" % nfa.connections)
        for c in nfa.connections:
            self.to_str(c.state)

if __name__ == "__main__":
        r = Regex("")
        word1 = ""
        regex = ""

        if len(sys.argv) < 2:
            print("Uso: python %s <N>" % sys.argv[0])
            sys.exit(1)

        for i in range(int(sys.argv[1])):
            word1 = word1 + "a"
            regex = regex + "a?"
        regex = regex + word1
        print("- N: %s" % sys.argv[1])
        print("- Word: %s" % word1)
        reg = r.add_concatenation(regex)
        print("- Regex: " +reg)
        postfix = r.get_postfix(reg)
        #print(postfix)
        NFA = r.get_nfa(postfix)
        word2 = "abbc"
        #print("NFA:")
        #print (r.to_str(NFA.start))
        m = Matcher(NFA.start, word1)
        t1 = datetime.datetime.utcnow()
        print("Our implementation ")
        print("Match?: ")
        print(m.searchMatch(word1))
        t2 = datetime.datetime.utcnow()
        delta = t2-t1
        print("Time:  %s.%s" % (delta.seconds, delta.microseconds))

        t3 = datetime.datetime.utcnow()
        print ("Python implementation ")
        print("Match?: ")
        print(re.match(regex,word1) != None)

        t4 = datetime.datetime.utcnow()
        delta = t4-t3

        print("Time:  %s.%s" % (delta.seconds, delta.microseconds))

