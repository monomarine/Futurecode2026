"""
в бесконечном цикле записывать строчки в файл
"""
print('вводите текст построчно. остановка ввода при пустой строке')

with open('someData.txt', 'a+', encoding='utf-8') as f:
    while True:
        line = input()
        if line == '':
            break
        f.write(line + "\n")