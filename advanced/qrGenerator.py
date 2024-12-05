##############################################################################################
### Project: Generador de Códigos QR                                                       ###
### Author: Guillermo Ayllon                                                               ###
### Date: 05/12/2024                                                                       ###
### Vers: 1.0                                                                              ###
### Level: Advanced                                                                        ###
### Description: Generador de códigos qr  en Python.                                       ###
##############################################################################################

## Para poder realizar el proyecto deberemos iinstalar previamente la libreria qrcode

import qrcode
import qrcode.constants

qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = 10,     border = 2)

qr.add_data("https://guillermoayllon.com")
qr.make(fit = True)

img = qr.make_image(fill_color = "black",
                    back_color = 'white'
                    
)

img.save("myQr.png")