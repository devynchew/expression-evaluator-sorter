from Operator1 import Operator1
from Operator2 import Operator2

templist = []

class BinaryTree:
    def __init__(self, key, leftTree = None, rightTree = None):
        self.key = key
        self.leftTree = leftTree
        self.rightTree = rightTree

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def getLeftTree(self):
        return self.leftTree

    def getRightTree(self):
        return self.rightTree

    # for CA2, you will likely store a string in 'key', like +, - sign
    def insertLeft(self, key):
        if self.leftTree == None:
            # insert as left subtree of current tree
            self.leftTree = BinaryTree(key)
        else:
            t = BinaryTree(key)
            # insert key into the middle of self and self's left tree
            self.leftTree , t.leftTree = t, self.leftTree

    def insertRight(self, key):
        if self.rightTree == None:
            self.rightTree = BinaryTree(key)
        else:
            t = BinaryTree(key)
            # insert key into the middle of self and self's right tree
            self.rightTree , t.rightTree = t, self.rightTree
    
    
    def printInorder(self, level):
        
        #L
        if self.leftTree != None:
            self.leftTree.printInorder(level+1)
            
        # N
        templist.append(str(level*symbol) + str(self.key))
        
        #R
        if self.rightTree != None:
            self.rightTree.printInorder(level+1)
        
    def clearTemplist(list):
        
        return templist.clear()
        
        
    def printPreorder(self, level):
        
        #N
        templist.append(str(level*symbol) + str(self.key))

        #L
        if self.leftTree != None:
            self.leftTree.printPreorder(level+1)
        
        #R
        if self.rightTree != None:
            self.rightTree.printPreorder(level+1)
            
    def printPostorder(self, level):
        
        #L
        if self.leftTree != None:
            self.leftTree.printPostorder(level+1)
        
        #R
        if self.rightTree != None:
            self.rightTree.printPostorder(level+1)
            
        #N
        templist.append(str(level*symbol) + str(self.key)) 
        
        

    
#main
with open('config.txt', 'r') as configfile:
    symbol = configfile.readline()
    # print(symbol)
    if symbol == ' \n':
        symbol = ' '
    else:
        symbol = symbol.rstrip()
        if len(symbol) >1:
            symbol = symbol[0]
            print('\n\n\nYour separator contains more than 1 character, we will take the first character by default and continue the program.')
            print('\nPlease exit the program and edit the config.txt file if you wish to change your separator.\n\n')
    operatorclass = configfile.readline()
    operatorclass = operatorclass.rstrip()
    if operatorclass == '2':
        operatorclass = Operator2
    else:
        operatorclass = Operator1
    
