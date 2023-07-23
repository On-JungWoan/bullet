def build_obj(args):

    if args.mode=='announce':
        assert args.univ_name is not None

        if args.univ_name == 'jnu':
            from .university import jnu
            return jnu()
        elif args.univ_name == 'grad-unist':
            from .university import grad_unist
            return grad_unist()
        elif args.univ_name == 'jbnu':
            from .university import jbnu
            return jbnu()
        elif args.univ_name == 'snu':
            from .university import snu
            return snu()
        elif args.univ_name == 'cnu':
            from .university import cnu
            return cnu()
        elif args.univ_name == 'knu':
            from .university import knu
            return knu()
        elif args.univ_name == 'pnu':
            from .university import pnu
            return pnu()
        elif args.univ_name == 'jejunu':
            from .university import jejunu
            return jejunu()        
        else:
            msg = '매칭되는 대학이 없습니다.'
            raise Exception(msg)