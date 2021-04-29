from PIL import Image
img = Image.open("Plantillos/Pozole.jpg")

dimensiones = (240,180)
img.resize(dimensiones)
imagen_resize.save("imagen.jpg")
