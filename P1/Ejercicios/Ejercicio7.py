def dict_add(mydict, t):
    if type(t) is None:
        raise ValueError
    if len(t) != 2:
        raise ValueError
    
    newdict = dict(mydict)
    newdict[t[0]] = t[1]
    return newdict

print(dict_add({1: 'manzana'}, (2, 'fresa')))