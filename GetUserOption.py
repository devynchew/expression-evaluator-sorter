from GetUserInputParent import GetUserInputParent

class GetUserOption(GetUserInputParent):
    def get_option(self):
        while True:
            try:
                value = int(input(self.prompt))
            except ValueError:
                print(self.errorMsg)
                continue # continue skips the current iteration
            except:
                print(self.errorMsg)
                continue
            if value < 1:
                print(self.errorMsg)
                continue
            if value > 3:
                print(self.errorMsg)
                continue
            else:
                # we got a valid value, exit the loop
                break
        return value