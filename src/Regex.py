

from State import *
from Link import *

class Regex:

    def __init__(self, regex_str):
        self.regex_str = regex_str
        self.nfa = None
        self.init_nfa()

    def init_nfa(self):
        expr = self.get_postfix(self.regex_str)

    def get_postfix(self, regexstr):
        output=""
        stack = []
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
                elif char in ('*','+','?'):
                    while len(stack) > 0:
                        if stack[-1] in ('*','+','?'):
                            output = output + stack.pop()
                        else:
                            break
                    stack.append(char)
                elif char == '|':
                    pass

        while len(stack) >0:
            output = output + stack.pop()
        return output

    def is_char(self, char):
        return char not in ('(', ')', '*', '+', '?', '|', '.')


if __name__ == "__main__":
        r = Regex("as*sad+asd")
        print r.get_postfix("a(bb)+c")

