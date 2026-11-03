'''
Посчитать количество гласных в строке.
 Перевернуть строку без срезов
 Проверить, является ли строка палиндромом.
'''

text = input()
reverse_text = ""

for i in range(len(text)-1,-1,-1):
    reverse_text += text[i]

if reverse_text == text:
    print('палиндром')
else:
    print('не палиндром')