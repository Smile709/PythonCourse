'''
Задача №17. Дан список чисел. Определите, сколько в нем встречается различных чисел. 
Input: [1, 1, 2, 0, -1, 3, 4, 4] 
Output: 6
'''
# lst = [1, 1, 2, 0, -1, 3, 4, 4]
# lstDif = []

# for i in lst:
#      if i not in lstDif:
#         lstDif.append(i)
# print(len(lstDif))

numbers = [2, 2, 1]
print(len(set(numbers)))
print(set(numbers))
