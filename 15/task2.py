"""
Дана строка: "python java python c++ java python". Подсчитайте, сколько раз встречается каждое слово, и выведите результат в виде словаря.
Структура: dict.
"""

text = input()
text_list = text.split()
word_count = dict()

for word in text_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for key,value in word_count.items():
    print(f"{key} - {value}")