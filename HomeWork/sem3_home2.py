"""
Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
Пример:
list_1 = [1, 2, 3, 4, 5]
k = 6
# 5
"""

list_1 = [1, 2, 3, 4, 5]
k = 6

closest = 0
dif = 0
minDif = max(list_1)

for i in list_1:
    dif = abs(i - k)
    if dif <= minDif:
        minDif = dif
        closest = i

print(closest)
