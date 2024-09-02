import string
import random

##se utilizan las librerias del uso de cadenas por la entrada de texto y aletoriedad 

longitud = int(input("Ingrese el tamaño de la contraseña: "))

caracter = string.ascii_letters + string.digits + string.punctuation
## caracter puede contener letras, digtos, y signos de puntuacion

contraseña = "".join(random.choice(caracter)for i in range(longitud))

##la contraseña se concatena con caracter en cual sera el numero de longitud que adoptara la generacion de la misma

print("la contraseña generada es: "+contraseña)