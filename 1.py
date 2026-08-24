from math import sqrt
x = 5  # int
y = 5.45  # Float
name = 'Anna' # str
yes_no = True  # bool (False)
n = '5'  # str

##x = str(x)
##print(x)
##print('hi')
##print('x-', type(x))
##print('name-', type(name))
##print(name + str(x))  # конкактенация
##print('x-', type(x))
##n = '145'
##n = int(n)
##print(type(n))
##print(name * 3)
##x = True
##PI = 3.1415926
##print(PI)
##print(x, y, name, sep='...', end='|||')
##print(x, y, name, sep=' ')
##n = int(input('Vvedite zn: '))
##n1 = int(input('Vvedite zn: '))
##print(n + n1)
##print(type(n))

"""
+, -, *, **, /, //, %
"""
# vvod
a = 3
b = 4
c = 5
# obrabotka
s = int(a* b / 2)

# vyvod
##print(s)
##
##a = 31
##b = 42
##c = 56
##"""
##p = (a + b + c) / 2
##s = sqrt(p(p-a)(p-b)(p-c))
##"""
##p = (a + b + c) / 2
##s = sqrt(p * (p-a) * (p-b) * (p-c))
##print ('ploshad =', round(s, 3))
##print(5/2)
##print(5//2)
##print(5%2)
##
##
##print(123 % 10)
##s = '1234'
##print(s.isdigit())
n = input('Vvedite zn: ')
n1 = input('Vvedite zn: ')
if n.isdigit() and n1.isdigit():
    n = int(n)
    n1 = int(n1)
print(n + n1)
print(type(n))
