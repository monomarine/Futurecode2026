enemyes = [100, 50, 100, 50, 10, 100, 20, 100]

player_power = 452

power_unit = player_power // len(enemyes)

for i in range(len(enemyes)):
    enemyes[i] -= power_unit

enemyes = list(filter(lambda x: x > 0, enemyes))

print(f"после удара на каждого врага пришлось {power_unit} мощи")
print(f"состояние врагов после атаки:")
print(enemyes)
