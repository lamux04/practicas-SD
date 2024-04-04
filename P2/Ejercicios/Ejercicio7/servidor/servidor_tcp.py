import os, socket, argparse
from _thread import *

def listar_archivos(cliente):
    cliente.send(' '.join(os.listdir()).encode('utf-8'))

def enviar_archivo(cliente, nombre_archivo):
    if not os.path.isfile(nombre_archivo):
        cliente.send('NO EXISTE'.encode('utf-8'))
        return
    tamanno_archivo = os.path.getsize(nombre_archivo)
    cliente.send(f'{tamanno_archivo}'.encode('utf-8'))
    mensaje = cliente.recv(1024).decode('utf-8')

    if not mensaje == 'OK':
        cliente.send('ERROR, archivo no enviado'.encode('utf-8'))
        return

    # Enviando archivo
    with open(nombre_archivo, 'rb') as archivo:
        datos_enviados = 0
        while datos_enviados < tamanno_archivo:
            datos = archivo.read(1024)
            datos_enviados += 1024
            cliente.send(datos)

def atender_cliente(cliente):
    # Mensaje de bienvenida
    cliente.send('Bienvenido al servidor FTP'.encode('utf-8'))

    while True:
        comando = cliente.recv(1024).decode('utf-8')
        if comando == 'exit':
            break
        if comando.split(' ')[0] == 'get':
            enviar_archivo(cliente, comando.split(' ')[1])
            continue
        if comando == 'listar':
            listar_archivos(cliente)
            continue

    return

def iniciar_servidor(host, port):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, port))
    servidor.listen(5)
    print('Esperando conexiones de clientes...')

    while True:
        cliente, addr = servidor.accept()
        start_new_thread(atender_cliente, (cliente, ))
        print(f'Cliente conectado: {addr}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=65000, help='listening port')
    args = parser.parse_args()
    iniciar_servidor('localhost', args.port)