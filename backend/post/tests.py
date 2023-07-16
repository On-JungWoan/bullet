from django.test import TestCase
# result/announce_jnu.json 으로부터 뉴스 데이터를 추출해오는지 테스트
class SavePost_test(TestCase):
    
    #test실행시 최초 1회 실행되는 함수. 테스트 데이터를 생성할 때 사용
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data             for all class methods.")
        pass

    #test실행때마다 실행되는 함수. 여러개의 테스트를 수행할 때, 수행 전에 실행되는 함수
    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    #test를 수행하는 함수
    def test_pullNewPost(self):
        import json
        import os
        from .forms import PostCreateForm
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
        
        if form.is_valid():
            print("데이터가 유효합니다.")
            form.save(commit=False)