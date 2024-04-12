import requests

if __name__ == '__main__':
    while True:
        print('Elige la opcion que deseas realizar')
        print('   1. Dar de alta una nueva habitación')
        print('   2. Modicar los datos de una habitación')
        print('   3. Consultar la lista completa de habitaciones')
        print('   4. Consultar una habitación mediante identicador')
        print('   5. Consultar la lista de habitaciones ocupadas o desocupadas')
        print('   6. Salir')

        opcion = input('> ')

        if opcion == 1:
            requests.post('')