"""
Условие: Создайте словарь контактов: {"Alice": "+7-900-111", "Bob": "+7-900-222"}. Реализуйте:

Добавление нового контакта.

Поиск номера по имени (если нет — вернуть "Не найден").

Удаление контакта.
Структура: dict.
"""
phones = {}

def AddPhone(name, phone):
    if not name in phones:
        phones[name] = phone
    else:
        print("данный контакт уже добавлен")

def RemovePhone(name):
    if name in phones:
        del phones[name]

def PrintPhones():
    i = 1
    for name, phone in phones.items():
        print(f"{i}: {name}: {phone}")
        i += 1

while True:
    print("выберите вариант работы\n"
          "1 - добавить контакт\n" 
          "2 - удалить контакт\n"
          "3 - вывести телефонную книгу\n")

    answer = input()
    if answer == "1":
        name = input("введите имя контакта")
        phone = input("введите телефон")
        AddPhone(name, phone)

    elif answer == "2":
        name = input("введите имя контакта")
        RemovePhone(name)

    elif answer == "3":
        PrintPhones()

    else:
        print("некорректный вариант работы")
