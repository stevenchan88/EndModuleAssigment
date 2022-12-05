import socket

ipServidor = "localhost"
puertoServidor = 8081

cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente.connect((ipServidor,puertoServidor))
print("conectado con: ",ipServidor,puertoServidor)

while True:
    msg = input(">: ")
    cliente.sendall(msg.encode())
    respuesta = cliente.recv(4096).decode()
    print(respuesta)
    if respuesta == "exit":
        break

print("----conexion cerrada----")
cliente.close()