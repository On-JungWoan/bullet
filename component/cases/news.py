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
        
# 한겨레
class hani(news):
    def __init__(self):
        super().__init__(
                       date_pat= f'//*[@id="section-left-scroll-in"]/div[3]/div[****PAT****]/div/p/span/text()',
                       title_pat=f'//*[@id="section-left-scroll-in"]/div[3]/div[****PAT****]/div/h4/a',
                       notice_path='https://www.hani.co.kr/arti/list.html',
                       next_btn='//*[@id="section-left-scroll-in"]/div[4]/a[****PAT****]',
                       date_format='%Y-%m-%d %H:%M')

# 중앙일보
class joongang(news):
    def __init__(self):
        super().__init__(
                       date_pat= f'//*[@id="story_list"]/li[****PAT****]/div/div/p/text()',
                       title_pat=f'//*[@id="story_list"]/li[****PAT****]/div/h2/a',
                       notice_path='https://www.joongang.co.kr/politics',
                       next_btn='//*[@id="container"]/section/div[3]/section/nav/ul/li[****PAT****]/a',
                       date_format='%Y.%m.%d %H:%M')


# YTN
class ytn(news):
    def __init__(self):
        super().__init__(
                       date_pat= f'//*[@id="nav_content"]/div[1]/ul/li[****PAT****]/a/div/div/span[1]/text()',
                       title_pat=f'//*[@id="nav_content"]/div[1]/ul/li[****PAT****]/a/div/span',
                       href_pat=f'//*[@id="nav_content"]/div[1]/ul/li[****PAT****]/a',
                       notice_path='https://www.ytn.co.kr/news/list.php?mcd=0101',
                       next_btn='//*[@id="nav_content"]/div[2]/a[****PAT****]',
                       date_format='%Y-%m-%d %H:%M')