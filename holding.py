import os.path

class GetInputFile():
    def __init__(self, prompt, errorMsg): 
            self.__prompt = prompt
            self.__errorMsg = errorMsg

    def getInput(self):
        while True:
            try:
                value = input(self.__prompt)
                if not os.path.isfile(value): # check if file exist on path
                    print('Input file must exist on path.')
                    continue

                valid = True # assume expressions in input file are valid
                with open(value) as file:
                    content = file.read().strip() # get rid of leading or trailing whitespace (including newlines)
                    if content: # check if file is empty
                        operators = ['+', '-', '*', '/', '**']
                        with open(value) as f:
                            for line in f:
                                if not valid:
                                    break
                                expression = line.split(',')[0] # store the expression
                                expression_n = expression.replace(' ', '') # remove all whitespaces from expression
                                
                                expression_list = list(expression_n) # convert string to list
                                print(f'expression_list {expression_list}')

                                for i in range(len(expression_list) - 1):
                                    print(expression_list[i])
                                    if i == 0: # ensure first char in expression is a parenthesis
                                        if expression_list[i] != '(':
                                            print('Input file must contain only fully parenthesized mathematical expressions.')
                                            break
                                    elif i == len(expression_list) - 1: # ensure last char in expression is a parenthesis
                                        if expression_list[i] != ')':
                                            print('Input file must contain only fully parenthesized mathematical expressions.')
                                            break
                                    else: # tokenise expression
                                        if expression_list[i] not in ['+', '-', '*', '/', '**', '(', ')', '.']:
                                            print('Input file contains invalid characters.')
                                            valid = False
                                            break
                                        
                                        if isinstance(expression_list[i], (int, float)):  # check if char is an operand
                                            if expression_list[i-1] == '(' and expression_list[i+1] in operators:
                                                pass
                                            elif expression_list[i-1] in operators and expression_list[i+1] == ')':
                                                pass
                                            elif expression_list[i-1] == '(' and expression_list[i+1] == ')':
                                                pass
                                            else:
                                                print('Input file must contain only fully parenthesized mathematical expressions.')
                                                break
                                        elif expression_list[i] in operators: 
                                            pass
                                        elif expression_list[i] in ['(', ')']:
                                            pass
                                        else:
                                            print('Input file contains invalid characters.')
                                            valid = False
                                            break
                
                    else:
                        print('Input file must not be empty.')
                        continue
                if not valid: # input file is not valid, continue to prompt user for input file
                    continue

            except:
                print(self.__errorMsg)
                continue

            else:
                # we got a valid value, exit the loop
                break
        return value