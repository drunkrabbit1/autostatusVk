
import vk_api # Импорт библиотеке vk api
import time
from random import randint
import json

tkn='fb9de23c1ced0607334808e92e4e2de1b5fb2817b6cfff7a9e4f7436afaefcf65898f76f8b99a1659e9bf'
while True: # Запускаем бесконечный цикл
    vk = vk_api.VkApi(token=tkn) # вот здесь нужно вписать ваш acces token.
    prefix = open('base.txt')
    data = prefix.readlines()
    rand = randint(0, len(data) - 1)
    vk.method("status.set", {"text": data[rand]}) # указано содержимое статуса.
    time.sleep(120) # анти-каптча. Погружает скрипт в «сон» на 30 секунд
