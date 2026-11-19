'''
 запись всего текста в файл
'''

new_file = open('newfile1.txt', 'w', encoding='utf-8')
new_file.write("новый текст в фай   ле")
new_file.close()

with open('text.txt', 'w') as f:
    for _ in range(10):
        f.write('hello world\n')
