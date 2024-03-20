import os, socket, argparse

def iniciar_servidor(HOST, PORT):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.bind((HOST, PORT))

    while True:
        comando, addr = servidor.recvfrom(1024)
        comando = comando.decode('utf-8')
        print(comando)
        if comando == 'exit':
            break
        if comando == 'ls':
            listar_ficheros(addr)
            continue
        if comando.split()[0] == 'rm':
            ruta = comando.split(' ')[1]
            eliminar_fichero(addr, ruta)
            continue
        if comando.split()[0] == 'write':
            ruta = comando.split(' ')[1]
            mensaje = ''.join(comando.split(' ')[2::])
            crear_fichero(addr, ruta, mensaje)
            continue
        if comando.split()[0] == 'cd':
            ruta = comando.split()[1]
        


        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=65000, help='listening port')
    args = parser.parse_args()
    iniciar_servidor('localhost', args.port)