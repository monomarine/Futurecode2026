path = r'D:\1.txt'
count = 0

with open(path, encoding='utf-8') as f:
    data = f.readlines()
    data = list(map(int, data))

    for i in data:
        if i > 0 and 10 <= i <= 99 and i % 2 == 0:
            count += 1

    print(count)