# Name: Ryan Tan Kah Shing
# Student ID: P2026312
# Class: DAAA/2B/04

from Parsetree import *

class Evaluate:
    def evaluate(tree):
        leftTree = tree.getLeftTree()
        rightTree = tree.getRightTree()
        op = tree.getKey()
        if leftTree != None and rightTree != None: 
            if op == '+':
                return operatorclass(Evaluate.evaluate(leftTree)) + operatorclass(Evaluate.evaluate(rightTree))
            elif op == '-':
                return operatorclass(Evaluate.evaluate(leftTree)) - operatorclass(Evaluate.evaluate(rightTree))
            elif op == '*':
                return operatorclass(Evaluate.evaluate(leftTree)) * operatorclass(Evaluate.evaluate(rightTree))
            elif op == '**':
                return operatorclass(Evaluate.evaluate(leftTree)) ** operatorclass(Evaluate.evaluate(rightTree))
            elif op == '/':
                return operatorclass(Evaluate.evaluate(leftTree)) / operatorclass(Evaluate.evaluate(rightTree))
        else:
            return tree.getKey()
