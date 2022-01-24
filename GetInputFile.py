import os.path
from Tokenize import Tokenize

class GetInputFile():
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
                
                # check that file is not empty and contains valid characters
                valid = True # assume expressions in input file are valid
                with open(value) as file:
                    content = file.read().strip() # get rid of leading or trailing whitespace (including newlines)
                    if content: # check if file is empty
                        with open(value) as f:
                            for line in f:
                                if not valid:
                                    break
                                expression = line.split(',')[0] # store the expression
                                expression_n = expression.replace(' ', '') # remove all whitespaces from expression
                                
                                expression_list = list(expression_n) # convert string to list

                                for i in range(len(expression_list) - 1):
                                    if i == 0: # ensure first char in expression is a parenthesis
                                        if expression_list[i] != '(':
                                            print('Input file must contain only fully parenthesized mathematical expressions.')
                                            valid = False
                                            break
                                    elif i == len(expression_list) - 1: # ensure last char in expression is a parenthesis
                                        if expression_list[i] != ')':
                                            print('Input file must contain only fully parenthesized mathematical expressions.')
                                            valid = False
                                            break
                                    else:
                                        pass
                        
                    else:
                        print('Input file must not be empty.')
                        continue

                if not valid: # input file is not valid, continue to prompt user for input file
                    print('something went wrong')
                    continue

                # if we reached here, start tokenising
                with open(value) as file:
                    for line in file:
                        expression = line.split(',')[0] # store the expression
                        expression_n = expression.replace(' ', '') # remove all whitespaces from expression
                        
                        expression_list = list(expression_n) # convert string to list
                        print(f'expression_list {expression_list}')

                        tokenizeClass = Tokenize(exList=expression_list)
                        l = tokenizeClass.tokenize()
                        print(f'tokenized list {l}')


            except:
                print(self.__errorMsg)
                continue

            else:
                # we got a valid value, exit the loop
                break
        return value