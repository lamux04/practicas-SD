import requests, json

url = 'http://localhost:65000'

if __name__ == '__main__':
    while True:
        print()
        print('Elige la opcion que deseas realizar')
        print('   1. Dar de alta una nueva habitación')
        print('   2. Modicar los datos de una habitación')
        print('   3. Consultar la lista completa de habitaciones')
        print('   4. Consultar una habitación mediante identicador')
        print('   5. Consultar la lista de habitaciones ocupadas o desocupadas')
        print('   6. Salir')

        opcion = int(input('> '))

        if opcion == 1:
            data = {}
            data['plazas'] = input('Introduce las plazas: ')
            data['equipamiento'] = []
            while True:
                data['equipamiento'].append(input('Introduce un equipamiento o salir: '))
                if data['equipamiento'][-1] == 'salir':
                    break
            data['equipamiento'].pop()
            data = json.dumps(data)
            r = requests.post(url=url + '/habitacion', data=data)
            print(r.text)
        elif opcion == 2:
            data = {}
            id = input('Introduce el identificador de la habitacion: ')
            data['plazas'] = input('Introduce las plazas: ')
            data['equipamiento'] = []
            while True:
                data['equipamiento'].append(input('Introduce un equipamiento o salir: '))
                if data['equipamiento'][-1] == 'salir':
                    break
            data['equipamiento'].pop()
            data = json.dumps(data)
            r = requests.put(url=url + f'/habitacion/{id}', data=data)
            print(r.text)
        elif opcion == 3:
            r = requests.get(url=url + '/habitacion')
            print(r.text)
        elif opcion == 4:
            id = input('Introduce el identificador de la habitacion: ')
            r = requests.get(url=url + f'/habitacion/{id}')
            print(r.text)
        elif opcion == 5:
            if input('Introduce 1 (ocupadas) o 2 (desocupadas): ') == 1:
                s = "ocupadas"
            else:
                s = "desocupadas"
            r = requests.get(url=url + f'/habitacion/{s}')
            print(r.text)
        else:
            break