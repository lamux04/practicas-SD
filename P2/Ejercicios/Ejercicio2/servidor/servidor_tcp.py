import socket, os

def recibir_archivo(cliente, nombre_fichero):
    with open(nombre_fichero, 'wb') as archivo:
        datos = cliente.recv(1024)
        while datos:
            if b"<EOF>" in datos:
                archivo.write(datos[:-5]) # Eliminamos EOF
                break
            archivo.write(datos)
            datos = cliente.recv(1024)
            
def iniciar_servidor(HOST, PORT):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen(1)
    print(f'Escuchando en {(HOST, PORT)}')
    
    while True:
        cliente, addr = servidor.accept()
        print(f'Conexión establecida desde {addr}')
        nombre_fichero = cliente.recv(1024).decode('utf-8')

        if os.path.isfile(nombre_fichero):
            cliente.send('EXISTE'.encode('utf-8'))
            res = cliente.recv(1024).decode('utf-8')
            if (res != 'SI'):
                cliente.close()
                continue
            os.remove(nombre_fichero)
        else:
            cliente.send('SI'.encode('utf-8'))
        recibir_archivo(cliente, nombre_fichero)
        print(f'Archivo {nombre_fichero} recibido')
        cliente.send(b'Recibido')
        cliente.close()

        

if __name__ == '__main__':
    iniciar_servidor('localhost', 65431)