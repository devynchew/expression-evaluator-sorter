# Name: Devyn Chew Kim Hong
# Student ID: P2026578
# Class: DAAA/2B/04

class Parenthesized:
    def __init__(self, exList):
        self.exList = exList

    # Conditions for fully parenthesized expressions:
    # All operands are surrounded by either one parenthesis and one operator, or two parentheses
    # The number of left brackets must be equal to the number of right brackets
    def checkParenthesis(self):
        operators = ['+', '-', '*', '/', '**']
        for i in range(len(self.exList)):
            if self.exList[i] not in ['(', ')', '+', '-', '*', '/', '**']: # item is an operand
                if self.exList[i-1] == '(' and self.exList[i+1] in operators:
                    pass
                elif self.exList[i-1] in operators and self.exList[i+1] == ')':
                    pass
                elif self.exList[i-1] == '(' and self.exList[i+1] == ')':
                    pass
                else:
                    return False
        if self.exList.count('(') != self.exList.count(')'):
            print('The number of left and right parenthesis must be equal.')
            return False
        return True