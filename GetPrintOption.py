# Name: Ryan Tan Kah Shing
# Student ID: P2026312
# Class: DAAA/2B/04

class GetPrintOption:
    def __init__(self, prompt, errorMsg): 
            self.__prompt = prompt
            self.__errorMsg = errorMsg

    def get_PrintOption(self):
        while True:
            try:
                value = int(input(self.__prompt))
            except ValueError:
                print(self.__errorMsg)
                continue # continue skips the current iteration
            except:
                print(self.__errorMsg)
                continue
            if value < 1:
                print(self.__errorMsg)
                continue
            if value > 2:
                print(self.__errorMsg)
                continue
            else:
                # we got a valid value, exit the loop
                break
        return value