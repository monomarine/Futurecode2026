'''
Вывести все делители числа N.
Проверить, является ли число простым.
'''
is_simple = True
n = int(input("введите число (целое) "))
print('Все делители числа:')
for i in range(2, n):
    if n % i == 0:
        is_simple = False
        print(i)

if is_simple:
    print('простое')
else:
    print('не простое')