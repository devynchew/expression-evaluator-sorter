class Tokenize:
    def __init__(self, exList):
        self.exList = exList
        
    def tokenize(self):
        operators = ['+', '-', '*', '/', '**']
        tokenizedList = []
        tempList = []

        for i in range(len(self.exList)):
            if self.exList[i].isdigit() and tempList and (tempList[-1].isdigit() or tempList[-1] == '-' or tempList[-1] == '.'):
                tempList.append(self.exList[i])
            elif self.exList[i] == '-' and self.exList[i-1] == '(':
                tempList.append(self.exList[i])
            # handling floats
            elif self.exList[i].isdigit() and self.exList[i+1] == '.':
                tempList.append(self.exList[i])
            elif self.exList[i] == '.' and tempList[-1].isdigit():
                tempList.append(self.exList[i])
            # handling multiple digits
            elif self.exList[i].isdigit() and self.exList[i+1].isdigit():
                tempList.append(self.exList[i])
            # handling power
            elif self.exList[i] == '*' and self.exList[i+1] == '*':
                tempList.append(self.exList[i])
            elif self.exList[i] == '*' and tempList and tempList[-1] == '*':
                tempList.append(self.exList[i])
            # add tempList to tokenizedList and reset tempList    
            elif tempList and tempList[-1].isdigit() and (self.exList[i] in operators or self.exList[i] == ')'):
                str = ''
                l = []
                for char in tempList:
                    str += char
                l.append(str)
                tokenizedList = tokenizedList + l
                tokenizedList.append(self.exList[i])
                tempList = []
            elif tempList and self.exList[i].isdigit() and tempList[-1] == '*':
                str = ''
                l = []
                for char in tempList:
                    str += char
                l.append(str)
                tokenizedList = tokenizedList + l
                tokenizedList.append(self.exList[i])
                tempList = []
            else:
                tokenizedList.append(self.exList[i])
                
        return tokenizedList

