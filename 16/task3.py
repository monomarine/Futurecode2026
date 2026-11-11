"""
Дана строка с email

проверьте корректность - содержит @ (толкьо 1)
и оканчивается на ****.com
"""
email = input("введите корректный email домена gmail.com")
domain = email.split("@")[-1]

if not email.count("@") == 1:
    print("символ '@' встречается не 1 раз")
elif not domain == "gmail.com":
    print("домен не соответствует требованиям")
else:
    print("email корректный")

