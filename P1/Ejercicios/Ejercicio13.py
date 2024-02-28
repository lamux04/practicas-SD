import os

f = open('/etc/passwd', 'r')

lusuarios = f.readlines();

lhome = []
for i in lusuarios:
    home = i.split(':')[-2]
    if home != '/':
        lhome.append(home)

print(lhome)