"""
Напишите функцию counter(), которая увеличивает
глобальную переменную count на 1 при каждом вызове.
Начальное значение count = 0.
"""
count = 0

def counter():
    global count
    count += 1

counter()
counter()
counter()
counter()

print(count)