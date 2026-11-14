matrix = []

n = int(input("введите количество строк "))
m = int(input("введите количество столбцов "))
for i in range(n + 1):
    matrix.append([])
    for j in range(m + 1):
        matrix[i].append('*')


print(matrix)