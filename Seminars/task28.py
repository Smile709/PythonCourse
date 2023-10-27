'''
найти факториал числа n через рекурсию
'''
def fact(n):
    if n <= 1:
        return n
    return fact(n - 1) * n
 
 
print(fact(5))