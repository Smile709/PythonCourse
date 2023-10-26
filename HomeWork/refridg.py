'''
Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. 
Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.
Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, 
и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), 
то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы
Формат входных данных
В первой строке подаётся число
n
n – количество холодильников. В последующих n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 5 до 100 символов.
​Sample Input 1:
6
222anton456
a1n1t1o1n1
0000a0000n00t00000o000000n
gylfole
richard
ant0n
Sample Output 1:
1 2 3
Sample Input 2:
9
osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
anton
aoooooooooontooooo
elelelelelelelelelel
ntoneeee
tonee
253235235a5323352n25235352t253523523235oo235523523523n
antoooooooooooooooooooooooooooooooooooooooooooooooooooon
unton
Sample Output 2:
1 2 7 8
'''

virus = 'anton'
n = int(input('Введите кол-во холодильников: '))
infected_fridges = []

for i in range(n):
    code_fridge = (input(f'Введите код {i + 1} холодильника: '))

    index = 0
    found = False
    for letter in code_fridge:
        if letter == virus[index]:
            index += 1
        if index == len(virus):
            found = True
            break
    if found:
        infected_fridges.append(i + 1)
print(infected_fridges)