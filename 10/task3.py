"""
функция принимает текст, переворачивает порядок букв в словах но относительный
порядок слов сохраняет

"""

def reverse_letters_in_words(text):
    text_list = text.split()
    for i in range(len(text_list)):
        text_list[i] = text_list[i][::-1]

    return ' '.join(text_list)


input_text = input()
print(reverse_letters_in_words(input_text))