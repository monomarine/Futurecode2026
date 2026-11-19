students = {}

# n - кол студентов в группе

# имя студента
# список оценок (разд пробелами)

def load_students():
    global students
    n = int(input())

    for _ in range(n):
        name = input()
        marks = input().split()
        students[name] = list(map(int, marks))

def get_average_marks():
    average_group = 0
    for student, marks in students.items():
        average_student = sum(marks) / len(marks)
        average_group += average_student

    average_group /= len(students)
    return average_group

def get_good_studets(average_group : float):
    result = []
    for student, marks in students.items():
        average_student = sum(marks) / len(marks)
        if average_student >= average_group:
            result.append(student)

    return result


load_students()
average = get_average_marks()
res = get_good_studets(average)
res.sort()
print(res)