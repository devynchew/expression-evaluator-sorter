class Sort():
    def __init__(self, filename):
        self.__filename = filename
    
    def sort(self):
        with open(self.__filename) as file:
            expressions = []
            for line in file:
                expression = line.split(',')[0] # store the expression
                print(expression)
                value = float(line.split(',')[1][:-1]) # store the value
                
                expression_n = expression.replace(' ', '') # remove all whitespaces from expression

                expressions.append((expression_n, value)) # append a tuple
            print(expressions)
            print()
            self.bubbleSort(expressions)
            print(expressions)

    def bubbleSort(self, l):
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