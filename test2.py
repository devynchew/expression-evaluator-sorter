l = ['-', '5', '0', '0']
l2 = ['(', '(']

str = ''
for ele in l:
    str += ele
print(str)
l_t = []
l_t.append(str)

l3 = l2 + l_t
print(l3)

templ = []
if templ:
    print('yes')
else:
    print('no')