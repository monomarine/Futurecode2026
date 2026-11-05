"""
 Ввести текст,
 вывести количество слов
 и самое длинное слово (первое из самых длинных).
"""

text = input()
text_list = text.split()

long_word = max(text_list, key=len)
print(long_word)