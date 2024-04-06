import socket, argparse

def iniciar_servidor(HOST, PORT):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.bind((HOST, PORT))
    print('Servidor esperando a usuarios...')

    mensaje, addr1 = servidor.recvfrom(1024)
    print(f'Usuario 1 conectado: {addr1}')
    while True:
        mensaje, addr2 = servidor.recvfrom(1024)
        if addr2 != addr1:
            print(f'Usuario 2 conectado: {addr2}')
            break

    servidor.sendto(f'COMIENZAS'.encode('utf-8'), addr1)
    servidor.sendto(f'NO COMIENZAS'.encode('utf-8'), addr2)

    while True:
        while True:
            mensaje, addr = servidor.recvfrom(1024)
            mensaje = mensaje.decode('utf-8')
            print(addr, addr1)
            if addr == addr1:
                break
        if mensaje == 'desconectar':
            servidor.sendto('Conexion terminada'.encode('utf-8'), addr2)
            break
        print('USUARIO 1: ', mensaje)
        servidor.sendto(mensaje.encode('utf-8'), addr2)

        while True:
            mensaje, addr = servidor.recvfrom(1024)
            mensaje = mensaje.decode('utf-8')
            print(addr, addr2)
            if addr == addr2:
                break
        if mensaje == 'desconectar':
            servidor.sendto('Conexion terminada'.encode('utf-8'), addr1)
            break
        print('USUARIO 2: ', mensaje)
        servidor.sendto(mensaje.encode('utf-8'), addr1)
    servidor.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=65000, help='listening port')
    args = parser.parse_args()
    iniciar_servidor('localhost', args.port)