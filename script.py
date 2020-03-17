from auto_status import AutoStatus

tkn = 'fb9de23c1ced0607334808e92e4e2de1b5fb2817b6cfff7a9e4f7436afaefcf65898f76f8b99a1659e9bf'
object1 = AutoStatus(token=tkn).json_file(name='base.json').user(name='fallen')

while True:
    object1.status_set_text()
    object1.anti_captcha(240)
