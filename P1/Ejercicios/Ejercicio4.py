def accum(x, y, z):
    res = 0
    if not type(x) is int:
        raise TypeError
    if not type(y) is int:
        raise TypeError
    if not type(z) is int:
        raise TypeError
    
    if (x % 2 == 0): 
        res += x
    if (y % 2 == 0):
        res += y
    if (z % 2 == 0):
        res += z

    return res
