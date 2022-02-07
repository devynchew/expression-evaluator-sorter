from Tokenize import Tokenize
from Parenthesized import Parenthesized

class GetExpression:
    def __init__(self, prompt, errorMsg):
        self.__prompt = prompt
        self.__errorMsg = errorMsg
        
    def get_expression(self):
        while True:
            try:
                expression = input(self.__prompt)
                expression_n = expression.replace(' ', '') # remove all whitespaces from expression
                expression_list = list(expression_n) # convert string to list

                valid = True # assume expression by user is valid first
                for i in range(len(expression_list)):
                    if i == 0: # ensure first char in expression is a parenthesis
                        if len(expression_list) == 1:
                            print('Expression must be more than 1 character.')
                            valid = False
                            break
                        if expression_list[i] != '(':
                            print('Expression must start with parenthesis.')
                            valid = False
                            break
                    elif i == len(expression_list) - 1: # ensure last char in expression is a parenthesis
                        if expression_list[i] != ')':
                            print('Expression must end with parenthesis.')
                            valid = False
                            break
                    else: # ensure that only valid characters are used
                        if expression_list[i] not in ['+', '-', '*', '/', '(', ')', '.'] and not expression_list[i].isdigit():
                            print('Expression contains invalid characters. Only numbers, +, -, *, **, /, (, ) are allowed.')
                            valid = False
                            break
                if not valid: # input expression contains invalid characters, continue to prompt user for input expression
                    continue

                # if we reached here, start tokenising
                tokenizeClass = Tokenize(exList=expression_list)
                l = tokenizeClass.tokenize()

                # Check if expressions are fully parenthesized
                parenthesizedClass = Parenthesized(exList=l)
                valid = parenthesizedClass.checkParenthesis()

                if not valid: # input expression is not fully parenthesized, continue to prompt user for input expression
                    continue
                else:
                    break

            except:
                print(self.__errorMsg)
                continue
        return l, expression

# getExpressionClass = GetExpression('Please enter the expression you want to evaluate: ', 'Please enter a fully parenthesized mathematical expression.')
# exp = getExpressionClass.get_expression()
# print(exp)