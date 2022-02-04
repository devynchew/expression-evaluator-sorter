from GetUserOption import GetUserOption
from GetInputFile import GetInputFile
from GetOutputFile import GetOutputFile
from parsetree import *
from Sort import Sort

class main_program:

    def interface(self):
        str = ''
        str += '*'*70 + '\n* ST1507 DSAA: Expression evaluator & Sorter' + f'{"*":>26}'
        str += '\n*' + '_'*68 + '*'
        str += '\n*' + ' '*68 + '*'
        str += '\n* - Done by: Devyn Chew (2026578) & Ryan Tan Kah Shing (2026312)' + f'{"*":>6}'
        str += '\n* - Class DAAA/2B/04' + f'{"*":>50}'
        str += '\n*' + ' '*68 + '*'
        str += '\n*' + '*'*69
        str += '\n\n\n\n'
        str += f'Please select your choice (\'1\',\'2\',\'3\'):'
        str += '\n1. Evaluate expression'
        str += '\n2. Sort expressions'
        str += '\n3. Exit'
        return str
    
    def run(self):

        exit_program = False

        while not exit_program:
            # print the interface
            print(self.interface())

            # get user option
            get_user_option = GetUserOption('Enter choice: ', 'Please enter a number between 1 and 4.')
            user_option = get_user_option.get_option()

            if user_option == 1: # option 1
                exp = input('\nPlease enter the expression you want to evaluate: ') #validation needed
                print('\n')
                tree = buildParseTree(exp)
                tree.printInorder(0) #needs to print 90 degrees
                # print(templist)
                for i in reversed(templist):
                    print(i)
                print (f'\nThe expression: {exp} evaluates to: {evaluate(tree)} \n\n')

            elif user_option == 2: # option 2
                inputFileClass = GetInputFile('Please enter input file: ', '\nPlease enter a valid text file with fully parenthesized mathematical expressions.') # get input file
                inputFile = inputFileClass.getInput()

                outputFileClass = GetOutputFile('Please enter output file: ', '\nPlease enter a valid output text file.')
                outputFile = outputFileClass.getOutput()
                
                sortClass = Sort(inputFile, outputFile)
                sortClass.sort()
                exit_program = True

            elif user_option == 3: # option 3
                print('Bye, thanks for using ST1507 DSAA: Expression Evaluator & Sorter')
                exit_program = True
                
            else:
                continue
main_program = main_program()
main_program.run()


