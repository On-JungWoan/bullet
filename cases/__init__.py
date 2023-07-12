def build_special_function(args):

    if args.mode=='announce':
        assert args.univ_name is not None

        if args.univ_name == 'jnu':
            from university import jnu
            return jnu