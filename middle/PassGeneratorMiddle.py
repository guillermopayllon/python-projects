##############################################################################################
### Project: Generador de contraseñas                                                      ###
### Author: Guillermo Ayllon                                                               ###
### Date: 03/12/2024                                                                       ###
### Vers: 1.0                                                                              ###
### Level: Middle                                                                          ###
### Description: Generador de contraseñas intermedio en Python.                            ###
##############################################################################################

import string
import random

size = int(input("¿Cuál es la longitud de la contraseña que necesitas?: "))

characters = string.ascii_letters + string.digits + string.punctuation

while True:
    print("\n--- Menú de Gestión de contraseñas ---")
    print("1. Generar contraseña aleatoria.")
    print("2. Generar contraseña solo numerica.")
    print("3. Generar contraseña letras minúsculas.")
    print("4. Generar contraseña letras mayúsculas.")
    print("5. Generar contraseña solo caracteres.")
    print("6. Salir.")
    
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            password = "".join(random.choice(characters)for i in range(size))
            print("La contraseña es: " + password)
        elif opcion == 2:
            password = "".join(random.choice(string.digits)for i in range(size))
            print("La contraseña es: " + password)
        elif opcion == 3:
            password = "".join(random.choice((string.ascii_letters).lower())for i in range(size))
            print("La contraseña es: " + password)
        elif opcion == 4:
            password = "".join(random.choice((string.ascii_letters).upper())for i in range(size))
            print("La contraseña es: " + password)
        elif opcion == 5:
            password = "".join(random.choice(string.punctuation)for i in range(size))
            print("La contraseña es: " + password)
        elif opcion == 6:
            print("Hasta pronto!!")
            break
        else:
            print("Opción no valida, por favor intentelo nuevamente.")
            
    except ValueError:
        print("Selección no valida")
    