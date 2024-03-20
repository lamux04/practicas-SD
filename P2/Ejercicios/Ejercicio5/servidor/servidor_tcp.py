import socket, argparse, os

def enviar_archivo(archivo, conexion):
    data = archivo.read(1024)
    while data:
        conexion.sendall(data)
        data = archivo.read(1024)
    conexion.send(b'<EOF>')

def iniciar_servidor(HOST, PORT):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))

    servidor.listen(1)
    while True:
        conexion, addr = servidor.accept()
        print(f'Conectado con {addr}')
        nombre = conexion.recv(1024).decode('utf-8')
        nombre += '.jpg'
        if not os.path.isfile(nombre):
            conexion.send('NO EXISTE'.encode('utf-8'))
            conexion.close()
            continue
        conexion.send('EXISTE'.encode('utf-8'))
        conexion.recv(1024)

        # Enviar archivo
        with open(nombre, 'rb') as archivo:
            enviar_archivo(archivo, conexion)
        conexion.close()
        
            

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=65000, help='listening port')
    args = parser.parse_args()
    iniciar_servidor('localhost', args.port)