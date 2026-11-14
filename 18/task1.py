"""
1. Создайте список чисел от 1 до 10.
2. Выведите:
- Первые 3 элемента
- Последние 2 элемента
- Каждый второй элемент
- Список в обратном порядке
3. Поменяйте местами первый и последний элементы.
"""
# 0     1   2   3   4   5   6
# 1     2   3   4   5   6   7
# -7    -6  -5 -4   -3  -2 -1
numbers = list(range(1, 11))
print(numbers)

print(numbers[:3])
print(numbers[-1:-3:-1])
print(numbers[-2::])
print(numbers[::-1])

numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)