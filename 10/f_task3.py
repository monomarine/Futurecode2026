"""
Функция count_vowels(text), которая считает количество гласных в строке.
"""
from soupsieve.util import lower


def count_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я' ]
    count = 0
    for char in text:
        if char in vowels:
            count += 1

    return count

text = input()
print(count_vowels(text))