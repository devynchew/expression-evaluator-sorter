exList = ['(', '(', '-', '5', '0', '0', '+', '(', '4', '*', '3', '.', '1', '4', ')', ')', '/', '(', '2', '*', '*', '3', ')', ')']

def tokenize(exList):
    valid = True
    operators = ['+', '-', '*', '/', '**']
    tokenizedList = []
    tempList = []

    for i in range(len(exList) - 1):
        if exList[i].isdigit() and (tempList[-1].isdigit() or tempList[-1] == '-' or tempList[-1] == '.'):
            tempList[-1] = tempList[-1] + exList[i]
        else:
            tokenizedList.append(exList[i])
            
    return valid, tokenizedList

valid, list = tokenize(exList)
print(list)
