"""Задача No37
Дано натуральное число N и последовательность из N 
элементов. Требуется вывести эту последовательность в 
обратном порядке.
Примечание. В программе запрещается объявлять массивы и 
использовать циклы (даже для ввода и вывода).
Input: 2 -> 3 4 Output: 4 3
"""
n = 4
def func (qty):
    if qty == 0:
        return '+'
    num = input ('Введите число: ')
    return func(qty-1) + num
print (func(4))