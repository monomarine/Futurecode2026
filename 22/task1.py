"""
ÿрņľуņтся хрĽнить информĽцию о стуŅņнтĽх (имя, ĿозрĽст, курс)
с Ŀозможностью поискĽ по ID.
"""
students = {}

def add_student(student):
    global students

    id = input("введите идентификатор студента >> ")
    name = input("введите имя студента >> ")
    age = input("введите возраст студента >> ")
    course = input("введите курс студента >> ")

    if id not in students:
        students[id] = (name, age, course)
        print(f"студент {name} успешно добавлен")
    else:
        print("идентификатор занят. добавление невозможно")