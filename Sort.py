class Sort():
    def __init__(self, filename):
        self.__filename = filename
    
    def sort(self):
        with open(self.__filename) as file:
            expressions = []
            for line in file:
                line.rstrip() # remove trailing whitespaces
                expression = (line.split(' ')[0], float(line.split(' ')[1][:-1]))
                print(expression)
                expressions.append(expression)
            print(expressions)
            self.bubbleSort(expressions)
            print(expressions)

    def bubbleSort(self, l):
        isSorted = False # Set to false so we can enter while loop

        while not isSorted:
            isSorted = True # assume everything is sorted until a swap happens
            print(len(l))
            for i in range(len(l)-1): # end at 2nd last element to compare with last element
                if l[i][1]>l[i+1][1]:
                    l[i],l[i+1], = l[i+1], l[i]
                    isSorted = False