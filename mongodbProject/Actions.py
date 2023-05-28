class Actions:
    def __init__(self, *objects):
        pass
# добавление нового элемета(пользователя/самолёта) в базу
    def add(self, *args):
        # коллекция для изменения - args[0]
        # данные в args[1] добавляются в виде json - объект для добавления
        args[0].insert_one(args[1])

# обновление значения в элементе(какого-то одного)
    def update(self, *args):
        # id - args[1]
        # что меняем - args[2] (поле для изменения)
        # новое значение - args[3]
        # коллекция для изменения - args[0]
        args[0].update_one({'_id': args[1]}, {'$set': {args[2]: args[3]}})

# удаление элемента коллекции
    def delete(self, *args):
        # коллекция для изменения - args[0]
        # id - args[1]
        args[0].delete_one({"_id": args[1]})

# вернуть элемент коллекции в формате json
    def returnElement(self, *args):
        # коллекция для изменения - args[0]
        # id - args[1]
        s = args[0].find_one({"_id": args[1]})
        return s

    def search_authorization(self, *args):
        # коллекция для изменения - args[0]
        # id - args[1]
        s = args[0].find_one({"login": args[1], "password": args[2]})
        return s

    def search_login(self, *args):
        # коллекция для изменения - args[0]
        # id - args[1]
        s = args[0].find_one({"login": args[1]})
        return s

    def search_email(self, *args):
        # коллекция для изменения - args[0]
        # id - args[1]
        s = args[0].find_one({"email": args[1]})
        return s

    def countElements(self, *args):
        # коллекция для изменения - args[0]
        s = args[0].count_documents({})
        return s
