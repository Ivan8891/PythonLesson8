
def add_contact(fio, number):
    file_data = open("pythonlesson8\data.txt", "a")
    file_data.writelines(fio + "\t" + number + "\n")
    print("Контакт успешно добавлен.")
    file_data.close()


def read_all():
    file_data = open("pythonlesson8\data.txt", "r")
    for line in file_data:
       print(line[:-1])
    file_data.close()


def find_contact(text):
    file_data = open("pythonlesson8\data.txt", "r")
    for line in file_data:
        if text in line:
            print(line[:-1])
    file_data.close()

def edit_contact(old_text):
    with open ("pythonlesson8\data.txt", "r") as f:
        old_data = f.read()
        if old_text in old_data:
            
            new_text = input("Введите новые данные: ")
            new_data = old_data.replace(old_text, new_text)

            with open ("pythonlesson8\data.txt", "w") as f:
                f.write(new_data)
            print("Данные успешно изменены.")
        else:
            print("Нет таких данных.")

def del_contact(contact):
    with open ("pythonlesson8\data.txt", "r") as f:
        old_data = f.read()
        if contact in old_data:

            new_data = old_data.replace(contact, "")

        with open ("pythonlesson8\data.txt", "w") as f:
            f.write(new_data)
        print("Данные успешно удалены.")
        #print("Нет таких данных.")