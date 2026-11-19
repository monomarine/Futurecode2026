from pathlib import Path

print("Введите путь к каталогу для анализа файлов")
path = input()

for item in Path(path).iterdir():
    if item.is_file() :
        print(f"{item.name:10}\t{item.stat().st_size / 1024 / 1024} Mb");