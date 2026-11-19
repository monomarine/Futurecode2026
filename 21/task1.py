'''
простое чтение файла целиком
'''

# 1 способ с ручным закрытием
f = open('data.txt')
text = f.read()
print(text)
f.close()

# 2 способ с автоматическим закрытием
with open('data.txt') as f:
    text = f.read()
    print(text)
