"""
Дан список чисел [3, 1, 2, 3, 4, 1, 5]. Удалите все дубликаты
Структура: set (для проверки) + list (для результата).
"""


shop_items = {"древесина", "кирпич", "стекло", "топор", "мотыга", "кирка", "каска", "отвертка"}
player_inventory = {"кирка", "древесина"}

print("введите название предмета для покупки")
item = input()

if item in shop_items and not  item in player_inventory:
    print(f"покупка товара '{item}' успешна")
    player_inventory.add(item)
    print("состав вашего инвентаря:")
    print(player_inventory)
elif item in player_inventory:
    print("невозможно купить товар дважды.")
else:
    print("название товара не распознано")
