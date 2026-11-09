"""
рекурсивно развернуть строку
"""

def reverse_recurion(text: str):
    if len(text) == 1:
        return text
    return text[-1] + reverse_recurion(text[:-1])

tt = input()
print(reverse_recurion(tt))