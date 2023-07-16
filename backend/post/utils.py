import json
import os
from .forms import PostCreateForm
from apscheduler.schedulers.background import BackgroundScheduler
#새로운 뉴스를 끌고 오는 함수
def savePost():
        # 상위의 상위의 경로 가져오기
        parent_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        # 상위 디렉토리에서 한 단계 아래 디렉토리의 경로 만들기
        announce_path = os.path.join(parent_path,'result\\announce_jnu.json')
        #raw string으로 표현
        path_string = r'{}'.format(announce_path)

        with open(path_string) as f:
            jsonData = json.load(f)

        #전달받은 json객체를 폼에 대입
        form = PostCreateForm()
        form.title = jsonData['title']
        form.content = "요약데이터가 들어갈 공간입니다."
        form.url = jsonData['href']
        form.date = jsonData['date']
        
        print(form)
        #외래키를 위한 site, keyword 데이터가 없어 지금은 유효하지 않음
        if form.is_valid():
            print("데이터가 유효합니다.")
            form.save(commit=False)

#background에서 주기적으로 실행되는 함수
def cronMethod(method, term=1):
    sch = BackgroundScheduler()
    # 1분마다 실행
    sch.add_job(method, 'interval', minutes=term, id='crontab')
    sch.start()

#app이 시작할 때 작동함.
def backgroundApp():
    cronMethod(savePost, 100)
