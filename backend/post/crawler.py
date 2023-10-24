import os
from config.settings import CRAWLING_PATH
from apscheduler.schedulers.background import BackgroundScheduler
import logging

logger = logging.getLogger(__name__)

sched = BackgroundScheduler()

def crawler():
    print("crawler")
    crawling_path = os.path.join(CRAWLING_PATH, 'crawling.py') 
    os.system(f'python {crawling_path}')

def crawler_main():
    print("crawler_main")
    scheduler= BackgroundScheduler(daemon=True, timezone='Asia/Seoul')
    
    scheduler.add_job(
        crawler,
        'interval',
        seconds=60,
        id="crawler",
        misfire_grace_time=60,
        replace_existing=True,
    )

    scheduler.start()
