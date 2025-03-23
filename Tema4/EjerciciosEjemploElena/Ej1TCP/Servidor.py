import socket

HOST = "0.0.0.0"  # Escuchar en todas las interfaces
PORT = 49200  # Puerto del servidor

try:
    # 1 - Crear socket de tipo servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((HOST, PORT))
        servidor.listen()
        print("Servidor se encuentra a la escucha...")

        while True:
            # 2 - Aceptar conexiones entrantes
            conexion, direccion = servidor.accept()
            with conexion:
                print(f"Conexión aceptada desde {direccion}")

                # 3 - Leer mensaje del cliente
                numero = conexion.recv(1)  # Leer un byte (número enviado)
                if not numero:
                    continue
                numero = int.from_bytes(numero, byteorder='big')
                print(f"Mensaje enviado por el cliente: {numero}")

                # 4 - Enviar respuesta al cliente (doble del número recibido)
                doble = str(numero * 2) + "\n"
                conexion.sendall(doble.encode("utf-8"))
                print("Servidor envía al cliente el doble")

except OSError as e:
    print(f"Ha habido algún error en la creación del Socket Servidor: {e}")
