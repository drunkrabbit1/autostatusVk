from multiprocessing.dummy import Array

import vk_api
import time
from random import randint
import json

"""
Описание:
1. Подключения объекта к пользлователю
2. Json монипуляции
  2.1 Подключения json_file
  2.2 Аторизация пользователя
  2.3 Методы
"""


def exceptions_captcha():
    return vk_api.exceptions.Captcha


def anti_captcha(min):
    time.sleep(min * 60)


class AutoStatus:
    vk = vk_api

    def __init__(self, token):
        self.deleted_id = []
        self.token = token
        self.vk = vk_api.VkApi(token=token)

    def error(self):
        print('error')
        return self

    def json_file(self, name='base.json'):
        base = open(name)
        self.json = json.loads(base.read())
        return self

    def user(self, name):
        self.user_name = name
        return self

    def status_set_text(self):
        rand = randint(0, len(self.json[self.user_name]) - 1)  # рандомное число
        self.vk.method("status.set", {"text": self.json[self.user_name][rand]['text']})

    def friends_deactivated(self):
        friends = self.vk.method("friends.get", values={'fields': 'nickname'})
        for friend in friends['items']:
            if 'deactivated' in friend:
                self.deleted_id.append(friend['id'])
        return self

    def delete(self):
        if not len(self.deleted_id) == 0:
            for id_user in self.deleted_id:
                self.vk.method("friends.delete", values={'user_id': id_user})
