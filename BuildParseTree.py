from Parsetree import BinaryTree
from Stack import Stack
from Tokenize import Tokenize


class BuildParseTree:
        
    def buildParseTree(exp):
        exp = " ".join(exp)
        string = exp.split(' ')
        while '' in string:
            string.remove('')
        string = ' '.join(string)
        splitexp = string.split() 
        tokenizeClass = Tokenize(exList = splitexp)
        tokens = tokenizeClass.tokenize()
        stack = Stack()
        tree = BinaryTree('?')
        stack.push(tree) # reference to tree is pushed in

        currentTree = tree # reference to root node of tree

        for t in tokens:
            # print(t)
            # print(type(t))
            # RULE 1: If token is '(' add a new node as left child and descend into that node
            if t == '(':
                currentTree.insertLeft('?') 
                stack.push(currentTree)
                currentTree = currentTree.getLeftTree()
            # RULE 2: If token is operator set key of current node to that operator and add a new node as right child and descend into that node
            elif t in ['+', '-', '*', '/', '**']:
                currentTree.setKey(t)
                currentTree.insertRight('?')
                stack.push(currentTree)
                currentTree = currentTree.getRightTree() 

            # RULE 3: If token is number, set key of the current node to that number and return to parent
            elif t not in ['+', '-', '*', '/', '**', ')'] :
                # t = float(t)
                currentTree.setKey(float(t))  
                parent = stack.pop()
                currentTree = parent

            # RULE 4: If token is ')' go to parent of current node
            elif t == ')':
                currentTree = stack.pop()
            else:
                raise ValueError

        return tree