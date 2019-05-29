'''
What we want to have here is a tuple of 
the input and the output
However we want to be more general than that 
we want to be able to find functions that
modify state in the way that we want.
'''

class search:
    def __init__(self, generator, checker, hints=[]):
        self.generator = generator
        self.checker = checker
        self.hints = hints
'''
find
 - A dictionary of generator, checker, hints

'''
def find(search_list, general_hints):
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



def find2(get_f, ex):
    for a in dir(__builtins__):
        if a in ['exit','quit','help','input','raw_input']:
            continue
        print a
        b = getattr(__builtins__,a)
        try:
            if b(get_f())==ex:
                return b
        except Exception as e:
            print e
