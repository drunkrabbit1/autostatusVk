
import vk_api # Импорт библиотеке vk api
import time
from random import randint
import json

tkn='fb9de23c1ced0607334808e92e4e2de1b5fb2817b6cfff7a9e4f7436afaefcf65898f76f8b99a1659e9bf'
base = open('base.json')
jsonData = json.loads(base.read())

while True: # Запускаем бесконечный цикл
    vk = vk_api.VkApi(token=tkn) # вот здесь нужно вписать ваш acces token.
    rand = randint(0, len(jsonData['prefix']) - 1) # рандомное число
    # указано содержимое статуса.
    vk.method("status.set", {"text": jsonData['prefix'][rand]['text']})
    time.sleep(120) # анти-каптча. Погружает скрипт в «сон» на 120 секунд
