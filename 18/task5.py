from random import randint
matrix = []

# заполнение матрицы
for i in range(10):
    line = []
    matrix.append(line)
    for j in range(10):
        line.append(randint(10, 99))

for i in range(10):
    summ = 0
    for j in range(10):
        print(matrix[i][j], end = ' ')
        summ += matrix[i][j]
    print(f"\tсреднее по строке - {summ / 10}", end = ' ')
    print()