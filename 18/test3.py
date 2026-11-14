"""
Дан кортеж чисел. Подсчитайте количество чётных и нечётных чисел.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
"""

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 3, 1, 5, 7 ,9)

count_chet = 0
count_nechet = 0

for n in numbers:
    if n % 2 == 0:
        count_chet += 1
    else:
        count_nechet += 1

print(count_chet, count_nechet)