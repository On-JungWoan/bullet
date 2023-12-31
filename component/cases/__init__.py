class CrawlFormat:
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

def build_obj(args):

    if args.mode=='announce':
        assert args.name is not None

        # announcement
        if args.name == 'jnu':
            from .university import jnu
            return jnu()
        elif args.name == 'grad-unist':
            from .university import grad_unist
            return grad_unist()
        elif args.name == 'jbnu':
            from .university import jbnu
            return jbnu()
        elif args.name == 'snu':
            from .university import snu
            return snu()
        elif args.name == 'cnu':
            from .university import cnu
            return cnu()
        elif args.name == 'knu':
            from .university import knu
            return knu()
        elif args.name == 'pnu':
            from .university import pnu
            return pnu()
        elif args.name == 'jejunu':
            from .university import jejunu
            return jejunu()
        
        # news
        elif args.name == 'yna':
            from .news import yna
            return yna()
        elif args.name == 'hani':
            from .news import hani
            return hani()
        elif args.name == 'joongang':
            from .news import joongang
            return joongang()
        elif args.name == 'ytn':
            from .news import ytn
            return ytn()
        elif args.name == 'chosun':
            from .news import chosun
            return chosun()
        elif args.name == 'mk':
            from .news import mk
            return mk()
        elif args.name == 'donga':
            from .news import donga
            return donga()
        elif args.name == 'hankyung':
            from .news import hankyung
            return hankyung()
        elif args.name == 'khan':
            from .news import khan
            return khan()                
        
        # job
        elif args.name == 'work':
            from .job import work
            return work()
        elif args.name == 'linkareer':
            from .job import linkareer
            return linkareer()
        elif args.name == 'jobkorea':
            from .job import jobkorea
            return jobkorea()
        elif args.name == 'saramin':
            from .job import saramin
            return saramin()
        elif args.name == 'incruit':
            from .job import incruit
            return incruit()
        elif args.name == 'intellipick':
            from .job import intellipick
            return intellipick()


        else:
            msg = '매칭되는 사이트가 없습니다.'
            raise Exception(msg)