import sys
import os
from django.core.management.base import BaseCommand
from config.settings import CRAWLING_PATH, TIME_ZONE
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
import logging

logger = logging.getLogger(__name__)
# class Command(BaseCommand):
def crawler():
    print("crawler")
    crawling_path = os.path.join(CRAWLING_PATH, 'crawling.py') 
    os.system(f'python {crawling_path}')

def start():
    scheduler=BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
    scheduler.remove_all_jobs()
    scheduler.add_job(
        crawler,
        'interval',
        minutes = 1,
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
