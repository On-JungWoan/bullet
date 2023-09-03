import sys
import os
from config.settings import CRAWLING_PATH, TIME_ZONE
from apscheduler.schedulers.background import BackgroundScheduler
import logging
from .models import Notification
import datetime
import asyncio

from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import User

logger = logging.getLogger(__name__)
# class Command(BaseCommand):
def crawler():
    print("crawler")
    crawling_path = os.path.join(CRAWLING_PATH, 'crawling.py') 
    os.system(f'python {crawling_path}')

def start():
    scheduler=BackgroundScheduler()
    scheduler.remove_all_jobs()
    scheduler.add_job(
        crawler,
        'interval',
        minutes = 2,
        id="crawler",
        misfire_grace_time=60,
        replace_existing=True,
    )
    try:
        logger.info("Starting scheduler...")
        scheduler.start()
        print(scheduler.get_jobs())
    except KeyboardInterrupt:
        logger.info("Stopping scheduler...")
        scheduler.shutdown()
# class Command(BaseCommand):
#   help = "Runs APScheduler."

#   def handle(self, *args, **options):
#     scheduler = BlockingScheduler(timezone=TIME_ZONE)
#     scheduler.add_jobstore(DjangoJobStore(), "default") 

#     scheduler.add_job(
#         crawler,
#         trigger=CronTrigger(minute="*/5"),  # Every 10 seconds
#         id="my_job",  # The `id` assigned to each job MUST be unique
#         max_instances=3,
#         replace_existing=True,
#         )
#     try:
#         logger.info("Starting scheduler...")
#         scheduler.start()
#     except KeyboardInterrupt:
#         logger.info("Stopping scheduler...")
#         scheduler.shutdown()
#         logger.info("Scheduler shut down successfully!")


      
# # #background에서 주기적으로 실행되는 함수
# def cronMethod(method, term=0.5):
#     sch = BackgroundScheduler()
#     # 1분마다 실행
#     sch.add_job(method, 'interval', minutes=term, id='crontab')
#     sch.start()

# #app이 시작할 때 작동함.
# def backgroundApp():
#     cronMethod(crawler, 100)

# 비동기 루프 객체
async_loop = asyncio.get_event_loop()

async def main():
    proc = await asyncio.create_subprocess_shell(
        send_notification,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{send_notification!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')

# 새로운 알림이 생성되었을 때 호출될 신호 처리 함수
@receiver(post_save, sender=User.interval)
def new_notification_handler(sender, instance, **kwargs):
    global async_loop

    if async_loop.is_running():
        print("Cancelling current notification loop...")
        async_loop.stop()
        async_loop = asyncio.new_event_loop()

    print("Starting a new notification loop...")
    asyncio.set_event_loop(async_loop)
    async_loop.run_until_complete(main())

def start_notification_loop():
    print("Starting the initial notification loop...")
    asyncio.run(main())