'''
Задача №19. 
Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  
K – положительное число. 
Input:   [1, 2, 3, 4, 5] k = 2 
Output:  [4, 5, 1, 2, 3]
'''

list1 = [1, 2, 3, 4, 5]
k=2

print(list1.pop(0))
print(list1.remove(4))

k=k%len(list1)
for i in range(k):
    temp=list1.pop()
    list1.insert(0, temp)
    print(list1)

# list2=list1[-k:]+list1[:-k]
# print(list2)