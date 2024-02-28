import os, shutil

def mover_subficheros(dir):
    if os.path.isfile(dir):
        if not os.path.isfile(os.path.join('.', os.path.basename(dir))):
            shutil.move(dir, '.')
    else:
        for i in os.listdir(dir):
            mover_subficheros(os.path.join(dir, i))

mover_subficheros('.')