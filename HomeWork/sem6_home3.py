'''Задача 32: 
Определить индексы элементов массива (списка), значения которых принадлежат заданному 
диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7] 
Вывод: [1, 9, 13, 14, 19]'''

lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min = 5
max = 15
prod=[]

for i in range(len(lst)):
    if min < lst[i] < max:
        prod.append(i)
print(prod)