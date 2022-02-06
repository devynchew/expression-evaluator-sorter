from msilib.schema import Binary
from GetUserOption import GetUserOption
from GetInputFile import GetInputFile
from GetOutputFile import GetOutputFile
from GetExpression import GetExpression
from Parsetree import *
from BuildParseTree import BuildParseTree
from Evaluate import Evaluate
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
        return str

    def options(self):
        str = ''
        str += f'Please select your choice (\'1\',\'2\',\'3\'):'
        str += '\n1. Evaluate expression'
        str += '\n2. Sort expressions'
        str += '\n3. Exit'
        str += '\n4. Option 4'
        str += '\n5. Option 5'
        
        return str
    
    # mode = 'Inorder Traversal'
    # order = 'Reverse'
    def run(self):

        exit_program = False
        print(self.interface())

        while not exit_program:
            # print the interface
            print(self.options())

            # get user option
            get_user_option = GetUserOption('Enter choice: ', 'Please enter a number between 1 and 4.')
            user_option = get_user_option.get_option()

            
            if user_option == 1: # option 1
                getExpressionClass = GetExpression('Please enter the expression you want to evaluate: ', 'Please enter a fully parenthesized mathematical expression.')
                exp, original = getExpressionClass.get_expression()
                print(f'exp: {exp}')
                print('\n')
                tree = BuildParseTree.buildParseTree(exp)
                tree.printInorder(0) #needs to print 90 degrees
                # print(f'templist: {templist}')
                print('')
                for i in reversed(templist):
                    print(i)
                print (f'\nThe expression: {original} evaluates to: {Evaluate.evaluate(tree)} \n\n')
                BinaryTree.clearTemplist(templist)
                

            
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
                
            elif user_option == 4: #option 4 ryan #change print traversal option
                print(f'Current Tree Traversal is  {traversal}')
                print('Change Tree Traversal:')
                print('1. Inorder Traversal')
                print('2. Preorder Traversal')
                print('3. Postorder Traversal')
                traversal = input('Enter choice here:')
                
            elif user_option == 5: #option 5 ryan reverse traversal or standard
                print(f'Current Print Order is  {order}')
                print('Change Print Order:')
                print('1. Standard')
                print('2. Reverse')
                order = input('Enter choice here:')
            else:
                continue
main_program = main_program()
main_program.run()


