# 0 - Низкий приоритет
# 1 - средний приоритет
# 2 - высокий приоритет
presents = [
    ['Lego', 1, 1500],
    ['3d принтер', 0, 30000],
    ['машина', 2, 2000],
    ['барби', 0, 500],
]

filters_presents = list(filter(lambda p: p[1] == 1, presents) )
filters_presents2 = list(filter(lambda p: p[2] >= 1000, presents) )

print("подарки со средним приоритетом: ")

for p in filters_presents:
    print(p[0], end=', ')


print("\nподарки дороже 1000 р:")
for p in filters_presents2:
    print(p[0], end=', ')

