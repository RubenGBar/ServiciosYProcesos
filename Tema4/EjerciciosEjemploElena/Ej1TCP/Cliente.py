import socket

HOST = "192.168.1.137"  # Dirección IP del servidor
PORT = 49200  # Puerto del servidor

try:
    # 1 - Crear un socket de tipo cliente
    print("Estableciendo conexión con el servidor")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((HOST, PORT))

        # 2 - Enviar un mensaje al servidor
        cliente.sendall(b"4")

        # 3 - Leer respuesta del servidor
        respuesta = cliente.recv(1024).decode("utf-8")
        print(f"El servidor me envía el siguiente mensaje: {respuesta}")

        # 4 y 5 - La conexión se cierra automáticamente con 'with'
        print("Se cierra la conexión del cliente")

except socket.gaierror:
    print("No se encuentra el host especificado.")
except ConnectionError:
    print("Se ha producido un error en la conexión con el servidor.")
