"""функция - генератор"""

def gen(n):
    i = 0
    while i < n:
        i = i+1
        yield i

res = gen(6)
print(res)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))

"""выражение - генератор"""
result =(i for i in range(5))
print(result)