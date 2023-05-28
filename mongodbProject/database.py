import pymongo

# клиент для подключения пока локальный, надо настроить общий
db_client = pymongo.MongoClient("mongodb://localhost:27017/")
# выбор базы данных для использования, если их несколько
current_db = db_client["airtickets"]

# функция для выбора коллекции в используемой базе(исдульзуется в файлах Users_db и Airs_db)
def request(data):
    collection = current_db[data]
    return collection

