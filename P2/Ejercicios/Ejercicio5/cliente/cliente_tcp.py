import os, socket, argparse

def recibir_archivo(conexion, nombre_archivo):
    with open(nombre_archivo, 'wb') as archivo:
        data = conexion.recv(1024)
        while data:
            if b'<EOF>' in data:
                data[:-5:1]
            archivo.write(data)
            data = conexion.recv(1024)

def descargar_imagen(HOST, PORT, nombre):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))
    cliente.send(nombre.encode('utf-8'))
    respuesta = cliente.recv(1024).decode('utf-8')
    if respuesta == 'NO EXISTE':
        print('El archivo no existe')
        cliente.close()
        return
    if respuesta == 'EXISTE':
        cliente.send(b'RECIBIR')
        recibir_archivo(cliente, f'{nombre}.jpg')
        print('Archivo recibido correctamente')
        cliente.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost', help='remote host')
    parser.add_argument('--port', default=65000, help='remote port')
    args = parser.parse_args()
    descargar_imagen(args.host, args.port, 'imagen')