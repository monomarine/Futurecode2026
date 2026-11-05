"""
Функция count_vowels(text), которая считает количество гласных в строке.
"""

def count_vowels(text):
    vowels = "aeiouуеыаоэяию"
    count = 0
    for char in text:
        if char in vowels:
            count += 1

    return count

SOME_TEXT = input()
print(count_vowels(SOME_TEXT))

