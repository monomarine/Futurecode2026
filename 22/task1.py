"""
ÿрņľуņтся хрĽнить информĽцию о стуŅņнтĽх (имя, ĿозрĽст, курс)
с Ŀозможностью поискĽ по ID.
"""
students = {}

def add_student():
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

def find_student_by_id(id):
    print(students.get(id, f"студент с {id} не найден"))

while True:
    print("выберите режим работы:\n"
          "1 - добавление студента\n"
          "2 - поиск студента по id\n")

    mode = int(input())
    if mode == 1: add_student()
    elif mode == 2:
        id = input("введите id студента >> ")
        find_student_by_id(id)