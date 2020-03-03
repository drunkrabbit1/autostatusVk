import vk_api # Импорт библиотеке vk api
import datetime # Импорт библиотеке datetime
import time # Импорт библиотеке time

while True: # Запускаем бесконечный цикл
    vk = vk_api.VkApi(token="ваш токен") # вот здесь нужно вписать ваш acces token. Чтобы получить его перейдите на этот сюда
    delta = datetime.timedelta(hours=3, minutes=0) # разница от UTC. Можете вписать любое значение вместо «3» ставите ваш пояс.
    t = (datetime.datetime.now(datetime.timezone.utc) + delta) # Присваиваем дату и время переменной «t»
    nowtime = t.strftime("%H:%M") # текущее время
    nowdate = t.strftime("%d.%m.%Y") # текущее дата
    on = vk.method("friends.getOnline") # получаем список id друзей онлайн
    counted = len(on) # подсчет кол-ва друзей
    vk.method("status.set", {"text": nowtime + " ● " + nowdate + " ● " + "Друзей онлайн: " + str(counted)}) # указано содержимое статуса.
    time.sleep(30) # анти-каптча. Погружает скрипт в «сон» на 30 секунд