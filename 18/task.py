from random import randint

enemies = [85,50,100,45,35,100,42]

player_damage = randint(100,500)

def TakeDamage( damage):
    global enemies
    unit_of_damage = damage // len(enemies)
    for i in range (len(enemies)):
        enemies[i] -= unit_of_damage

    enemies = list(filter(lambda x: x > 0, enemies))

count = 1
while len(enemies) > 0:
    print(f"игрок нанес урон на {player_damage} единиц")
    TakeDamage( player_damage)
    print(f"нанесен {count} удар")
    count += 1
    print(enemies)