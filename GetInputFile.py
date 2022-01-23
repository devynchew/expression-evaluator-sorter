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
                        print('Ok')
                        with open(value) as f:
                            for line in f:
                                expression = line.split(',')[0] # store the expression
                                expression_n = expression.replace(' ', '') # remove all whitespaces from expression
                                
                                expression_list = list(expression_n) # convert string to list

                                for i in range(len(expression_list) - 1):
                                    print(i)
                                    if i == 0: # ensure first char in expression is a parenthesis
                                        if expression_list[i] not in ['(', ')']:
                                            valid = False
                                            print('Input file must contain only fully parenthesized mathematical expressions.')
                                            continue
                                    elif i == len(expression_list) - 1: # ensure last char in expression is a parenthesis
                                        if expression_list[i] not in ['(', ')']:
                                            valid = False
                                            print('Input file must contain only fully parenthesized mathematical expressions.')
                                            continue
                                    else:
                                        if isinstance(expression_list[i], (int, float)):  # check if char is an operand
                                            if expression_list[i-1] == '(' and expression_list[i+1] in ['+', '-', '*', '/', '**']:
                                                pass
                                            elif expression_list[i-1] in ['+', '-', '*', '/', '**'] and expression_list[i+1] == ')':
                                                pass
                                            elif expression_list[i-1] == '(' and expression_list[i+1] == ')':
                                                pass
                                            else:
                                                print('Input file must contain only fully parenthesized mathematical expressions.')
                                                continue






                    else:
                        print('Input file must not be empty.')
                        continue

            except:
                print(self.__errorMsg)
                continue

            else:
                # we got a valid value, exit the loop
                break
        return value