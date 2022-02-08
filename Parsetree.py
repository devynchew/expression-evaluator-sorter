# Name: Ryan Tan Kah Shing
# Student ID: P2026312
# Class: DAAA/2B/04

from Operator1 import Operator1
from Operator2 import Operator2

templist = []

class ParseTree:
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

    def insertLeft(self, key):
        if self.leftTree == None:
            # insert as left subtree of current tree
            self.leftTree = ParseTree(key)
        else:
            t = ParseTree(key)
            # insert key into the middle of self and self's left tree
            self.leftTree , t.leftTree = t, self.leftTree

    def insertRight(self, key):
        if self.rightTree == None:
            self.rightTree = ParseTree(key)
        else:
            t = ParseTree(key)
            # insert key into the middle of self and self's right tree
            self.rightTree , t.rightTree = t, self.rightTree
    
    
    def printInorder(self, level): #Inorder traversal
        
        #L
        if self.leftTree != None:
            self.leftTree.printInorder(level+1)
            
        # N
        templist.append(str(level*symbol) + str(self.key))
        
        #R
        if self.rightTree != None:
            self.rightTree.printInorder(level+1)
        
    def printPreorder(self, level): #Preorder traversal
        
        #N
        templist.append(str(level*symbol) + str(self.key))

        #L
        if self.leftTree != None:
            self.leftTree.printPreorder(level+1)
        
        #R
        if self.rightTree != None:
            self.rightTree.printPreorder(level+1)
            
    def printPostorder(self, level): #Postorder traversal
        
        #L
        if self.leftTree != None:
            self.leftTree.printPostorder(level+1)
        
        #R
        if self.rightTree != None:
            self.rightTree.printPostorder(level+1)
            
        #N
        templist.append(str(level*symbol) + str(self.key)) 
        
    def clearTemplist(list): #clear list after printing tree traversal
        
        return templist.clear()
        

    
#main
with open('config.txt', 'r') as configfile:
    symbol = configfile.readline() #read first line(symbol)
    if symbol == ' \n': #set symbol to space if symbol is space followed by newline
        symbol = ' '
    else:
        symbol = symbol.rstrip() #remove newline
        if len(symbol) >1:
            symbol = symbol[0] #take first character of symbol if symbol is longer than 1 character
            print('\n\n\nYour separator contains more than 1 character, we will take the first character by default and continue the program.')
            print('\nPlease exit the program and edit the config.txt file if you wish to change your separator.\n\n')
    operatorclass = configfile.readline() #read second line(operator class)
    operatorclass = operatorclass.rstrip()
    if operatorclass == '2':
        operatorclass = Operator2
    else:
        operatorclass = Operator1
    
