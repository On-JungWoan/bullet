import sys
import os
from django.core.management.base import BaseCommand
from apscheduler.schedulers.background import BackgroundScheduler
from config.settings import BASE_DIR
# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         # 상위의 상위의 경로 가져오기
#         parent_path = BASE_DIR.parent
#         # 상위 디렉토리에서 한 단계 아래 디렉토리의 경로 만들기
#         sys.path(0, os.path.join(parent_path, 'component'))
#         import crawling.main
        


# #background에서 주기적으로 실행되는 함수
# def cronMethod(method, term=1):
#     sch = BackgroundScheduler()
#     # 1분마다 실행
#     sch.add_job(method, 'interval', minutes=term, id='crontab')
#     sch.start()

# #app이 시작할 때 작동함.
# def backgroundApp():
#     cronMethod(savePost, 100)
