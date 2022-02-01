with open('config.txt', 'r') as configfile:
    symbol = configfile.readline()
    operator = configfile.readline()
    if symbol == ' ':
        print('space')
    else:
        print(char.encode())
    
    # print(symbol)
    # print(operator)
    
print(symbol)
print(type(symbol))
print(operator)