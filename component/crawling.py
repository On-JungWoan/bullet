import os
import sys
import json
import argparse
from lxml import html
from typing import Tuple
from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By

import requests
from bs4 import BeautifulSoup
from summarize import summarize

sys.path.append('.')
from backend.decorators import dataIO
from arguments import get_args_parser
from utils import pat_post_process, load_chrome_driver, prepare


def crawling(args, obj,
        driver:webdriver, tree:html, page_num:int, res:dict
    ) -> Tuple[int, bool, dict]:

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
            date, title, title_href = pat_post_process(tree=tree, idx=idx, **obj.pat)
            date = datetime.strptime(str(date), obj.date_format)

            if date.year == 1900:
                date = date.replace(datetime.now().year)

            title_href = obj.parent_path + title_href
                
            margin_date = datetime.now() - timedelta(days=args.period)
            if date < margin_date:
                return page_num, True, res

            filter_res = sum([key in title for key in args.keyword])
            if filter_res > 0:
                print(title)

                if args.debug:
                    print(f'[제목]{title}\n[링크] {title_href}\n[작성일자] {date}\n')

                sum_res = None
                if not args.no_summarize:
                    # bs4로 공지 내용 받아오기
                    if 'https:' not in title_href:
                        title_href = 'https:' + title_href

                    try:
                        response = requests.get(title_href)
                        if response.status_code == 200:
                            html = response.text
                            soup = BeautifulSoup(html, 'html.parser')
                            contents = soup.select_one('#articleWrap > div.content01.scroll-article-zone01 > div > div > article').text
                        else : 
                            print(response.status_code)
                        # 문서 요약하기
                        print('==== 요약 중 ====')
                        sum_res = summarize(contents)                        
                    except:
                        sum_res = title
                        title_href = title
                res[title] = {
                    'content':sum_res, 
                    'url':title_href,
                    'date':date.strftime('%Y-%m-%d'),
                    'created_at':date.strftime('%Y-%m-%d'),
                    'keyword':args.keyword[0],
                    'site':args.name,
                }
            idx += 1
        except:
            next_XPath = obj.next_btn.replace('****PAT****', str(page_num+1)) \
                if '****PAT****' in obj.next_btn \
                else obj.next_btn

            try:
                next_btn = driver.find_element(by=By.XPATH, value=next_XPath)
                next_btn.click()
            except:
                return page_num, True, res

            return page_num + 1, False, res


def get_result(args):
    print(args.name, args.keyword, args.period)    
    obj = prepare(args)

    # get announcement page
    driver = load_chrome_driver(args.chrome_version)
    # driver.options.add_argument('headless')
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
    driver.quit()

    if len(result) > 0:
        save_file = os.path.join(args.output_dir, f'{args.mode}_{args.name}_{datetime.now().strftime("%m%d_%H%M")}.json')
        with open(save_file, 'w') as f:
            json.dump(result, f)
        return result
    else:
        if args.debug:
            print('기간 내에 존재하는 데이터가 없습니다.')
        return None


@dataIO
def main(info_list:list=None)->str:
    parser = argparse.ArgumentParser('pipeline script', parents=[get_args_parser()])
    args = parser.parse_args()

    if not os.path.isdir(args.output_dir):
        os.mkdir(args.output_dir)    

    if info_list is not None:
        for info in info_list:
            args.name, args.keyword, args.period = info

            if not isinstance(args.keyword, list):
                args.keyword = [args.keyword]

            yield get_result(args)
    else:
        # for main debug
        yield get_result(args)


if __name__ == '__main__':
    main()