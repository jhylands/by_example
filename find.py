def find(f_gen, ex):
    call_with = []
    deeper = []
    for att in dir(f_gen()):
        f = f_gen()
        try:
            a = getattr(f,att)
            if callable(a):
                print a
                if a()==ex:
                    return att+"()"
                else:
                    pass
            elif a==ex:
                return att
            elif type(a) not in [str,int,float]:
                deeper.append(a)
        except TypeError as e:
            call_with.append(a)
        except Exception as e:
            print e
    return {'call':call_with, 'depth':deeper}
