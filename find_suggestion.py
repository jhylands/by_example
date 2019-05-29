from inspect import getargspec as spec
from math import isnan
def arg_no(f):
    try:
        if spec(f).defaults is None: return 0
        return len(spec(f).args)-len(spec(f).defaults)
    except Exception as e:
        print "inspect Error: %s"%e
        return float('nan')
    
def find(f_gen, ex, useful_values=[]):
    call_with = []
    deeper = []
    for att in dir(f_gen()):
        f = f_gen()
        try:
            a = getattr(f,att)
            if callable(a):
                no_args = arg_no(a)
                print a
                print "args: %s"%no_args
                if no_args==0 and a()==ex:
                    return att+"()"
                elif no_args==1 or isnan(no_args):
                    if a(useful_values[0])==ex:
                        return att+"(%s)"%useful_values[0]
                    else:
                        print att+"(%s)"%useful_values[0]
                else:
                    print "no_args: %s"%no_args
            elif a==ex:
                return att
            elif type(a) not in [str,int,float]:
                deeper.append(a)
        except TypeError as e:
            print e.message
            call_with.append(a)
        except Exception as e:
            print "Exception: %s"%e
    return {'call':call_with, 'depth':deeper}
