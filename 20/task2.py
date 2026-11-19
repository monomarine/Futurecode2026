"""
Напишите программу, которая объединит два списка товаров с их количеством в один общий складской отчет.
Нужно создать единый словарь, где названия фруктов — это ключи,
а итоговое количество на складе — значения. Если фрукт встречается в обоих списках, его количества нужно сложить.

На вход программе подаются две строки. В каждой строке через пробел записаны пары «
название:количество
». Например:
яблоки:10 груши:5 бананы:12
.

На выходе программа выводит одну строку - итоговый словарь в формате
{'фрукт1': количество1, 'фрукт2': количество2, …}
.
"""

fruits1 = input().split()
fruits2 = input().split()

fruits1.extend(fruits2)
print(fruits1)

sklad = {}
def add_fruits(fruits: list):
    global sklad
    for fruit in fruits:
        fruit_data = fruit.split(":")
        fruit_name = fruit_data[0]
        fruit_count = fruit_data[1]

        if fruit in sklad:
            sklad[fruit_name] += int(fruit_count)
        else:
            sklad[fruit_name] = int(fruit_count)

add_fruits(fruits1)

print(sklad)