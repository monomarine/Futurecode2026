"""
Напишите рекурсивную функцию power(base, exp), возводящую base в степень exp (считаем exp >= 0).
"""

def power(base, exp):
    if exp == 1:
        return base
    return base * power(base, exp - 1)

print(power(25, 256))