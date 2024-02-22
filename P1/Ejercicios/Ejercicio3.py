import filecmp, sys, shutil, os

# Creamos un nombre que no exista
def nombre_duplicado(num):
    if (os.path.isfile(sys.argv[1] + ' - COPY (%i).py' % num) == False):
        return sys.argv[1] + ' - COPY (%i).py' % num
    else:
        return nombre_duplicado(num + 1)

# Comprobamos que exista el fichero
if os.path.isfile(sys.argv[1]) == False:
    raise FileNotFoundError

nuevo_archivo = nombre_duplicado(0)

shutil.copy(sys.argv[1], nuevo_archivo)

# Comprobamos que son iguales
if filecmp.cmp(sys.argv[1], nuevo_archivo, shallow=False):
    print ('Copia de ', sys.argv[1], ' creada en ', nuevo_archivo)
else:
    print ('Algo salio mal')