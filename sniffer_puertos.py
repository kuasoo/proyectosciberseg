import socket


ip = input("Ingrese la direccion IP a escanear: ")

for puerto in  range(1, 65535):
#se analiza los puertos con un rango establecido que es la totalidad de puertos existentes
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
#af indica el uso del protocolo ipv4 y el SOCK_STREAM indica el uso del protocolo tcp

    resultado = sock.connect_ex((ip, puerto))
    if resultado == 0:
        print("El siguente puerto esta abierto: "+str (puerto))
        sock.close()
    else:
        print("El puerto se encuentra cerrado: "+str (puerto))