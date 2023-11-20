'''Задача No51.
Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют 
одинаковое значение некоторой характеристики, и возвращают True, если это так. 
Если значение характеристики для разных объектов отличается - то False. 
Для пустого набора объектов, функция должна возвращать True. 
Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
Ввод: Вывод:
values = [0, 2, 10, 6] same if same_by(lambda x: x % 2, values):
print(‘same’) 
else:
print(‘different’)
'''

def same_by(characteristic, objects):
    # return list(filter(characteristic, objects))==objects
    return len(list(filter(characteristic, objects)))==len(objects)
values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2 == 0, values):
    print('same') 
else:
    print('different')