"""
Палиндром — число, читающееся одинаково в обе стороны.

Найти все палиндромы от 1 до N и посчитать их количество.
"""
n = int(input("введите верхний предел последовательности"))

for i in range(1, n + 1):
    number = str(i)
    mid = int(len(number) // 2)
    if number[0: mid] == number[:mid:-1]:
        print(number)