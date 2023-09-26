from . import CrawlFormat as job

# 워크넷
class work(job):
    def __init__(self):
        super().__init__(
                       date_pat='//*[@id="list****PAT****"]/td[5]/div/p[2]/text()',
                       title_pat='//*[@id="list****PAT****"]/td[3]/div/div/a',
                       notice_path='https://www.work.go.kr/empInfo/themeEmp/themeEmpInfoSrchList.do?occupation=&currentUri=%2FempInfo%2FthemeEmp%2FthemeEmpInfoSrchList.do&webIsOut=&bookmarkTargetId=&thmaHrplCd=S00074&resultCnt=10&notSrcKeyword=&isEmptyHeader=&_csrf=4e558b99-2e05-41c6-a22c-a1e046d9985c&currntPageNo=9&listCookieInfo=DTL&isChkLocCall=&pageIndex=1&selTheme=S00074&sortField=DATE&moerButtonYn=&themeListidx=4&keyword=&region=&sortOrderBy=DESC',
                       next_btn='//*[@id="frm"]/div[3]/nav/a[****PAT****]',
                       date_format='%y/%m/%d')


# 링커리어
class linkareer(job):
    def __init__(self):
        super().__init__(
                       date_pat='//*[@id="simple-tabpanel-0"]/div/div[2]/table/tbody/tr[****PAT****]/td[5]/p/text()',
                       title_pat='//*[@id="simple-tabpanel-0"]/div/div[2]/table/tbody/tr[****PAT****]/td[3]/div/a/p',
                       href_pat='//*[@id="simple-tabpanel-0"]/div/div[2]/table/tbody/tr[****PAT****]/td[3]/div/a',
                       notice_path='https://community.linkareer.com/community',
                       next_btn='//*[@id="simple-tabpanel-0"]/div/div[5]/ul/li[****PAT****]/a',
                       date_format='%Y.%m.%d')


# 잡코리아
class jobkorea(job):
    def __init__(self):
        super().__init__(
                       date_pat='//*[@id="content"]/div[1]/div[3]/ul/li[****PAT****]/div[2]/div[1]/span[3]/text()',
                       title_pat='//*[@id="content"]/div[1]/div[3]/ul/li[2]/div[2]/a/div[1]/span',
                       href_pat='//*[@id="content"]/div[1]/div[3]/ul/li[2]/div[2]/a',
                       notice_path='https://www.jobkorea.co.kr/User/Qstn/Index',
                       next_btn='//*[@id="simple-tabpanel-0"]/div/div[5]/ul/li[****PAT****]/a',
                       date_format='%Y-%m-%d 작성')


# 사람인
class saramin(job):
    def __init__(self):
        super().__init__(
                       date_pat='//*[@id="qst_and_ans_list"]/div[1]/li[****PAT****]/div[2]/div/span/text()',
                       title_pat='//*[@id="qst_and_ans_list"]/div[1]/li[2]/a',
                       notice_path='https://www.saramin.co.kr/zf_user/company-review-qst-and-ans/sub?page=1',
                       next_btn='//*[@id="qst_and_ans_list"]/div[****PAT****]/a[1]',
                       date_format='%Y-%m-%d')