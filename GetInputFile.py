import os.path

class GetInputFile():
    def __init__(self, prompt, errorMsg): 
            self.prompt = prompt
            self.errorMsg = errorMsg

    def getInput(self):
        while True:
            try:
                value = input(self.prompt)
            except:
                print(self.errorMsg)
                continue
            if not os.path.isfile(value): # check if file exist
                print(self.errorMsg)
                continue
            else:
                # we got a valid value, exit the loop
                break
        return value