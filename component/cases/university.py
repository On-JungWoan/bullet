class jnu():
    def __init__(self):
        self.parent_path = 'https://www.jnu.ac.kr/'
        self.notice_path = 'https://www.jnu.ac.kr/WebApp/web/HOM/COM/Board/board.aspx?boardID=5'
        self.pat = {
            'DATE_PAT' : f'//*[@id="grvw_board_list"]/tbody/tr[****PAT****]/td[4]/text()',
            'TITLE_PAT' : f'//*[@id="ctl00_ctl00_ContentPlaceHolder1_PageContent_ctl00_rptList_ctl****PAT****_hy_Title"]/text()',
            'HREF_PAT' : f'//*[@id="ctl00_ctl00_ContentPlaceHolder1_PageContent_ctl00_rptList_ctl****PAT****_hy_Title"]/@href'
        }

    @staticmethod
    def special_func(tree, idx):
        is_announce = tree.xpath(f'//*[@id="ctl00_ctl00_ContentPlaceHolder1_PageContent_ctl00_rptList_ctl{idx:02}_lbl_RowNum"]')[0]
        is_announce = is_announce.text == '공지'
        msg = 'announce skip'

        return is_announce, msg, None