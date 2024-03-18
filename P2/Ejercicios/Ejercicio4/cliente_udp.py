import socket, argparse

def iniciar_conexion(HOST, PORT):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cliente.sendto('Estableciendo conexion'.encode('utf-8'), (HOST, PORT))
    bienvenida,addr = cliente.recvfrom(1024)
    print(bienvenida.decode('utf-8'))

    # Enviamos el nombre
    nombre = str(input())
    cliente.sendto(nombre.encode('utf-8'), (HOST, PORT))

    # Enviamos mensajes
    mensaje, addr = cliente.recvfrom(1024)
    print(mensaje.decode('utf-8'))

    pregunta = str(input())
    while pregunta != 'exit':
        cliente.sendto(pregunta.encode('utf-8'), (HOST, PORT))
        respuesta, addr = cliente.recvfrom(1024)
        print(respuesta.decode('utf-8'))
        pregunta = str(input('Introduce otra pregunta (exit para salir): '))

    # Salir
    cliente.sendto('exit'.encode('utf-8'), (HOST, PORT))



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost', help='remote host')
    parser.add_argument('--port', default=65000, help='remote port')
    args = parser.parse_args()
    iniciar_conexion(args.host, args.port)