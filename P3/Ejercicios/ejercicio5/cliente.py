import requests, json

url = 'http://localhost:65000'

if __name__ == '__main__':
    while True:
        print()
        print('Elige la opcion que deseas realizar')
        print('   1. Registrar usuario')
        print('   2. Activar cuenta')
        print('   3. Buscar usuario')

        opcion = int(input('> '))

        if opcion == 1:
            data = {}
            data['username'] = input('Nombre de usuario: ')
            data['clave'] = input('Clave: ')
            data['correo'] = input('Correo: ')
            data['nombre'] = input('Nombre: ')
            data['apellidos'] = input('Apellidos: ')
            data = json.dumps(data)
            r = requests.post(url=url + '/nuevoUsuario', data=data)
            print(r.text)
        elif opcion == 2:
            username = input('Nombre de usuario: ')
            r = requests.put(url=url + f'/activarCuenta/{username}')
            print(r.text)
        elif opcion == 3:
            cad = input('Cadena: ')
            r = requests.get(url=url + f'/busquedaUsuarios/{cad}')
            print(r.text)
        else:
            break