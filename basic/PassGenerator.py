##############################################################################################
### Project: Generador de contraseñas                                                      ###
### Author: Guillermo Ayllon                                                               ###
### Date: 03/12/2024                                                                       ###
### Vers: 1.0                                                                              ###
### Description: Generador de contraseñas básico en Python.                                ###
##############################################################################################

import string
import random

## Declaramos una variale size en la que el usuario podrá indicar la longitud de la contraseña.
size = int(input("¿Cuál es la longitud de la contraseña que necesitas?: "))

characters = string.ascii_letters + string.digits + string.punctuation

# La variable characters contendrá todos los tipos de carácteres que se pueden incluir
# ascii_letters = Todas las letras mayúsculas y minúsculas
# digits = Todos los números del 0 al 9
# punctuation = Todos los carácteres especiales.

password = "".join(random.choice(characters)for i in range(size))

# La variable password es donde se generará la contraseña aleatoria.
# Esta contraseña se genera gracias a Random
# Usamos un bucle for para que genere tantos caracteres como longitud queramos para la contraseña.


# Mostramos la contraseña por consola.
print("La contraseña solicitada es: " + password)