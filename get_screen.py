#Метод для генерации имени скриншота и путь сохранения

from uuid import uuid4


path = '/home/dekart/python/Autotests/Screen/'

def generate_name_screen():
    filename = f"screenshot-{uuid4()}.png"
    return filename



