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
        else:
            msg = '매칭되는 대학이 없습니다.'
            raise Exception(msg)