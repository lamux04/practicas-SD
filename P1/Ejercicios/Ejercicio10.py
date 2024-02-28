def interseccion_listas(lista1, lista2):
    if not type(lista1) is list:
        raise TypeError
    if not type(lista2) is list:
        raise TypeError
    
    res = []

    lista1 = set(lista1)
    lista2 = set(lista2)

    return list(lista1 & lista2)

    
    for i in lista1:
        j = 0
        while j < len(lista2) and lista2[j] != i:
            j += 1
        if (j < len(lista2)):
            res.append(i)
    return res
        

print(interseccion_listas([2, 5, 6, 7, 1, 4], [3, 4, 6, 7]))