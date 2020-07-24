from auto_status import AutoStatus, anti_captcha, exceptions_captcha

tkn1 = ''
tkn2 = ''

object1 = AutoStatus(token=tkn1).json_file().user('fallen')
object2 = AutoStatus(token=tkn2).json_file().user('none')

while True:
    object1.status_set_text()
    object2.status_set_text()
    anti_captcha(6)
