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