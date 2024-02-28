import os

union = open('union.txt', 'w')

lineas = []

for i in os.listdir():
    if os.path.isfile(i) and i.split('.')[-1] == 'txt':
        f = open(i, 'r')
        lineas.extend(f.readlines())

union.writelines(lineas)