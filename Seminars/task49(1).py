"""с помощью лямбда функций опрдеделить является ли число 2-х значным"""
num= '8 11 0 -23 140 1'
# print(*filter(lambda x: 10 <=abs(int (x)) <= 99,num.split()))
# print(f"Число {(lambda x: 10 <= x <= 99)(int(input("Введите число: ")))} является двузначным")
print(*filter(lambda x: len(str(abs(int(x))))==2,num.split()))