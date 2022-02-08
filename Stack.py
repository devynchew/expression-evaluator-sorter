# Name: Ryan Tan Kah Shing
# Student ID: P2026312
# Class: DAAA/2B/04

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

    