"""
 Ввести текст,
 вывести количество слов
 и самое длинное слово (первое из самых длинных).
"""

text = input("введите произвольный текст ")

text_list = text.split()
max_leght_word = max(text_list, key=len)
print(max_leght_word)