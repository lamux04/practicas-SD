import socket, argparse

def iniciar_servidor(HOST, PORT):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen(2)
    print('Servidor esperando a usuarios...')

    cliente1, addr1 = servidor.accept()
    print(f'Usuario 1 conectado: {addr1}')
    cliente2, addr2 = servidor.accept()
    print(f'Usuario 2 conectado: {addr2}')    

    cliente1.send(f'COMIENZAS'.encode('utf-8'))
    cliente2.send(f'NO COMIENZAS'.encode('utf-8'))

    while True:
        mensaje = cliente1.recv(1024).decode('utf-8')
        if mensaje == 'desconectar':
            cliente2.send('Conexion terminada'.encode('utf-8'))
            print('Conexion terminada')
            cliente1.close()
            cliente2.close()
            break
        print('USUARIO 1: ', mensaje)
        cliente2.send(mensaje.encode('utf-8'))

        mensaje = cliente2.recv(1024).decode('utf-8')
        if mensaje == 'desconectar':
            cliente1.send('Conexion terminada'.encode('utf-8'))
            print('Conexion terminada')
            cliente1.close()
            cliente2.close()
            break
        print('USUARIO 2: ', mensaje)
        cliente1.send(mensaje.encode('utf-8'))
    servidor.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=65000, help='listening port')
    args = parser.parse_args()
    iniciar_servidor('localhost', args.port)