def interseccion_listas(lista1, lista2):
    if not type(lista1) is list:
        raise TypeError
    if not type(lista2) is list:
        raise TypeError
    
    res = []

    lista1 = set(lista1)
    lista2 = set(lista2)

    return list(lista1 | lista2)

print(interseccion_listas([2, 5, 6, 7, 1, 4], [3, 4, 6, 7]))
