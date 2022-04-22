"""
    Author: Davi Alexandre
"""

import sys


class MyArgs:
    def __init__(self, free:'identifiers', constrained:'identifiers and a predicate'):
        self._args = list(free) + list(constrained.keys())
        self._args = {arg:None for arg in free}
        for arg, predicate in constrained.items():
            self._args[arg] = predicate
        for arg in self._args.keys():
            if arg != '_args':
                setattr(self, arg, None)
    def __str__(self):
        msg = ''
        for arg in self._args.keys():
            msg += arg + ': ' + str(getattr(self, arg)) + '\n'
        return msg

def eval_args(*free, **constrained):
    argv = sys.argv
    args = MyArgs(free, constrained)
    identifiers = list(free) + list(constrained.keys())
    for arg in argv[1:]:
        if not arg[:2].startswith('--') or arg == '--':
            continue
        arg = arg[2:]
        if not '=' in arg:
            arg = arg.replace('-', '_')
            if arg in constrained.keys():
                if constrained[arg] == None:
                    key = arg
                    value = 'True'
                else:
                    continue
            else: continue
        else:
            key, value = arg.split('=')
            key = key.replace('-', '_')
        if key not in identifiers:
            continue
        try:
            value = eval(value)
        except:
            value = eval("'" + str(value) + "'")

        predicate = args._args[key] if key != arg.replace('-', '_') else (lambda x: x)
        if not predicate(value):
            raise Exception(
                f"The argument {key} does not satisfy "
                f"it's predicate for the value {value}")
        setattr(args, key, value)
    return args


if __name__ == '__main__':
    args = eval_args(
        no_equals=None,
        reprocess=lambda v: isinstance(v, bool), 
        read_limit=lambda v: isinstance(v, int) and v > 0)

    if args.reprocess: print('Reprocessing...')
    if args.read_limit == 1: print('Reading until 1')

    print(args)