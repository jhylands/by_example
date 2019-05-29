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
