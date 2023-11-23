'''Задача №49. 
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 
1. Программа должна выводить данные 
2. Программа должна сохранять данные в текстовом файле 
3. Пользователь может ввести одну из характеристик для поиска определенной записи
    (Например имя или фамилию человека) 
4. Использование функций. Ваша программа не должна быть линейной
'''
import os

def work_with_phonebook(filename): # Бот программы (основная функция)
	
    choice=show_menu()

    phone_book=read_txt(filename)

    while (choice!=8):

        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('Фамилия: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice==3:
            last_name=input('Фамилия: ')
            new_number=input('Новый номер тел.: ')
            print(change_number(phone_book, last_name, new_number))
        elif choice==4:
            last_name=input('Фамилия: ')
            print(delete_by_lastname(phone_book, last_name))
        elif choice==5:
            number=input('Номер тел.: ')
            print(find_by_number(phone_book, number))
        elif choice==6:
            user_line=input('Новая запись(Фамилия, Имя, Телефон, Описание): ')
            add_user(phone_book, user_line)
        elif choice==7:
            write_txt(filename, phone_book)

        choice=show_menu()

def show_menu(): # Печатает меню выбора
    print('1. Распечатать справочник', 
          '2. Найти телефон по фамилии', 
          '3. Изменить номер телефона', 
          '4. Удалить запись', 
          '5. Найти абонента по номеру телефона', 
          '6. Добавить абонента в справочник',
          '7. Сохранить справочник', 
          '8. Закончить работу', sep= '\n') 
    choice=int(input("введите команду: "))
    return choice

def read_txt(filename): #Добавить текст в программу
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r', encoding='utf-8') as file:
        for line in file:
            record = dict(zip(fields, line.split(',')))
            if '\n' in record['Описание']:
                record['Описание'] = record['Описание'][:-1]
            phone_book.append(record)
    return phone_book

def write_txt(filename, phone_book): #7.Записать программу в файл
    with open(filename,'w',encoding='utf-8') as file:
        for i in range(len(phone_book)):
            s='' 
            for v in phone_book[i].values():
                s+=v+','
            file.write(f'{s[:-1]}\n')
    print('Изменения внесены в файл')
    
def print_result(phone_book): #1.Распечатать справочник в консоль
    if len(phone_book) > 0:
        for line in phone_book:
            print(f"{line['Фамилия'].ljust(20)}{line['Имя'].ljust(20)}{line['Телефон'].ljust(20)}{line['Описание'].ljust(20)}")
    else: print(f"Файл не существует.")

def find_by_lastname(phone_book, last_name): #2.Поиск по фамилии
    for line in phone_book:
        if line['Фамилия'].lower() == last_name.lower():
            return line

def change_number(phone_book, last_name, new_number): #3.Изменить номер тел.
    for line in phone_book:
        if line['Фамилия'].lower() == last_name.lower():
            line['Телефон'] = str(new_number)
    return phone_book

def delete_by_lastname(phone_book, last_name): #4.Удалить запись
    count=0
    for line in phone_book:
        count+=1
        if line['Фамилия'].lower() == last_name.lower():
            phone_book.pop(count-1)
    return phone_book

def find_by_number(phone_book, number): #5.Поиск по номеру тел.
    for line in phone_book:
        if line['Телефон'] == str(number):
            return line

def add_user(phone_book, user_line): #6.Добавить запись
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_line.split(',')))
    phone_book.append(record)
    return phone_book

work_with_phonebook("phone_book.txt")