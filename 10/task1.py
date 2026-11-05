"""
создайте и используйте функцию для расчета
периметра прямоугольника

создайте и используйте функцию для расчета
площади прямоугольника
"""

def get_perimeter_and_area(a, b):
    perimeter = 2 * a + 2 * b
    area = a * b
    return perimeter, area

x1 = int(input("введите значение 1 стороны"))
x2 = int(input("введите значение 1 стороны"))

perim, area  = get_perimeter_and_area(x1, x2)
print(perim, area)