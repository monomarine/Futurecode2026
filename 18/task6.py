matrix = []

cols = int(input("введите количество столбцов "))
rows = int(input("введите количество строк "))
symbol = input('введите символ для заполнения ')

# заполнение матрицы
for i in range(rows):
    line = []
    matrix.append(line)
    for j in range(cols):
        line.append(symbol)

# вывод матрицы
for i in range(rows):
    for j in range(cols):
         print(matrix[i][j], end=' ')
    print()