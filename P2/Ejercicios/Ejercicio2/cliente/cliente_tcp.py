import socket, os

def enviar_archivo(HOST, PORT, ruta_fichero):
    con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con.connect((HOST, PORT))
    nombre_fichero = ruta_fichero.split('/')[-1]
    con.send(nombre_fichero.encode('utf-8'))
    respuesta = con.recv(1024).decode('utf-8')

    if respuesta == 'EXISTE':
        sobreescribir = input('El archivo existe en el servidor, ¿quiere sobreescribir (S/N)?')
        if sobreescribir != 'S' and sobreescribir != 's':
            print('Transferencia cancelada.')
            con.close()
            return
        con.send('SI'.encode('utf-8'))

    if respuesta == 'SI':

        with open(ruta_fichero, 'rb') as archivo:
            while True:
                datos = archivo.read(1024)
                if not datos:
                    break
                con.send(datos)
        con.send("<EOF>".encode('utf-8'))

        print('Archivo enviado')
        notificacion = con.recv(1024)
        if notificacion == b'Recibido':
            print ('Servidor ha recido el archivo.')
    con.close()
    

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 65431
    con = enviar_archivo(HOST, PORT, './prueba.pdf')