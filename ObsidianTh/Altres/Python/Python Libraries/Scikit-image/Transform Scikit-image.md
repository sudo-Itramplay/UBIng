transform té a veure en tota la manipulació de dades

`.resize(imatge, (novamidaR , novamidaC), antialiasing=Bool`

després de fer un resize és possible que es necessiti una normalització de base 1 a 255
->`(resized_image*255).astype(np.uint8)`
