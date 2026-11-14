"""
Дан список numbers = [10, 25, -3, 7, 9, 4, -8, 6, 1, 12].

Вычислите произведение элементов среза numbers[-2:2:-2].
"""

numbers = [10, 25, -3, 7, 9, 4, -8, 6, 1, 12]
result = 1

for num in numbers[-2:2:-2]:
    print(num, end=' ')
    result *= num

print("\n", result)
