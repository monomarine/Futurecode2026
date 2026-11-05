"""
Напишите рекурсивную функцию power(base, exp), возводящую base в степень exp (считаем exp >= 0).
"""

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp-1)

print(power(2,8))