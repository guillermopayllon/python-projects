##############################################################################################
### Project: Escaner de puertos                                                            ###
### Author: Guillermo Ayllon                                                               ###
### Date: 04/12/2024                                                                       ###
### Vers: 1.0                                                                              ###
### Level: Basic                                                                           ###
### Description: Escaner de puertos básico                                                 ###
##############################################################################################

import socket

ipAddress = input("¿Que dirección ip quieres escanear?: ")

for port in range(1, 65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ## AF_INET = Usamos protocolo IPV4
    ## SOCK_STREAM = Usamos TCP

    sock.settimeout(5)  ## Le damos un socket de 5 segundos
    
    result = sock.connect((ipAddress, port))
    
    if result == 0:
        print("Puerto Abierto: " +str(port))
        sock.close()
    else:
        print("Puerto Cerrado: " + str(port))



