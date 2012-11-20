

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
        while len(postfix_regex):
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
                op1 = stack.pop()
                op2 = stack.pop()
                if char == ".":
                    stack.append(Concat(op1,op2))
                elif char == "|":
                    stack.append(Or(op1,op2))

        return stack.pop()

if __name__ == "__main__":
        r = Regex("as*sad+asd")
        reg = r.add_concatenation("a(bb|cc)+c")
        print(reg)
        postfix = r.get_postfix(reg)
        print(postfix)
        NFA = r.get_nfa(postfix)
        word1 = "abbc"
        word2 = "abc"
        m = Matcher(NFA.start, word1)
        print(m.searchMatch(word1))
        m = Matcher(NFA.start,word2)
        print (m.searchMatch(word2))

