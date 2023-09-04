from funcional import *

def menu(item):
    if item == "1": read_all()
    elif item == "2": add_contact(input("Введите ФИО контакта: "), input("Введите номер контакта: "))
    elif item == "3": find_contact(input("Введите ФИО или номер для поиска: "))
    elif item == "4": edit_contact(input("Введите ФИО или номер который хотите изменить: "))
    elif item == "5": del_contact(input("Введите ФИО или номер который хотите удалить: "))
    elif item == "6": exit()
    else: print("Такого пункта меню нет.")

def print_item():
    return print("Выберите действие: "
                 "\n 1 - Вывод всех контактов "
                 "\n 2 - Добавить контакт "
                 "\n 3 - Поиск контакта "
                 "\n 4 - Изменить контакт "
                 "\n 5 - Удалить контакт "
                 "\n 6 - Выход")