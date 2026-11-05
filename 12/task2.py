"""
Напишите рекурсивную функцию factorial(n), возвращающую n!.
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(20))