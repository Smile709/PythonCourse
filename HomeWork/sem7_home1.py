'''Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, 
вычисляющую элемент по номеру строки и столбца.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
Если строк меньше двух, выдайте текст
ОШИБКА! Размерности таблицы должны быть больше 2!.
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

Пример
На входе:
print_operation_table(lambda x, y: x * y, 3, 3)
На выходе:
1 2 3
2 4 6 
3 6 9
'''
def print_operation_table(operation, num_rows, num_columns):
    if num_columns <= 1 or num_rows <= 1:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!') 
    else: 
        for i in range(1,num_rows+1):
            if i == 1:
                res = [i for i in range(1, num_rows+1)]
            for j in range(1,num_columns+1):
                print(operation(i,j), end=' ')
            print()

# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         for i in range(1,num_rows+1):
#             if i == 1:
#                 sq = [i for i in range(1,num_rows+1)]
#             else:
#                 sq = [operation(i,j) if j > 1 else i for j in range(1, num_columns + 1)]
#             print(*sq)

print_operation_table(lambda x, y: x - y, 5, 4)