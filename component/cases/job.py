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
        