import vk_api # Импорт библиотеке vk api
import datetime # Импорт библиотеке datetime
import time # Импорт библиотеке time
from random import randint

while True: # Запускаем бесконечный цикл
    vk = vk_api.VkApi(token="4f8ad799b1cfbbf23ad4829a97f8840c88a3c1cc6b37f85521c896845a65c5fdd247f73bf859ddf8a111a") # вот здесь нужно вписать ваш acces token. Чтобы получить его перейдите на этот сюда
    delta = datetime.timedelta(hours=3, minutes=0) # разница от UTC. Можете вписать любое значение вместо «3» ставите ваш пояс.
    prefix = open('base.txt')
    data = prefix.readlines()
    rand = randint(0, len(data) - 1)
    vk.method("status.set", {"text": data[rand]}) # указано содержимое статуса.
    time.sleep(60) # анти-каптча. Погружает скрипт в «сон» на 30 секунд
