import socket, argparse

def entrar_chat(HOST, PORT):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))
    mensaje = cliente.recv(1024).decode('utf-8')
    print('SERVER: Conexion iniciada: ', mensaje)

    if mensaje == 'COMIENZAS':
        cliente.send(str(input('TU: ')).encode('utf-8'))
        if mensaje == 'desconectar':
            print('SERVER: Conexion terminada')
            cliente.close()
            return

    while True:
        mensaje = cliente.recv(1024).decode('utf-8')
        if mensaje == 'Conexion terminada':
            print('SERVER: Conexion terminada')
            cliente.close()
            break
        print('OTRO: ', mensaje)
        mensaje = str(input('TU: '))
        cliente.send(mensaje.encode('utf-8'))
        if mensaje == 'desconectar':
            print('SERVER: Conexion terminada')
            cliente.close()
            break
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost', help='remote host')
    parser.add_argument('--port', default=65000, help='remote port')
    args = parser.parse_args()
    entrar_chat(args.host, args.port)