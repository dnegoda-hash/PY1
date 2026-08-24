# def proba():
#     print('proba')
#     return 'function'
#
# n = proba()
# print(n)


def summator(x=10, y=50):  # summator - имя функции, x и y -параметры
    return x + y


res = summator(100, 20)
print(res)
print(summator(50, 30))
print(summator(90))  # позиционный аргумент
print(summator(y=10))  # ключевой аргумент


def many_args(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args)


print(many_args(2, 4, 3, 4, y=20, x=34))
print(many_args())
print(many_args(44, 66, c=76))

# Область видимости переменных
# параметры функции и определенные в ней переменные
# называются локальными