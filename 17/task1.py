marks = [] #оценки конкретного студента

while True:
    m = input("введите оценку")
    if m.isnumeric() and 1 < int(m) < 6:
        marks.append(int(m))
    elif m == "":
        break
    else:
        continue


print("введенные оценки: ", marks)
print("средний балл: ", sum(marks) / len(marks))
print("количество двоек: ", marks.count(2))

