import socket

HOST = 'localhost'
PORT = 1025

s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_tcp.bind((HOST, PORT))

s_tcp.listen(1)
print("Nos quedamos a la espera...")

s_cliente,addr = s_tcp.accept()

mensaje = s_cliente.recv(1024)

print("Recibo:["+mensaje.decode("utf-8")+"] del cliente con la dirección " + str(addr))
s_cliente.send("Hola, cliente, soy el servidor".encode("utf-8"))
s_cliente.close()
s_tcp.close()