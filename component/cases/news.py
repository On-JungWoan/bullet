class university:
    def __init__(
            self, date_pat:str, title_pat:str, notice_path:str,
            next_btn:str, date_format:str, href_pat:str=None, parent_path:str='',
        ):
        self.parent_path = parent_path
        self.notice_path = notice_path
        self.next_btn = next_btn
        self.date_format = date_format

        title = f'{title_pat}/text()'
        href = f'{title_pat}/@href' if href_pat is None else f'{href_pat}/@href'

        self.pat = {
            'DATE_PAT' : date_pat,
            'TITLE_PAT' : title,
            'HREF_PAT' : href
        }
        
    @staticmethod
    def special_func(tree, idx):
        return False, None, None


# 연합뉴스
class yna(university):
    def __init__(self):
        super().__init__(
                       date_pat= f'//*[@id="container"]/div/div/div[1]/section/div[1]/ul/li[****PAT****]/div/div[1]/span[2]/text()',
                       title_pat=f'//*[@id="container"]/div/div/div[1]/section/div[1]/ul/li[****PAT****]/div/div[2]/a/strong',
                       href_pat=f'//*[@id="container"]/div/div/div[1]/section/div[1]/ul/li[****PAT****]/div/div[2]/a',
                       notice_path='https://www.yna.co.kr/news?site=navi_latest_depth01',
                       next_btn='//*[@id="container"]/div/div/div[1]/section/div[2]/a[****PAT****]',
                       date_format='%m-%d %H:%M')