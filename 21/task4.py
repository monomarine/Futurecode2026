"""
чтение и запись файлов из других каталогов
"""

from pathlib import Path    # импорт класса Path Для работы с файлами

# raw - строка - как пишется пишется так и читается
file = Path(r'D:\Test\new.txt')

text = file.read_text(encoding='utf-8')
print(text)