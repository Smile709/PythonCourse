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
    #        user_line=input('Новая запись: ')
            add_user(phone_book, user_line)
    #        write_txt(filename, phone_book)
        elif choice==7:
            write_txt(filename, phone_book)

        choice=show_menu()

def show_menu():
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
            phone_book.append(record)
    return phone_book

def write_txt(filename, phone_book): #Записать программу в файл
    with open(filename,'w',encoding='utf-8') as file:
        for i in range(len(phone_book)):
            s='' 
            for v in phone_book[i].values():
                s+=v+','
            file.write(f'{s[:-1]}\n')

def print_result(phone_book): #Распечатать справочник в консоль
    if len(phone_book) > 0:
        for line in phone_book:
            print(f"{line['Фамилия']}, {line['Имя']}, {line['Телефон']}, {line['Описание']}")
    else: print(f"Файл не существует.")

def find_by_lastname(phone_book, last_name):
    for line in phone_book:
        if line['Фамилия'].lower() == last_name.lower():
            result = line['Телефон'] 
        else: result = "Такой Фамилии нет"
    return result

def find_by_number(phone_book, number):
    for line in phone_book:
        if line['Телефон'].lower() == number.lower():
            result = line['Фамилия', 'Имя'] 
        else: result = "Такого номера нет"
    return result

def change_number(phone_book, last_name, new_number):
    for line in phone_book:
        if line['Фамилия'].lower() == last_name.lower():
            line['Телефон'] = new_number
        else: result = "Такой Фамилии нет"
    return result

def delete_by_lastname(phone_book, last_name):
    for line in phone_book:
        if line['Фамилия'].lower() == last_name.lower():
            line[:] = []
        else: result = "Такой Фамилии нет"
    return result

def add_user(phone_book, user_line):
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_line.split(',')))
    phone_book.append(record)
    return phone_book

work_with_phonebook("phone_book.txt")