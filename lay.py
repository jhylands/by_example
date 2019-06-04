def lay(list_of_tokens, depth=0):
    if depth <= 0:
        tokens = list_of_tokens
    else:
        tokens = lay(list_of_tokens, depth-1)
    acc = []
    print tokens
    for val in product(product(tokens,tokens + [t for t in list_of_tokens if type(t)!=type(tokens[0])]), dir(tokens[0])):
        try:
            (n1,n2),(attr) = val
        except TypeError:
            print val
            continue
        print attr
        try:
            print attr, n1, n2
            np, t = no_params(attr)
            tmp = getattr(n1, attr)() if np is 0 else getattr(n1, attr)(n2)
            if type(tmp) == str:
                acc.append(tmp)
        except Exception as e:
            print e.message
    return list(set(acc))
