from Actions import *
from database import *

# класс для базы пользователей, здесь мы определяем какую коллекцию будем использовать,
# а все методы наследуются от класса Actions
class Users_database(Actions):
    collection = request("users")

    # выделяет память под объект касса
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    # инициализирует объект класса
    def __init__(self, *objects):
        super().__init__(*objects)
    # ипортируем все методы из класса Actions
