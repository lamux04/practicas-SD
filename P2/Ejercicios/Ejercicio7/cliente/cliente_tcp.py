import os, socket, argparse

def listar_archivos(cliente):
    listado = cliente.recv(1024).decode('utf-8')
    print(listado)

def get_archivo(cliente, nombre_archivo):
    tamanno_archivo = cliente.recv(1024).decode('utf-8')
    if tamanno_archivo == 'NO EXISTE':
        print('El archivo no existe en el servidor')
        return
    tamanno_archivo = int(tamanno_archivo)
    if os.path.isfile(nombre_archivo):
        sobreescribir = str(input('El archivo ya existe localmente, quieres sobreescribirlo? (S/N)'))
        if not 'S' in sobreescribir or not 's' in sobreescribir:
            cliente.send('NO'.encode('utf-8'))
            return
    cliente.send('OK'.encode('utf-8'))
    # Recibir archivo
    with open(nombre_archivo, 'wb') as archivo:
        while tamanno_archivo > 0:
            datos = cliente.recv(1024)
            tamanno_archivo -= 1024
            archivo.write(datos)

    print('Archivo recibido con exito')        

def iniciar_cliente(host, port):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, port))
    print('Conectado con el servidor')
    mensaje = cliente.recv(1024).decode('utf-8')
    print(mensaje)

    while True:
        comando = str(input())
        cliente.send(comando.encode('utf-8'))
        if comando == 'exit':
            cliente.close()
            break
        if comando == 'listar':
            listar_archivos(cliente)
            continue
        if comando.split(' ')[0] == 'get':
            get_archivo(cliente, comando.split(' ')[1])
            continue


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost', help='remote host')
    parser.add_argument('--port', default=65000, help='remote port')
    args = parser.parse_args()
    iniciar_cliente(args.host, args.port)