def es_primo (a):
    i = 2
    while i < a ** 0.5 and a % i != 0:
        i += 1
    if a % i == 0 and a != i:
        return False
    return True
    
        

def prime (a, b):
    if not type(a) is int:
        raise TypeError
    if not type(b) is int:
        raise TypeError
    if a > b:
        raise ValueError
    
    res = []
    for i in range(a, b):
        if (es_primo(i)):
            res.append(i)

    return res

print (prime(2, 10))
    
