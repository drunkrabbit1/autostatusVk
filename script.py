from auto_status import AutoStatus, anti_captcha

tkn1 = 'fb9de23c1ced0607334808e92e4e2de1b5fb2817b6cfff7a9e4f7436afaefcf65898f76f8b99a1659e9bf'
# tkn2 = ''
object1 = AutoStatus(token=tkn1).json_file(name='base.json').user('fallen')
# object2 = AutoStatus(token=tkn2).json_file(name='base.json').user(name='None')

while True:
    object1.status_set_text()
    # object2.status_set_text()
    anti_captcha(240)
