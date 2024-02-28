import os

def copiar(origen, destino):
    if not type(origen) is str or not type(destino) is str:
        raise TypeError
    if not os.path.isfile(origen):
        raise FileNotFoundError

    forigen = open(origen, 'r')
    fdestino = open(destino, 'w')

    fdestino.writelines(forigen.readlines())

    forigen.close()
    fdestino.close()

copiar('mifichero.txt', 'copia.txt')