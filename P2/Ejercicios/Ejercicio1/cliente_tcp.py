import socket

HOST = 'localhost'
PORT = 1025

s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s_tcp.connect((HOST, PORT))

s_tcp.send('Hola soy el cliente'.encode('utf-8'))

mensaje = s_tcp.recv(1024)
print(mensaje.decode('utf-8') + 'recibido')

s_tcp.close()