data = []

text = input("введите данные для добавления. 0 - остановка ввода >> ")
while text != "0":
    data.append(text)
    text = input("введите данные для добавления. 0 - остановка ввода >> ")

print("Информация по данным:")
print(f"количество введенных данных  - {len(data)}")
print(f"самое длинный текст в списке - {max(data, key=len)}")
print(f"самое короткий текст в списке - {max(data, key=lambda x: -len(x))}")

data1 = data.pop(0)
print(data)