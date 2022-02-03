from Parenthesized import Parenthesized

class GetExpression:
    def __init__(self, prompt, errorMsg):
        self.__prompt = prompt
        self.__errorMsg = errorMsg
        
    def getExpression(self):
        while True:
            try:
                exp = input(self.__prompt)
                