"""определить с помощью рекурсии, число Х является простым"""

def symple(n, i=2):
    if n == 2 or i * i > n:
        return True
    if n % i == 0:
        return False
    return symple(n, i + 1)

print(symple(11))
