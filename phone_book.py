'''Задача №49. 
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 
1. Программа должна выводить данные 
2. Программа должна сохранять данные в текстовом файле 
3. Пользователь может ввести одну из характеристик для поиска определенной записи
    (Например имя или фамилию человека) 
4. Использование функций. Ваша программа не должна быть линейной
'''
# phone_book=['Иванов, Иван, 111, описание Иванова', 'Петров, Петр, 222, описание Петрова']
# filename = open('phone_book.txt', 'a', encoding='utf-8')
# filename.writelines(phone_book)
def work_with_phonebook(filename):
	
    choice=show_menu()

    phone_book=read_txt(filename)

    while (choice!=7):

        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print(change_number(phone_book,last_name,new_number))
        elif choice==4:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('new data ')
            add_user(phone_book,user_data)
            write_txt('phonebook.txt',phone_book)

        choice=show_menu()

def show_menu():
    print('1. Распечатать справочник', '2. Найти телефон по фамилии', '3. Изменить номер телефона', '4. Удалить запись', '5. Найти абонента по номеру телефона', '6. Добавить абонента в справочник', '7. Закончить работу', sep= '\n') 
    choice=int(input("введите команду: "))
    return choice

def read_txt(filename): 

    phone_book=[]

    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename,'r', encoding='utf-8') as file:

        for line in file:
            record = dict(zip(fields, line.split(',')))    
            phone_book.append(record)	

    return phone_book

def write_txt(filename, phone_book):

    with open(filename,'w',encoding='utf-8') as file:

        for i in range(len(phone_book)):
            s='' 
            for v in phone_book[i].values():
                s+=v+','
            file.write(f'{s[:-1]}\n')

def print_result(phone_book):
    print("ok")
work_with_phonebook("phone_book.txt")