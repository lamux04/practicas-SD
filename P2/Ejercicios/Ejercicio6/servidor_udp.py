import os, socket, argparse, shutil

def listar_ficheros(servidor, addr):
    servidor.sendto(' '.join(os.listdir()).encode('utf-8'), addr)

def eliminar_fichero(servidor, addr, ruta):
    if (os.path.isfile(ruta)):
        os.remove(ruta)
        servidor.sendto(f'{ruta} eliminado correctamente'.encode('utf-8'), addr)
    else:
        servidor.sendto(f'{ruta} no es un fichero'.encode('utf-8'), addr)

def crear_fichero(servidor, addr, ruta, mensaje):
    if not os.path.isfile(ruta):
        with open(ruta, 'w+') as file:
            file.write(mensaje)
        servidor.sendto(f'{ruta} creado correctamente'.encode('utf-8'), addr)
    else:
        servidor.sendto(f'{ruta} no es un fichero'.encode('utf-8'), addr)

def cambiar_directorio(servidor, addr, ruta):
    if os.path.isdir(ruta):
        os.chdir(ruta)
        servidor.sendto(f'El directorio actual ahora es: {os.getcwd()}'.encode('utf-8'), addr)
    else:
        servidor.sendto(f'{ruta} no es un directorio'.encode('utf-8'), addr)

def mover_fichero(servidor, addr, origen, destino):
    if (os.path.isfile(origen) and os.path.isdir(destino)):
        shutil.move(origen, destino)
        servidor.sendto(f'{origen} movido correctamente'.encode('utf-8'), addr)
    else:
        servidor.sendto(f'{origen} no es un fichero o {destino} no es un directorio'.encode('utf-8'), addr)
        
def iniciar_servidor(HOST, PORT):
    print (f'Listening on {PORT}')
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.bind((HOST, PORT))

    while True:
        comando, addr = servidor.recvfrom(1024)
        comando = comando.decode('utf-8')
        print(comando)
        if comando == 'exit':
            break
        if comando == 'ls':
            listar_ficheros(servidor, addr)
            continue
        if comando.split()[0] == 'rm':
            ruta = comando.split(' ')[1]
            eliminar_fichero(servidor, addr, ruta)
            continue
        if comando.split()[0] == 'write':
            ruta = comando.split(' ')[1]
            mensaje = ' '.join(comando.split(' ')[2::])
            crear_fichero(servidor, addr, ruta, mensaje)
            continue
        if comando.split()[0] == 'cd':
            ruta = comando.split()[1]
            cambiar_directorio(servidor, addr, ruta)
            continue
        if comando.split()[0] == 'mv':
            origen = comando.split()[1]
            destino = comando.split()[2]
            mover_fichero(servidor, addr, origen, destino)
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=65000, help='listening port')
    args = parser.parse_args()
    iniciar_servidor('localhost', args.port)