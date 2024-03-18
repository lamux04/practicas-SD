import socket, argparse

def iniciar_servidor(HOST, PORT):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.bind((HOST, PORT))

    while True:
        mensaje, addr = servidor.recvfrom(1024)
        mensaje = mensaje.decode('utf-8')
        if mensaje != 'Estableciendo conexion':
            continue
        print(f'Conexion establecida con {addr}')
        servidor.sendto('¡Bienvenido! ¿Cuál es su nombre para que pueda dirigirme a usted?'.encode('utf-8'), addr)
        
        # Recibimos el nombre
        nombre, addr = servidor.recvfrom(1024)
        nombre = nombre.decode('utf-8')

        # En que puedo ayudarte
        servidor.sendto(f'{nombre}, ¿en qué puedo ayudarte?'.encode('utf-8'), addr)

        mensaje, addr = servidor.recvfrom(1024)
        mensaje = mensaje.decode('utf-8')

        while mensaje != 'exit':
            servidor.sendto('Debe ponerse en contacto con el servicio de atención de dudas cuya dirección es dudas@ejemplo.com'.encode('utf-8'), addr)
            mensaje, addr = servidor.recvfrom(1024)
            mensaje = mensaje.decode('utf-8')
        print(f'Conexion terminada con {addr}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=65000, help='listening port')
    args = parser.parse_args()
    iniciar_servidor('localhost', args.port)