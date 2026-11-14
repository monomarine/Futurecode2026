"""
Дана строка URL. Используя найдите и извлеките
имя домена (между :// и первым /).

С помощью преобразуйте извлеченное имя в нижний регистр
и удалите из него все точки (.).
"""

url = "https://kb.cifUUUium.ru/lessons/13866/tasks/1244651"


start_index = url.find("://") + 3
end_index = url.find("/", 8)

domain = url[start_index:end_index].lower().replace(".", "")
print(domain)
