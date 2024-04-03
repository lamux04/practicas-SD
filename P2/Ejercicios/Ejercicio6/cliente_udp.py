import os, socket, argparse

def listar_directorio(cliente, addrServidor):
    cliente.sendto('ls'.encode('utf-8'), addrServidor)
    mensaje,addr = cliente.recvfrom(1024)
    print(mensaje.decode('utf-8'))

def eliminar_fichero(cliente, addrServidor, ruta):
    comando = f'rm {ruta}'
    cliente.sendto(comando.encode('utf-8'), addrServidor)
    mensaje,addr = cliente.recvfrom(1024)
    print(mensaje.decode('utf-8'))

def crear_fichero(cliente, addrServidor, ruta, mensaje):
    comando = f'write {ruta} {mensaje}'
    cliente.sendto(comando.encode('utf-8'), addrServidor)
    mensaje,addr = cliente.recvfrom(1024)
    print(mensaje.decode('utf-8'))

def cambiar_directorio(cliente, addrServidor, ruta):
    comando = f'cd {ruta}'
    cliente.sendto(comando.encode('utf-8'), addrServidor)
    mensaje,addr = cliente.recvfrom(1024)
    print(mensaje.decode('utf-8'))

def mover_fichero(cliente, addrServidor, origen, destino):
    comando = f'mv {origen} {destino}'
    cliente.sendto(comando.encode('utf-8'), addrServidor)
    mensaje,addr = cliente.recvfrom(1024)
    print(mensaje.decode('utf-8'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost', help='remote host')
    parser.add_argument('--port', default=65000, help='remote port')
    args = parser.parse_args()
    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addrServidor = (args.host, args.port)
    
    while True:
        comando = str(input(''))
        if comando == 'exit':
            break
        if comando == 'ls':
            listar_directorio(cliente, addrServidor)
            continue
        if comando.split()[0] == 'rm':
            ruta = comando.split(' ')[1]
            eliminar_fichero(cliente, addrServidor, ruta)
            continue
        if comando.split()[0] == 'write':
            ruta = comando.split(' ')[1]
            mensaje = ' '.join(comando.split(' ')[2::])
            crear_fichero(cliente, addrServidor, ruta, mensaje)
            continue
        if comando.split()[0] == 'cd':
            ruta = comando.split()[1]
            dir_actual = cambiar_directorio(cliente, addrServidor, ruta)
            continue
        if comando.split()[0] == 'mv':
            origen = comando.split()[1]
            destino = comando.split()[2]
            mover_fichero(cliente, addrServidor, origen, destino)