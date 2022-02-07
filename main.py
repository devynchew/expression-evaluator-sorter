from GetUserOption import GetUserOption
from GetInputFile import GetInputFile
from GetOutputFile import GetOutputFile
from GetExpression import GetExpression
from GetTraversalOption import GetTraversalOption
from GetPrintOption import GetPrintOption
from Parsetree import *
from BuildParseTree import BuildParseTree
from Evaluate import Evaluate
from Sort import Sort
from Calculator import Calculator
from ChangeConfig import ChangeConfig


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
        str = '\n'
        str += f'Please select your choice (\'1\',\'2\',\'3\',\'4\',\'5\',\'6\',\'7\'):'
        str += '\n1. Evaluate expression'
        str += '\n2. Sort expressions'
        str += '\n3. Change Tree Traversals'
        str += '\n4. Change Printing Order'
        str += '\n5. Open up a calculator interface'
        str += '\n6. Change operator'
        str += '\n7. Exit'
        
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
                # print(f'exp: {exp}')
                print(f'\nCurrent Print is set to {traversal} in {order} mode.')
                print('\n')
                tree = BuildParseTree.buildParseTree(exp)
                if traversal == 'Inorder Traversal':
                    tree.printInorder(0) 
                elif traversal == 'Preorder Traversal':
                    tree.printPreorder(0)
                elif traversal == 'Postorder Traversal':
                    tree.printPostorder(0)
                    
                print('')
                if order == 'Reverse':
                    for i in reversed(templist):
                        print(i)
                elif order == 'Standard':
                    for i in templist:
                        print(i)
                print(f'\nThe expression: {original} evaluates to: {Evaluate.evaluate(tree)} \n\n')
                BinaryTree.clearTemplist(templist)

            
            elif user_option == 2: # option 2
                inputFileClass = GetInputFile('Please enter input file: ', '\nPlease enter a valid text file with fully parenthesized mathematical expressions.') # get input file
                inputFile = inputFileClass.getInput()

                outputFileClass = GetOutputFile('Please enter output file: ', '\nPlease enter a valid output text file.')
                outputFile = outputFileClass.getOutput()
                
                sortClass = Sort(inputFile, outputFile)
                sortClass.sort()

            elif user_option == 3: # option 3 ryan #change print traversal option
                print(f'\n\nCurrent Tree Traversal is  {traversal}')
                print('Change Tree Traversal:')
                print('1. Inorder Traversal')
                print('2. Preorder Traversal')
                print('3. Postorder Traversal')
                traversalInputClass = GetTraversalOption('Enter choice here (\'1\',\'2\',\'3\'): ', '\nPlease enter a number between 1 and 3') # get traversal order
                traversalInput = traversalInputClass.get_TraversalOption()
                print('\n\n')
                if traversalInput == 1:
                    traversal = 'Inorder Traversal'
                elif traversalInput == 2:
                    traversal = 'Preorder Traversal'
                elif traversalInput == 3:
                    traversal = 'Postorder Traversal'
                
            elif user_option == 4: #option 4 ryan reverse traversal or standard
                print(f'\n\nCurrent Print Order is  {order}')
                print('Change Print Order:')
                print('1. Standard')
                print('2. Reverse')
                orderInputClass = GetPrintOption('Enter choice here (\'1\',\'2\'): ', '\nPlease enter a number between 1 and 2') # get printing order
                orderInput = orderInputClass.get_PrintOption()
                print('\n\n')
                if orderInput == 1:
                    order = 'Standard'
                elif orderInput == 2:
                    order = 'Reverse'
                
                
            elif user_option == 5: # option 5 Devyn calculator interface
                calculatorClass = Calculator()
                calculatorClass.run()
                
            elif user_option == 6: # option 6 Devyn change config file
                changeConfigClass = ChangeConfig('Please enter 1 for standard operator or 2 for special operator: ', 'Please enter either 1 or 2.')
                changeConfigClass.change_operator()

            elif user_option == 7:
                print('Bye, thanks for using ST1507 DSAA: Expression Evaluator & Sorter')
                exit_program = True
            else:
                continue

main_program = main_program()
main_program.run()


