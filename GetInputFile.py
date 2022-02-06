import os.path
from Tokenize import Tokenize
from Parenthesized import Parenthesized

class GetInputFile:
    def __init__(self, prompt, errorMsg): 
            self.__prompt = prompt
            self.__errorMsg = errorMsg

    def getInput(self):
        while True:
            try:
                value = input(self.__prompt)
                # check if file exist on path
                if not os.path.isfile(value): 
                    print('Input file must exist on path.')
                    continue
                
                # check that file is not empty and ensure it only contains valid characters
                valid = True # assume expressions in input file are valid
                with open(value) as file:
                    content = file.read().strip() # get rid of leading or trailing whitespace (including newlines)
                    if content: # check if file is empty
                        with open(value) as f:
                            for line in f:
                                if not valid: # don't bother checking other lines if one of the lines is invalid
                                    break
                                expression = line.split(',')[0] # store the expression
                                expression_n = expression.replace(' ', '') # remove all whitespaces from expression
                                
                                expression_list = list(expression_n) # convert string to list
                                # print(f'expression_list {expression_list}')
                                for i in range(len(expression_list)):
                                    if i == 0: # ensure first char in expression is a parenthesis
                                        if len(expression_list) == 1:
                                            print('Expressions in input file must contain more than 1 character.')
                                            valid = False
                                            break
                                        if expression_list[i] != '(':
                                            print('Expressions in input file must start with parenthesis.')
                                            valid = False
                                            break
                                    elif i == len(expression_list) - 1: # ensure last char in expression is a parenthesis
                                        if expression_list[i] != ')':
                                            print('Expressions in input file must end with parenthesis.')
                                            valid = False
                                            break
                                    else: # ensure that only valid characters are used
                                        if expression_list[i] not in ['+', '-', '*', '/', '(', ')', '.'] and not expression_list[i].isdigit():
                                            print('Input file contains invalid characters. Only numbers, +, -, *, **, /, (, ) are allowed.')
                                            valid = False
                                            break
                                        
                        
                    else:
                        print('Input file must not be empty.')
                        continue

                if not valid: # input file is either empty or contains invalid characters, continue to prompt user for input file
                    continue

                # if we reached here, start tokenising
                with open(value) as file:
                    for line in file:

                        expression = line.split(',')[0] # store the expression
                        expression_n = expression.replace(' ', '') # remove all whitespaces from expression
    
                        expression_list = list(expression_n) # convert string to list
                        # print(f'expression_list {expression_list}')

                        tokenizeClass = Tokenize(exList=expression_list)
                        l = tokenizeClass.tokenize()
                        # print(f'tokenized list {l}')

                        # Check if expressions are fully parenthesized
                        parenthesizedClass = Parenthesized(exList=l)
                        valid = parenthesizedClass.checkParenthesis()
                        if not valid: # don't bother checking other lines if one of them is not fully parenthesized
                            print(f'Expression: {l} is not fully parenthesized.')
                            break

                if not valid:
                    continue
                else:
                    break

            except:
                print(self.__errorMsg)
                continue

        return value