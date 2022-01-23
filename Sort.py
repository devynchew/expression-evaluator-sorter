class Sort():
    def __init__(self, inputfile, outputfile):
        self.__inputfile = inputfile
        self.__outputfile = outputfile
    
    def sort(self): # main function for option 2 (sorting expressions from a file)
        with open(self.__inputfile) as file:
            expressions = []
            for line in file:
                expression = line.split(',')[0] # store the expression
               
                value = float(line.split(',')[1][:-1]) # store the value
                
                expression_n = expression.replace(' ', '') # remove all whitespaces from expression

                expressions.append((expression_n, value)) # append a tuple

            sorted_expressions = self.bubbleSort(expressions)

            self.printOutput(sorted_expressions)
            self.outputReport(self.__outputfile, sorted_expressions)

    def bubbleSort(self, l): # handles all the sorting logic
        isSorted = False # Set to false so we can enter while loop

        while not isSorted:
            isSorted = True # assume everything is sorted until a swap happens

            for i in range(len(l)-1): # end at 2nd last element to compare with last element
                if l[i][1]>l[i+1][1]: # sort by value ascending
                    l[i],l[i+1], = l[i+1], l[i]
                    isSorted = False
                elif l[i][1]==l[i+1][1]: # sort by length ascending
                    if len(l[i][0]) > len(l[i+1][0]):
                        l[i],l[i+1], = l[i+1], l[i]
                        isSorted = False
                    elif len(l[i][0]) == len(l[i+1][0]):
                        if l[i][0].count('(') + l[i][0].count(')') < l[i+1][0].count('(') + l[i+1][0].count(')'):
                            l[i],l[i+1], = l[i+1], l[i]
                            isSorted = False
        return l
    
    def writeToFile(self, file, content): # writes a line of string to a file
        # Open the file in append & read mode ('a+')
        with open(file, "a+") as file_object:
            # Move read cursor to the start of file.
            file_object.seek(0)
            # If file is not empty then append '\n'
            data = file_object.read(100)
            if len(data) > 0 :
                file_object.write("\n")
            # Append text at the end of file
            file_object.write(content)

    def outputReport(self, file, expressions): # generates the output report
        # create a unique list of values# create a unique list of values
        valueArr = []
        for expression in expressions:
            valueArr.append(expression[1])
        mySet = set(valueArr)
        uniqueValues = list(mySet)

        counter = 0 # counter just to handle how the first line prints differently
        for value in uniqueValues:
            if counter == 0:
                self.writeToFile(file, '*'*3 + ' Expressions with value= ' + str(value))
            else:
                self.writeToFile(file, '\n' + '*'*3 + ' Expressions with value= ' + str(value))
            counter += 1

            for expression in expressions:
                if expression[1] == value:
                    self.writeToFile(file, f'{expression[0]}==>{value}')

    def printOutput(self, expressions): # prints the output to screen
        # create a unique list of values
        valueArr = []
        for expression in expressions:
            valueArr.append(expression[1])
        mySet = set(valueArr)
        uniqueValues = list(mySet)

        print('>>>Evaluation and sorting started:')
        for value in uniqueValues:
            print('\n' + '*'*3 + ' Expressions with value= ' + str(value))
            for expression in expressions:
                if expression[1] == value:
                    print(f'{expression[0]}==>{value}')
        print('>>>Evaluation and sorting completed!')

