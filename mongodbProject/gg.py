from Users_db import *
from Airs_db import *

# тестовые значения
user = {"_id": 1, "name": "hyu", "surname": "megahyu"}
air = {}

# массив с выбором класса(в них определяется коллекция для добавления)
base = [Users_database(), Airs_database()]
# 0 или 1 - это пользователи или самолёты, надо будет написать принцип выбора того или иного класса в зависимости
# от того, что мы хотим добавлять
typeOfRole = 0

#
# тест работы методов
#
id = 6
#
# base[typeOfRole].add(base[typeOfRole].collection, user)
#
# base[typeOfRole].update(base[typeOfRole].collection, id, "name", "Hyu")
#
base[typeOfRole].delete(base[typeOfRole].collection, 10)
#
# print(base[typeOfRole].returnElement(base[typeOfRole].collection, id))
#
# base[typeOfRole].search(base[typeOfRole].collection, "admin", "admin")
# поиск производится по имени и фамилии пока что в дальнейшем заменим на пароль\логин.
# 1й элемент - имя, 2й элемент - отчество

# print(base[typeOfRole].countElements(base[typeOfRole].collection))