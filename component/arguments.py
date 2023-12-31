import argparse

def get_args_parser():
    parser = argparse.ArgumentParser('parent parser', add_help=False)

    # general
    parser.add_argument('--keyword', default=['공고'], nargs='+', \
                        help='알람을 받고자하는 키워드를 입력합니다.')
    parser.add_argument('--mode', default='announce', choices=['announce', 'news', 'employment'], type=str, \
                        help='키워드를 얻고자 하는 분야를 선택합니다. (available : 공지사항, 뉴스, 취업정보)')
    parser.add_argument('--period', default=10, type=int, \
                        help='얻고자하는 데이터의 기간(일)을 설정합니다. 설정된 기간보다 오래된 데이터는 수집하지 않습니다.')
    parser.add_argument('--output_dir', default='result', type=str, \
                        help='결과의 저장 경로입니다.')
    parser.add_argument('--chrome_version', default='116.0.5845.96', type=str, \
                        help='사용하고 있는 크롬의 버전을 입력합니다.')
    parser.add_argument('--debug', default=False, action='store_true', \
                        help='디버깅용')

    # announce
    parser.add_argument('--name', default='jnu', type=str, \
                        help='공지사항을 불러올 대학 이름을 설정합니다.')

    # 요약모델
    parser.add_argument('--no_summarize', default=False, action='store_true', \
                        help='해당 옵션을 사용하면 문서요약 기능이 작동하지 않습니다..')
    
    return parser