import requests, json

url = 'http://localhost:65000'

if __name__ == '__main__':
    while True:
        print()
        print('Elige la opcion que deseas realizar')
        print('   1. Dar de alta un nuevo miembro en el directorio')
        print('   2. Modicar los datos de un miembro')
        print('   3. Consultar la lista de todos los miembros de la universidad')
        print('   4. Hacer una busqueda por DNI')
        print('   5. Constultar todos los miembros segun categoria')
        print('   6. Salir')

        opcion = int(input('> '))

        if opcion == 1:
            data = {}
            data['dni'] = input('Introduce el dni: ')
            data['nombre'] = input('Introduce el nombre: ')
            data['correo'] = input('Introduce el correo: ')
            data['categoria'] = input('Introduce el categoria: ')
            data['asignaturas'] = []
            while True:
                data['asignaturas'].append(input('Introduce una asignatura o salir: '))
                if data['asignaturas'][-1] == 'salir':
                    break
            data['asignaturas'].pop()
            data = json.dumps(data)
            r = requests.post(url=url + '/nuevoMiembro', data=data)
            print(r.text)
        elif opcion == 2:
            data = {}
            dni = input('Introduce el dni: ')
            data['nombre'] = input('Introduce el nombre: ')
            data['correo'] = input('Introduce el correo: ')
            data['categoria'] = input('Introduce el categoria: ')
            data['asignaturas'] = []
            while True:
                data['asignaturas'].append(input('Introduce una asignatura o salir: '))
                if data['asignaturas'][-1] == 'salir':
                    break
            data['asignaturas'].pop()
            data = json.dumps(data)
            r = requests.put(url=url + f'/modificarMiembro/{dni}', data=data)
            print(r.text)
        elif opcion == 3:
            r = requests.get(url=url + '/miembros')
            print(r.text)
        elif opcion == 4:
            dni = input('Introduce el dni: ')
            r = requests.get(url=url + f'/miembro/{dni}')
            print(r.text)
        elif opcion == 5:
            s = input('Introduce la categoria: ')
            r = requests.get(url=url + f'/miembro/categoria/{s}')
            print(r.text)
        else:
            break