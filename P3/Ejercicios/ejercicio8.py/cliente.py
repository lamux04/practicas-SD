import requests, json

url = 'http://localhost:65000'

if __name__ == '__main__':
    while True:
        print('1. Registrar aterrizaje')
        print('2. Registrar despegue')
        print('3. Listar aviones')
        print('4. Salir')
        opcion = int(input('Que quiere hacer? '))

        if opcion == 4:
            break

        if opcion == 1:
            avion = {
                'matricula': input('Introduzca la matricula: '),
                'fecha llegada': input('Introduzca la fecha de llegada: '),
                'hora llegada': input('Introduzca la hora de llegada: ')
            }
            respuesta = requests.post(url=url+'/registrarAterrizaje', data=json.dumps(avion))
            print(respuesta.content)

        if opcion == 2:
            avion = {
                'matricula': input('Introduzca la matricula: '),
                'fecha salida': input('Introduzca la fecha de salida: '),
                'hora salida': input('Introduzca la hora de salida: ')
            }
            respuesta = requests.put(url=url+f'/despegue/{avion["matricula"]}', data=json.dumps(avion))
            print(respuesta.content)

        if opcion == 3:
            respuesta = requests.get(url=url+'/getAviones')
            print(respuesta.content)

        print()