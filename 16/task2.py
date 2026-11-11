"""
Дана строка URL. Используя найдите и извлеките
имя домена (между :// и первым /).

С помощью преобразуйте извлеченное имя в нижний регистр
и удалите из него все точки (.).
"""

url = "https://github.com/monomarine?tab=repositories"
print(url)

index_start = url.find("://") + 3
index_end = url.find("/", 8)

domain = url[index_start:index_end]
print(domain)