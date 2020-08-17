
from colorImage import *         # Importar

if __name__ == "__main__":       # Main
    path = input("Por favor ingrese la ruta de la imagen: ")    # Ingreso de la ruta de la imagen
    imagen = colorImage(path)    # Llamado a la clase colorImage
    imagen.displayProperties()   # Llamado al metodo displayProperties
    imagen.makeGray()            # Llamado al metodo makeGray
    x = input("Por favor ingrese la componente del canal que desea ver (Ej: red, green o blue): ") # Ingreso del parametro
    imagen.colorizeRGB(x)        # Llamado al metodo colorizeRGB
    imagen.makeHue()             # Llamado al metodo makeHue
