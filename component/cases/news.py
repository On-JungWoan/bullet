from . import CrawlFormat as news

# 연합뉴스
class yna(news):
    def __init__(self):
        super().__init__(
                       date_pat= f'//*[@id="container"]/div/div/div[1]/section/div[1]/ul/li[****PAT****]/div/div[1]/span[2]/text()',
                       title_pat=f'//*[@id="container"]/div/div/div[1]/section/div[1]/ul/li[****PAT****]/div/div[2]/a/strong',
                       href_pat=f'//*[@id="container"]/div/div/div[1]/section/div[1]/ul/li[****PAT****]/div/div[2]/a',
                       notice_path='https://www.yna.co.kr/news?site=navi_latest_depth01',
                       next_btn='//*[@id="container"]/div/div/div[1]/section/div[2]/a[****PAT****]',
                       date_format='%m-%d %H:%M')