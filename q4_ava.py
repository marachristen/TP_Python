import argparse, sys
from functools import *
from functools import reduce
d = {"+":lambda x,y: x+y, "*": lambda x,y: x*y}

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-o","--operator",help="opérateur à utiliser", required=True, choices=d.keys())
    parser.add_argument("-v","--verbose",help="afficher avertissements", action="store_true")
    parser.add_argument("-n","--number", help="nombres à combiner", required=True, nargs="+", type=int)


    args = parser.parse_args()

    if args.verbose:
        print("mode verbose activé", file=sys.stderr)
        print("% d entiers lus" % len(args.number), file=sys.stderr)

    print(reduce(d[args.operator], args.number))



