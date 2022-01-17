class GetOutputFile():
    def __init__(self, prompt, errorMsg): 
            self.__prompt = prompt
            self.__errorMsg = errorMsg

    def getOutput(self):
        while True:
            try:
                value = input(self.__prompt)
                if len(value) <= 4: # check if output filename is at least 1 character long
                    print('Please enter a \'.txt\' file with a name of at least one character.')
                    continue
                filename = value[:len(value) - 4] # remove the last 4 char from string to get filename
                endswith = value[-4:] # get the last 4 char from string to check for valid file type (.txt)
            except:
                print(self.__errorMsg)
                continue
            if endswith != '.txt': # check if output file ends with '.txt'
                print('Please enter a file ending with \'.txt\'.')
                continue
            if not all(x.isalnum() or x.isspace() or x not in('\\','/',':','*','?','"','<','>','|') for x in filename): # ensure output file name does not contain invalid characters
                print(self.__errorMsg)
                continue
            else:
                # we got a valid output file, exit the loop
                break
        return value