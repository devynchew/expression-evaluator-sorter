class Parenthesized():
    def __init__(self, exList):
        self.exList = exList

    # Conditions for fully parenthesized expressions:
    # All operands are surrounded by either one parenthesis and one operator, or two parentheses
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
                    print(f'current char: {self.exList[i]}')
                    return False
        return True