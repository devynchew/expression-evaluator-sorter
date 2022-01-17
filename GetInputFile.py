import os.path

class GetInputFile():
    def __init__(self, prompt, errorMsg): 
            self.__prompt = prompt
            self.__errorMsg = errorMsg

    def getInput(self):
        while True:
            try:
                value = input(self.__prompt)
            except:
                print(self.__errorMsg)
                continue
            if not os.path.isfile(value): # check if file exist
                print(self.__errorMsg)
                continue
            else:
                # we got a valid value, exit the loop
                break
        return value