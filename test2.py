l = ['(', '(', '-500', '+', '(', '4', '*', '3.14', ')', ')', '/', '(', '2', '**', '3', ')', ')']
str = ''
for i in range(len(l)):
    if i == len(l) - 1:
        str += l[i]
    else:
        str += l[i] + ' '

print(str)