# Name: Devyn Chew Kim Hong
# Student ID: P2026578
# Class: DAAA/2B/04

class ChangeConfig:
    def __init__(self, prompt, errorMsg): 
            self.__prompt = prompt
            self.__errorMsg = errorMsg

    def change_operator(self):
        while True:
            try:
                value = int(input(self.__prompt))

                if value < 1:
                    print(self.__errorMsg)
                    continue

                if value > 2:
                    print(self.__errorMsg)
                    continue

                with open("config.txt", "r") as file:
                    lines = file.readlines()
                    lines[1] = str(value)

                with open("config.txt", "w") as file:
                    for line in lines:
                        file.write(line)

                if value == 1:
                    print('\nSwitched to standard operator.')
                if value == 2:
                    print('\nSwitched to special operator.')

                break
            except ValueError:
                print('Please enter a number, either 1 or 2.')
                continue # continue skips the current iteration
            except:
                print(self.__errorMsg)
                continue

        return value
