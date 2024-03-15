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

def invertir_archivo(HOST, PORT):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))

    # Nombre del archvio
    ruta_archivo = str(input('Introduce la ruta del archivo: '))

    if not os.path.isfile(ruta_archivo):
        return

    # Enviamos el archivo
    archivo = open(ruta_archivo, 'r')
    s_archivo = ''.join(archivo.readlines())
    enviar_archivo(s_archivo, cliente)
    archivo.close()

    print('Archivo enviado')

    # Recibimos el archivo
    s_archivo, tam = recibir_archivo(cliente)

    print(f'El archivo ({tam} B) imprimido es:')
    print(s_archivo)
    cliente.close()



if __name__ == '__main__':
    invertir_archivo('localhost', 65000);