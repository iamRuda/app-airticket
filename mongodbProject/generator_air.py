from Users_db import *
from Airs_db import *
import random

location = ["Москва(Домодедово)", "Москва(Шереметьево)", "Москва(Внуково)", "Санкт-Петербург(Пулково)", "Анапа",
            "Барнаул", "Астрахань", "Владивосток", "Белгород", "Архангельск", "Казань", "Каллининград", "Иркутск",
            "Краснодар", "Курган", "Сочи", "Мурманск", "Нижний Новгород", "Новосибирск", "Омск", "Псков", "Самара",
            "Ставрополь", "Томск", "Тюмень", "Улан-Удэ", "Ульяновск", "Уфа", "Чита", "Якутск"]

class_ticket = ["Эконом", "Эконом", "Эконом", "Комфорт", "Комфорт", "Бизнес"]

airplane = ["МС-21", "Ил-96-300", "Ил-96-400М", "CR929", "А300 B2", "А300 B4", "А300 С4", "А300 320"]

company = ["S5", "Аэродвиж", "ОтВинта"]

base = [Users_database(), Airs_database()]
typeOfRole = 1
air = {"_id": 0, "from": None, "in": None, "date_from": None, "date_in": None, "time_from": None, "time_in": None, "class_ticket": None, "airplane": None,
        "company": None, "price": None, "miles": None}

n = 20
for i in range(n):
    air["_id"] = i
    air["from"] = location[random.randint(0, len(location) - 1)]
    air["in"] = location[random.randint(0, len(location) - 1)]
    while air["from"] == air["in"]:
        air["in"] = location[random.randint(0, len(location) - 1)]
    date = random.randint(1, 30)
    air["date_from"] = "2022/12/" + str(date)
    air["date_in"] = "2022/12/" + str(date+1)
    air["time_from"] = str(random.randint(0, 23)) + ":" + str(random.randint(0, 59))
    air["time_in"] = str(random.randint(0, 23)) + ":" + str(random.randint(0, 59))
    air["class_ticket"] = class_ticket[random.randint(0, len(class_ticket) - 1)]
    air["airplane"] = airplane[random.randint(0, len(airplane) - 1)]
    air["company"] = company[random.randint(0, len(company) - 1)]
    air["price"] = random.randint(50, 100) * 100
    air["miles"] = random.randint(2, 8) * 100
    base[typeOfRole].add(base[typeOfRole].collection, air)
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