def no_params(attr):
    try:
        getattr('',attr)()
        return (0, None)
    except:
        try:
            getattr('',attr)([])
            return (1,list)
        except TypeError:
            try:
                getattr('',attr)(0)
                return (1 , int)
            except:
                try:
                    getattr('',attr)('')
                    return (1, str)
                except TypeError:
                    return False
                except:
                    print attr
        except:
            return False
