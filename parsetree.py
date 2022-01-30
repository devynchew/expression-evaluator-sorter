from Tokenize import Tokenize

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
            
        #N
        print( str(level*'.') + str(self.key))
        
        #R
        if self.rightTree != None:
            self.rightTree.printInorder(level+1)

class Stack:
    def __init__(self):
        self.__list= []
    
    def isEmpty(self):
        return self.__list == []
    def size(self):
        return len(self.__list)
    def clear(self):
        self.__list.clear()

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__list.pop()

    def get(self):
        if self.isEmpty():
            return None
        else:
            return self.__list[-1]

    def __str__(self): # print every item in the stack
        output = '<'
        for i in range( len(self.__list) ):
            item = self.__list[i]
            if i < len(self.__list)-1 :
                output += f'{str(item)}, '
            else:
                output += f'{str(item)}'
        output += '>'
        return output

def buildParseTree(exp):
    exp = " ".join(exp)
    string = exp.split(' ')
    while '' in string:
        string.remove('')
    string = ' '.join(string)
    splitexp = string.split() #to be replaced with new tokenizer, currently used for testing
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

#operator implementation 
def evaluate(tree):
    leftTree = tree.getLeftTree()
    rightTree = tree.getRightTree()
    op = tree.getKey()
    if leftTree != None and rightTree != None: 
        if op == '+':
            return evaluate(leftTree) + evaluate(rightTree)
        elif op == '-':
            return evaluate(leftTree) - evaluate(rightTree)
        elif op == '*':
            return evaluate(leftTree) * evaluate(rightTree)
        elif op == '**':
            return evaluate(leftTree) ** evaluate(rightTree)
        elif op == '/':
            print (evaluate(leftTree), evaluate(rightTree))
            return evaluate(leftTree) / evaluate(rightTree)
    else:
        return tree.getKey()
    
# exp = '( 2 + ( 4 * 5 ) )'
exp2 = '((-500+(4*3.14))/(2**3))'
# exp3 =  '((11.07+25.5)-10)'
tree = buildParseTree(exp2)
tree.printInorder(0)
print (f'The expression: {exp2} evaluates to: {evaluate(tree)}')