import os

for i in os.listdir():
    print(i)

nombre = str(input('Introduce el fichero a renombrar: '))

if not os.path.isfile(nombre):
    raise FileNotFoundError

nuevo_nombre = str(input('Introduce el nuevo nombre: '))

if os.path.isfile(nuevo_nombre):
    raise FileExistsError

os.rename(nombre, nuevo_nombre)