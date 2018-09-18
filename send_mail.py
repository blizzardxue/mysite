import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':
    print("send mail now!")
    send_mail(
        '来自黎志学的会议通知',
        '请按时参加周日举行的会议，总经理有重要指示发布',
        'blizzard_xue@sina.com',
        ['360959752@qq.com', 'blizzard_xue@sina.com', '13923727561@139.com'],
    )