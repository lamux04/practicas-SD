import os, socket

def enviar_archivo(s_archivo, destino):
    
    # Enviamos la longitud
    destino.send(str(len(s_archivo)).encode('utf-8'))

    destino.recv(1024).decode('utf-8')
    
    # Enviamos el archivo
    destino.sendall(s_archivo.encode('utf-8'))

    destino.recv(1024)

def recibir_archivo(destino):
    s_archivo = ''

    # Recibimos el tamanno
    tamanno = int(destino.recv(1024).decode('utf-8'))

    # Confirmamos recibido el tamanno
    destino.send('Recibido tamanno'.encode('utf-8'))

    # Recibimos el fichero
    n = 0
    while n < tamanno:
        n += 1024
        s_archivo += destino.recv(1024).decode('utf-8')

    destino.send('Recibido'.encode('utf-8'))

    return s_archivo, tamanno
    
def iniciar_servidor(HOST, PORT):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen(1)
    print(f'Servidor iniciado en {(HOST, PORT)}')

    while True:
        cliente, addr = servidor.accept()
        print(f'Conexion establecida con {addr}')

        # Recibimos el archivo
        s_archivo, tamanno = recibir_archivo(cliente)

        # Invertimos el archivo
        s_archivo = s_archivo[::-1]

        # Enviamos el archivo
        enviar_archivo(s_archivo, cliente)

        print('Archivo invertido y enviado')
        cliente.close()


if __name__ == '__main__':
    iniciar_servidor('localhost', 65000);