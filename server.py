import socket

ip = "192.168.233.1"
puerto = 8081
dataConection = (ip,puerto)
conexionesMaximas = 10

socketServidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketServidor.bind(dataConection)
socketServidor.listen(conexionesMaximas)

print("Esperando conexiones en: ",ip,puerto)
cliente,direccion = socketServidor.accept()
print("Conexion establecida con: ",direccion[0],direccion[1])

while True:
    datos = cliente.recv(1024).decode()
    print(datos)
    if datos == "exit":
        cliente.sendall("exit".encode())
        break
    print("Recibido",datos)
    cliente.sendall("---Recibido---".encode())
print("Conexion cerrada")
socketServidor.close()
