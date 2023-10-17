"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть.
"""

coins = [0, 1, 0, 1, 1, 0]

count_orel = 0
count_reshka = 0

for i in range(len(coins)):
    if coins[i] == 1:
        count_orel += 1
    else:
        count_reshka += 1
if count_orel > count_reshka:
    print(count_reshka)
else:
    print(count_orel)
