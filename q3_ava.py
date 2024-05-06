import sys
from functools import *
d = {'+': lambda x,y: x+y, '*': lambda  x,y: x*y}

if __name__=='__main__':
    try:
        if len(sys.argv) < 3: #zum teste ebs mind 2 zahle und es + oder * het
            print(f"opérateur invalide:{sys.argv[-1]}",file=sys.stderr)
        else:
            with open("output.txt","w") as f:
                sys.stdout = f
                print(reduce(d[sys.argv[-1]],[int(x) for x in sys.argv[1:-1]]))
    except ValueError:
        print("les arguments doivent être des entiers", file=sys.stderr)

