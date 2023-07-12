import argparse
from lxml import html
from typing import Tuple
from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By

from arguments import get_args_parser
from utils import pat_post_process, load_chrome_driver, prepare


def special_func(tree:html, idx:int) -> Tuple():
    is_announce = tree.xpath(f'//*[@id="ctl00_ctl00_ContentPlaceHolder1_PageContent_ctl00_rptList_ctl{idx:02}_lbl_RowNum"]')[0]
    is_announce = is_announce.text == '공지'
    msg = 'announce skip'

    return is_announce, msg, None


def test_eight_components(obj,
        driver:webdriver, tree:html, page_num:int, target_day:int
    ) -> Tuple[int, bool]:
    TARGET_DAY = args.target_day

    NOTICE_PATH = 'https://www.jnu.ac.kr/WebApp/web/HOM/COM/Board/board.aspx?boardID=5'
    DATE_PAT = f'//*[@id="grvw_board_list"]/tbody/tr[****PAT****]/td[4]/text()'
    TITLE_PAT = f'//*[@id="ctl00_ctl00_ContentPlaceHolder1_PageContent_ctl00_rptList_ctl****PAT****_hy_Title"]/text()'
    HREF_PAT = f'//*[@id="ctl00_ctl00_ContentPlaceHolder1_PageContent_ctl00_rptList_ctl****PAT****_hy_Title"]/@href'

    idx = 1

    while True:
        try:
            is_skip, return_msg, return_value = special_func(tree, idx)
            if is_skip:
                print(return_msg)
                idx += 1
                continue

            # get details of announcement
            date = tree.xpath(pat_post_process(DATE_PAT, f'{idx:02}'))[0]
            date = datetime.strptime(str(date), '%Y-%m-%d')
            title = tree.xpath(pat_post_process(TITLE_PAT, f'{idx:02}'))[0]
            title_href = tree.xpath(pat_post_process(HREF_PAT, f'{idx:02}'))[0]
            title_href = 'https://www.jnu.ac.kr/' + title_href
            
            margin_date = datetime.now() - timedelta(days=TARGET_DAY)
            if date < margin_date:
                return page_num, True

            print(title, date, title_href)
            idx += 1
        except:
            next_btn = driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ctl00_ContentPlaceHolder1_PageContent_pnlBoard"]/div[3]/ul/li[8]/a')
            next_btn.click()

            return page_num + 1, False


def main(args):
    obj = prepare(args)

    # get announcement page
    driver = load_chrome_driver(args.chrome_version)
    driver.get(obj.notice_path)
    driver.implicitly_wait(0.5)

    page_num = 1
    is_done = False

    while not is_done:
        # get page source
        page = driver.page_source
        tree = html.fromstring(page)

        page_num, is_done = test_eight_components(driver, obj, tree, page_num, args.target_day)

    driver.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser('pipeline script', parents=[get_args_parser()])
    args = parser.parse_args()
    main(args)
    pass