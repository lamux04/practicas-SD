import os

def listar_ficheros(dir):
    if os.path.isdir(dir):
        for i in os.listdir(dir):
            if (os.path.isfile(os.path.join(dir, i))):
                print(os.path.join(dir, i), ' -> ', os.path.getsize(os.path.join(dir, i)), 'B')
            else:
                listar_ficheros(os.path.join(dir, i))

listar_ficheros('.')