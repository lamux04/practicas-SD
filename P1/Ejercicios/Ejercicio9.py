import os

def get_file_info(filename):
    if not type(filename) is str:
        raise TypeError
    if filename == None:
        raise ValueError
    
    if not os.path.isfile(filename):
        raise FileNotFoundError
    
    f = open(filename, 'r')
    
    contenido = f.read().split()
    res = []
    for i in contenido:
        if [*i][len(i) - 1] == 's':
            res.append(i)

    return os.path.getsize(filename), res

print(get_file_info("mifichero.txt"))