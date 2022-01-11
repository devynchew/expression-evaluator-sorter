class main_program:


    def interface():
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

main_program = main_program
print(main_program.interface())




main_program() # run the main program