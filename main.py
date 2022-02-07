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
        str += '\n4. Change Tree Traversals'
        str += '\n5. Change Printing Order'
        
        return str
    
    # mode = 'Inorder Traversal'
    # order = 'Reverse'
    
    def run(self):

        traversal = 'Inorder Traversal'
        order = 'Reverse'
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
                print('\n')
                tree = BuildParseTree.buildParseTree(exp)
                if traversal == 'Inorder Traversal':
                    tree.printInorder(0) 
                elif traversal == 'Preorder Traversal':
                    tree.printPreorder(0)
                elif traversal == 'Postorder Traversal':
                    tree.printPostorder(0)
                    
                # print(templist)
                print('')
                if order == 'Reverse':
                    for i in reversed(templist):
                        print(i)
                elif order == 'Standard':
                    for i in templist:
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
                traversalInput = input('Enter choice here (\'1\',\'2\',\'3\'): ')
                print('\n\n')
                if traversalInput == '1':
                    traversal = 'Inorder Traversal'
                elif traversalInput == '2':
                    traversal = 'Preorder Traversal'
                elif traversalInput == '3':
                    traversal = 'Postorder Traversal'
                
                
            elif user_option == 5: #option 5 ryan reverse traversal or standard
                print(f'Current Print Order is  {order}')
                print('Change Print Order:')
                print('1. Standard')
                print('2. Reverse')
                orderInput = input('Enter choice here (\'1\',\'2\'): ')
                if orderInput == '1':
                    order = 'Standard'
                elif orderInput == '2':
                    order = 'Reverse'
            else:
                continue
main_program = main_program()
main_program.run()


