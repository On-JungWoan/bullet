import os
import json
import argparse
from lxml import html
from typing import Tuple
from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By

from arguments import get_args_parser
from utils import pat_post_process, load_chrome_driver, prepare


def crawling(args, obj,
        driver:webdriver, tree:html, page_num:int, res:dict
    ) -> Tuple[int, bool, dict]:

    DATE_PAT, TITLE_PAT, HREF_PAT = [v for v in obj.pat.values()]

    idx = 1
    while True:
        try:
            is_skip, return_msg, return_value = obj.special_func(tree, idx)
            if is_skip:
                if return_msg is not None:
                    print(return_msg)
                idx += 1
                continue

            # get details of announcement
            date = tree.xpath(pat_post_process(DATE_PAT, f'{idx:02}'))[0]
            date = datetime.strptime(str(date), obj.date_format)
            title = tree.xpath(pat_post_process(TITLE_PAT, f'{idx:02}'))[0]
            title_href = tree.xpath(pat_post_process(HREF_PAT, f'{idx:02}'))[0]
            title_href = obj.parent_path + title_href
                
            margin_date = datetime.now() - timedelta(days=args.period)
            if date < margin_date:
                return page_num, True, res

            filter_res = sum([key in title for key in args.keyword])
            if filter_res > 0:
                print(title)

                if args.debug:
                    print(f'[제목]{title}\n[링크] {title_href}\n[작성일자] {date}\n')

                res[title] = {
                    'date':date.strftime(obj.date_format),
                    'href':title_href,
                }

            idx += 1
        except:
            next_XPath = obj.next_btn.replace('****PAT****', str(page_num+1)) \
                if '****PAT****' in obj.next_btn \
                else obj.next_btn

            next_btn = driver.find_element(by=By.XPATH, value=next_XPath)
            next_btn.click()

            return page_num + 1, False, res


def main(args):
    obj = prepare(args)

    # get announcement page
    driver = load_chrome_driver(args.chrome_version)
    driver.get(obj.notice_path)
    driver.implicitly_wait(0.5)

    page_num = 1
    is_done = False
    result = {}

    while not is_done:
        # get page source
        page = driver.page_source
        tree = html.fromstring(page)

        page_num, is_done, result = crawling(args, obj, driver, tree, page_num, result)

    if len(result) > 0:
        save_file = os.path.join(args.output_dir, f'{args.mode}_{args.univ_name}_{datetime.now().strftime("%m%d_%H%M")}.json')
        with open(save_file, 'w') as f:
            json.dump(result, f)
    else:
        if args.debug:
            print('기간 내에 존재하는 데이터가 없습니다.')
    driver.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser('pipeline script', parents=[get_args_parser()])
    args = parser.parse_args()

    if not os.path.isdir(args.output_dir):
        os.mkdir(args.output_dir)

    main(args)