from Actions import *
from database import *

# класс для базы самолетов, здесь мы определяем какую коллекцию будем использовать,
# а все методы наследуются от класса Actions
class Airs_database(Actions):
    collection = request("airs")

    # выделяет память под объект касса
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    # инициализирует объект класса
    def __init__(self, *objects):
        super().__init__(*objects)
    # ипортируем все методы из класса Actions
