# Name: Devyn Chew Kim Hong
# Student ID: P2026578
# Class: DAAA/2B/04

class GetUserOption:
    def __init__(self, prompt, errorMsg): 
            self.__prompt = prompt
            self.__errorMsg = errorMsg

    def get_option(self):
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
            if value > 7:
                print(self.__errorMsg)
                continue
            else:
                # we got a valid value, exit the loop
                break
        return value