from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import User

from multiprocessing import Process
from .notice import notice_main
from .crawler import crawler_main

#새로운 프로세스를 생성하는 함수 proc1 = 알림, proc2 = 크롤러
def proc1_main():
    global proc1
    proc1 = Process(target=notice_main)
    print('start notice')
    proc1.start()
    print('done')   

def proc2_main():
    global proc2
    proc2 = Process(target=crawler_main)
    print('start crawler')
    proc2.start()
    print('done')

# 새로운 알림이 생성되었을 때 신호를 전달받고, 프로세스 종료절차를 밟은 후 재실행하는 함수
@receiver(post_save, sender=User.interval)
def new_notification_handler(sender, instance, **kwargs):
    print("Cancelling current notification loop...")
    if proc1.is_alive():
        print("Terminating the current notification loop...")
        proc1.close()
        print("Starting a new notification loop...")
        proc1_main()