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



# 전남대학교
class jnu(university):
    def __init__(self):
        super().__init__(
                       date_pat= f'//*[@id="grvw_board_list"]/tbody/tr[****PAT****]/td[4]/text()',
                       title_pat=f'//*[@id="ctl00_ctl00_ContentPlaceHolder1_PageContent_ctl00_rptList_ctl****PAT****_hy_Title"]',
                       notice_path='https://www.jnu.ac.kr/WebApp/web/HOM/COM/Board/board.aspx?boardID=5',
                       next_btn='//*[@id="ctl00_ctl00_ContentPlaceHolder1_PageContent_pnlBoard"]/div[3]/ul/li[8]/a',
                       parent_path='https://www.jnu.ac.kr/',
                       date_format='%Y-%m-%d')

    @staticmethod
    def special_func(tree, idx):
        """
        앞에 공지딱지 걸러내는 함수임
        """
        is_announce = tree.xpath(f'//*[@id="ctl00_ctl00_ContentPlaceHolder1_PageContent_ctl00_rptList_ctl{idx:02}_lbl_RowNum"]')[0]
        is_announce = is_announce.text == '공지'
        msg = 'announce skip'

        return is_announce, msg, None
    

# 유니스트 대학원 공지사항
class grad_unist(university):
    def __init__(self):
        super().__init__(
            date_pat=f'//*[@id="post-23"]/div/table/tbody/tr[****PAT****]/td[1]/div/div/span[2]/text()',
            title_pat=f'//*[@id="post-23"]/div/table/tbody/tr[****PAT****]/td[1]/a',
            notice_path='https://adm-g.unist.ac.kr/category/info/notice/',
            next_btn='//*[@id="post-23"]/div/div[2]/ul/li[6]/a',
            date_format='%Y.%m.%d')