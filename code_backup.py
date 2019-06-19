def find2(get_f, ex):
    for a in dir(__builtins__):
        if a in ['exit','quit','help','input','raw_input']:
            continue
        print a
        b = getattr(__builtins__,a)
        try:
            if b(get_f())==list:
                return b
        except Exception as e:
            print e
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
def layer(depth=0):
    if depth<=0:
        l1r = list_of_tokens
    else:
        l1r = layer(depth-1)
    layern = product(product(l1r,l1r), list_of_functions)
    l2r = set([f(n1,n2) for (n1,n2),f in layern])
    return l2r
def errornious(f):
    try:
        f('a')
        return True
    except Exception:
        return False
def no_params(attr):
    try:
        t = type(getattr('',attr)())
        return (0, None, t)
    except:
        try:
            t = type(getattr('',attr)([]))
            return (1,list, t)
        except TypeError:
            try:
                t = type(getattr('',attr)(0))
                return (1 , int, t)
            except:
                try:
                    t= type(getattr('',attr)(''))
                    return (1, str, t)
                except TypeError:
                    return [0,0,0]
                except:
                    print attr
                    [0,0,0]
        except:
            return [0,0,0]
def lay(list_of_tokens, depth=0):
    if depth <= 0:
        tokens = list_of_tokens
    else:
        tokens = lay(list_of_tokens, depth-1)
    acc = []
    print tokens
    for val in product(product(tokens,tokens + [t for t in list_of_tokens if type(t)!=type(tokens[0])]), [f for f in dir(tokens[0]) if no_params(f)[2]==type(tokens[0])]):
        try:
            (n1,n2),(attr) = val
        except TypeError:
            print val
            continue
        print attr
        try:
            print attr, n1, n2
            np, t_in, t_out = no_params(attr)
            tmp = getattr(n1, attr)() if np is 0 else getattr(n1, attr)(n2)
            if type(tmp) == str:
                acc.append(tmp)
        except Exception as e:
            print e.message
    return list(set(acc))
def mirror(x):
    if str(x)[0]=='-':
        return int(str(x) + str(x)[1:][::-1])*-1
    else:
        return int(str(x) + str(x)[::-1])
def shift(x):
    return int(str(x)[-1] + str(x)[:-1])
