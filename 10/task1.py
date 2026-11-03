"""
создайте и используйте функцию для расчета
периметра прямоугольника

создайте и используйте функцию для расчета
площади прямоугольника
"""

def get_area_and_perimeter(a, b):
    area = a * b
    perimeter = a + b
    return area, perimeter

height = int(input("введите высоту прямоугольника"))
weight = int(input("введите ширину прямоугольника"))

a, b = get_area_and_perimeter(height, weight)
print(f"площадь - {a}\n"
      f"периметр - {b}\n")