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
# FIXME: unist는 next_btn xpath가 계속 바뀜
#        바뀌는 패턴이 있어서 special_func에 정의해주면 될 듯.
class grad_unist(university):
    def __init__(self):
        super().__init__(
            date_pat='//*[@id="post-23"]/div/table/tbody/tr[****PAT****]/td[1]/div/div/span[2]/text()',
            title_pat='//*[@id="post-23"]/div/table/tbody/tr[****PAT****]/td[1]/a',
            notice_path='https://adm-g.unist.ac.kr/category/info/notice/',
            next_btn='//*[@id="post-23"]/div/div[2]/ul/li[6]/a',
            date_format='%Y.%m.%d')
        

# 전북대학교 전체 공지
class jbnu(university):
    def __init__(self):
        super().__init__(
            date_pat='//*[@id="print_area"]/div[2]/table/tbody/tr[****PAT****]/td[5]/text()',
            title_pat='//*[@id="print_area"]/div[2]/table/tbody/tr[****PAT****]/td[2]/span/a',
            parent_path='https://www.jbnu.ac.kr/kor/',
            notice_path='https://www.jbnu.ac.kr/kor/?menuID=139',
            next_btn='//*[@id="print_area"]/div[3]/a[****PAT****]',
            date_format='%Y.%m.%d')
        

# 서울대학교 일반공지
class snu(university):
    def __init__(self):
        super().__init__(
            date_pat='//*[@id="skip-content"]/div/div[2]/div[1]/table/tbody/tr[****PAT****]/td[2]/text()',
            title_pat='//*[@id="skip-content"]/div/div[2]/div[1]/table/tbody/tr[****PAT****]/td[1]/a/span[1]/span',
            href_pat='//*[@id="skip-content"]/div/div[2]/div[1]/table/tbody/tr[****PAT****]/td[1]/a',
            parent_path='https://www.snu.ac.kr',
            notice_path='https://www.snu.ac.kr/snunow/notice/genernal?page=1',
            next_btn='//*[@id="skip-content"]/div/div[2]/div[2]/div[2]/a[****PAT****]',
            date_format='%Y.%m.%d.')
        

# 충남대학교
class cnu(university):
    def __init__(self):
        super().__init__(
                       date_pat= '//*[@id="txt"]/div[1]/table/tbody/tr[****PAT****]/td[4]/text()',
                       title_pat='//*[@id="txt"]/div[1]/table/tbody/tr[****PAT****]/td[2]/a',
                       notice_path='https://plus.cnu.ac.kr/_prog/_board/?code=sub07_0701&site_dvs_cd=kr&menu_dvs_cd=0701',
                       next_btn='//*[@id="txt"]/div[3]/div/p/a[****PAT****]',
                       parent_path='https://plus.cnu.ac.kr/',
                       date_format='%Y-%m-%d')

    @staticmethod
    def special_func(tree, idx):
        """
        앞에 공지딱지 걸러내는 함수임
        """
        is_announce = tree.xpath(f'//*[@id="txt"]/div[1]/table/tbody/tr[{idx}]/td[1]')[0]
        is_announce = is_announce.text == '공지'
        msg = 'announce skip'

        return is_announce, msg, None


# 경북대학교
# TODO : 여기 날짜 버튼 idx-1 해야함
class knu(university):
    def __init__(self):
        super().__init__(
                       date_pat= '//*[@id="btinForm"]/div[1]/table/tbody/tr[****PAT****]/td[5]/text()',
                       title_pat='//*[@id="btinForm"]/div[1]/table/tbody/tr[****PAT****]/td[2]/a',
                       notice_path='https://www.knu.ac.kr/wbbs/wbbs/bbs/btin/list.action?bbs_cde=1&menu_idx=67',
                       next_btn='//*[@id="body_content"]/div[2]/a[****PAT****]',
                       parent_path='https://www.knu.ac.kr/',
                       date_format='%Y/%m/%d')

    @staticmethod
    def special_func(tree, idx):
        """
        앞에 공지딱지 걸러내는 함수임
        """
        is_announce = tree.xpath(f'//*[@id="btinForm"]/div[1]/table/tbody/tr[{idx}]/td[1]')[0]
        is_announce = is_announce.text == '공지'
        msg = 'announce skip'

        return is_announce, msg, None


# 부산대학교
class pnu(university):
    def __init__(self):
        super().__init__(
                       date_pat= '//*[@id="board-wrap"]/div[2]/table/tbody/tr[****PAT****]/td[4]/text()',
                       title_pat='//*[@id="board-wrap"]/div[2]/table/tbody/tr[****PAT****]/td[2]/p/a',
                       notice_path='https://www.pusan.ac.kr/kor/CMS/Board/Board.do?mCode=MN095',
                       next_btn='//*[@id="board-wrap"]/div[3]/div/a[****PAT****]',
                       parent_path='https://www.pusan.ac.kr/kor',
                       date_format='%Y-%m-%d')

    @staticmethod
    def special_func(tree, idx):
        """
        앞에 공지딱지 걸러내는 함수임
        """
        is_announce = tree.xpath(f'//*[@id="board-wrap"]/div[2]/table/tbody/tr[{idx}]/td[1]/img')
        len(is_announce) == 1
        msg = 'announce skip'

        return is_announce, msg, None


# 제주대학교
class jejunu(university):
    def __init__(self):
        super().__init__(
                       date_pat= '//*[@id="sub-main-contents"]/div/div[3]/table/tbody/tr[****PAT****]/td[6]/text()',
                       title_pat='//*[@id="sub-main-contents"]/div/div[3]/table/tbody/tr[****PAT****]/td[3]/a',
                       notice_path='https://www.jejunu.ac.kr/ara/noticesurvey/outEvent.htm?category=203',
                       next_btn='//*[@id="sub-main-contents"]/div/p[2]/a[****PAT****]',
                       parent_path='https://www.jejunu.ac.kr',
                       date_format='%Y-%m-%d')

    @staticmethod
    def special_func(tree, idx):
        """
        앞에 공지딱지 걸러내는 함수임
        """
        is_announce = tree.xpath(f'//*[@id="sub-main-contents"]/div/div[3]/table/tbody/tr[{idx}]/td[1]/span')
        len(is_announce) == 1
        msg = 'announce skip'

        return is_announce, msg, None


# TODO : 2023-07-24 회의록 TOTO부분 참고
# # 충북대학교, 경상대학교
# class cbnu(university):
#     def __init__(self):
#         super().__init__(
#                        date_pat= f'//*[@id="grvw_board_list"]/tbody/tr[****PAT****]/td[4]/text()',
#                        title_pat=f'//*[@id="ctl00_ctl00_ContentPlaceHolder1_PageContent_ctl00_rptList_ctl****PAT****_hy_Title"]',
#                        notice_path='https://www.jnu.ac.kr/WebApp/web/HOM/COM/Board/board.aspx?boardID=5',
#                        next_btn='//*[@id="ctl00_ctl00_ContentPlaceHolder1_PageContent_pnlBoard"]/div[3]/ul/li[8]/a',
#                        parent_path='https://www.jnu.ac.kr/',
#                        date_format='%Y-%m-%d')

#     @staticmethod
#     def special_func(tree, idx):
#         """
#         앞에 공지딱지 걸러내는 함수임
#         """
#         is_announce = tree.xpath(f'//*[@id="ctl00_ctl00_ContentPlaceHolder1_PageContent_ctl00_rptList_ctl{idx:02}_lbl_RowNum"]')[0]
#         is_announce = is_announce.text == '공지'
#         msg = 'announce skip'

#         return is_announce, msg, None