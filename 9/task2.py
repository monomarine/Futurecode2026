"""
Палиндром — число, читающееся одинаково в обе стороны.

Найти все палиндромы от 1 до N и посчитать их количество.
"""

n = int(input())

for i in range(n):
    num = str(i)
    mid = int(len(num) // 2)
    if num[0:mid] == num[:mid:-1]:
        print(num)
