import os
from config.settings import CRAWLING_PATH
from apscheduler.schedulers.background import BackgroundScheduler
import logging

logger = logging.getLogger(__name__)

def crawler():
    print("crawler")
    crawling_path = os.path.join(CRAWLING_PATH, 'crawling.py') 
    os.system(f'python {crawling_path}')

def crawler_main():
    print("crawler_main")
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