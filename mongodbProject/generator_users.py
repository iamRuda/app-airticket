from Users_db import *
from Airs_db import *
import random

login = ["arabadai", "markkipler", "otzovik", "uwu12345", "gorodow", "morkovka", "huinjuly", "ridik666", "olaola234",
         "gogogaga", "mahachlapa", "utyrwqa", "lol00000", "wewewe", "checkpoint", "piraniya", "uno777", "shasha0123",
         "monanona", "racooncity", "uoi5432", "boriska", "casper", "jackjack", "petrolfull", "qwerty01", "pwrwlol",
         "carmapol", "infograph", "kokoroch", "jullyya", "andurun", "hackhack", "partymaker", "dancer00", "igrushka",
         "pooooow", "lolipop", "kukuruza", "lambaba", "uhulua", "pythonist", "javaroper", "cpluplu", "cashier", "admin"]

password = ["goofgoof", "meowmeow", "0123456789", "ogoogotut", "tuttop", "killcomp", "mashik", "doshik", "port127",
            "ururun", "burmister", "burger", "pizzalol", "markupbit", "bitlider", "hypepipe", "lookme", "kgkwpopa",
            "shikshik", "cuckrise", "kolakola", "shakermaker", "cellweider", "pogyst", "mongodb", "pippython",
            "julejack", "magicrobe", "hyliopass", "goofgoog", "yoyoten", "elonmask", "polygon", "lupapupa", "uwuuwu"]

email = ["@gmail", "@yandex", "@rambler", "@yahoo", "@bing", "@mail", "@signal"]

role = ["user" for i in range(20)] + ["cashier" for i in range(2)]
random.shuffle(role)
role = ["admin", "cashier"] + role

name = ["Артур", "Роман", "Анна", "Константин", "Руслан", "Николай", "Анастасия", "Юлия", "Ольга", "Армен", "Андрей",
        "Екатерина", "Мария", "Джек", "Полина", "Питер", "Катерина", "Зоя", "Григорий", "Марта", "Елена", "Фёдор"]

surname = ["Комолов", "Иванов", "Петров", "Козлов", "Катаев", "Карпов", "Коммисаров", "Бахтин", "Сабуров", "Лутак",
           "Волков", "Зайцев", "Львов", "Коваль", "Гагарин", "Юн", "Порус", "Кабо", "Замятин", "Носков", "Моу",
           "Хокшоу", "Веневцев", "Юрасов", "Труневы", "Зимин", "Рябов", "Троекуров", "Руденко", "Ромашка"]

patronymic = ["Сергеевич", "Андреевич", "Дмитриевич", "Егоров", "Михайлович", "Николаевич", "Борисович", "Владимирович",
              "Максимович", "Георгиевич", "Витальевич"]

base = [Users_database(), Airs_database()]
typeOfRole = 0
user = {"_id": 0, "login": None, "password": None, "email": None, "role": None, "date_registration": None, "name": None,
        "surname": None, "patronymic": None, "virtual_money": None, "points_mile": None, "myticket": {}}

n = 20
for i in range(n):
    user["_id"] = i
    user["login"] = login[random.randint(0, len(login)-1)] + str(i)
    user["password"] = password[random.randint(0, len(password)-1)] + str(i)
    user["email"] = login[random.randint(0, len(login)-1)] + str(i) + email[random.randint(0, len(email)-1)]
    if i == 0:
        user["role"] = "admin"
    elif i == 1:
        user["role"] = "cashier"
    else:
        user["role"] = role[i % len(role)-1]
    user["date_registration"] = "2022/" + str(random.randint(1, 28)) + "/" + str(random.randint(1, 28))
    user["name"] = name[random.randint(0, len(name)-1)]
    user["surname"] = surname[random.randint(0, len(surname) - 1)]
    user["patronymic"] = patronymic[random.randint(0, len(patronymic) - 1)]
    if user["role"] == "user":
        user["virtual_money"] = random.randint(50, 200)*100
        user["points_mile"] = random.randint(0, 10)*100
    base[typeOfRole].add(base[typeOfRole].collection, user)

#
# base[typeOfRole].update(base[typeOfRole].collection, id, "name", "Hyu")
#
# base[typeOfRole].delete(base[typeOfRole].collection, id)
#
# base[typeOfRole].returnElement(base[typeOfRole].collection, id)
#
# base[typeOfRole].search(base[typeOfRole].collection, "admin", "admin")
# поиск производится по имени и фамилии пока что в дальнейшем заменим на пароль\логин.
# 1й элемент - имя, 2й элемент - отчество