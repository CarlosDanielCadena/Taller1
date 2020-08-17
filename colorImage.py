
'''
/////////////////////////////////////////////
//    PONTIFICIA UNIVERSIDAD JAVERIANA     //
//                                         //
//  Carlos Daniel Cadena Cahvarro          //
//  Procesamiento de imagenes              //
//  TALLER #1                              //
/////////////////////////////////////////////
'''

import numpy as np
import cv2
import os

class colorImage:

    def __init__(self, path):                   # Constructor
        self.image = cv2.imread(path, 1)        # Imagen original 1
        self.image2 = cv2.imread(path, 1)       # Imagen original 2
        #cv2.imshow("Original", self.image)     # Impresion de imagen original
        #cv2.waitKey(1000)

    def displayProperties(self):                            # Método displayProperties
        height, width, channels = self.image.shape          # Obtener el tamaño de la imagen
        print(f"El ancho de la imagen es: {width} \nEl largo de la imagen es: {height}") # Imprimir el tamaño de la imagen

    def makeGray(self):                                             # Método makeGray
        self.gris = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)    # Pasar de BGR a Grises
        cv2.imshow("Escala de grises", self.gris)                   # Imprimir imagen a escala de grises
        cv2.waitKey(1000)                                           # Esperar 1s antes de seguir

    def colorizeRGB(self, x):               # Método colorizeRGB
        if x == "red":                      # Condición para rojo
            self.image[:, :, 0] = 0         # Eliminar componentes azules
            self.image[:, :, 1] = 0         # Eliminar componentes verdes
            self.image[:, :, 1] = self.gris # Grises en componente roja
            cv2.imshow("Rojo", self.image)  # Imprimir imagen rojiza
            cv2.waitKey(1000)               # Esperar 1s antes de seguir

        elif x == 'green':                  # Condición para verde
            self.image[:, :, 0] = 0         # Eliminar componentes azules
            self.image[:, :, 2] = 0         # Eliminar componentes rojas
            self.image[:, :, 1] = self.gris # Grises en componente verde
            cv2.imshow("Verde", self.image) # Imprimir imagen verdoza
            cv2.waitKey(1000)               # Esperar 1s antes de seguir

        elif x == 'blue':                   # Condición para azul
            self.image[:, :, 1] = 0         # Eliminar componentes verdes
            self.image[:, :, 2] = 0         # Eliminar componentes rojas
            self.image[:, :, 1] = self.gris # Grises en componente azul
            cv2.imshow("Azul", self.image)  # Imprimir imagen azuloza
            cv2.waitKey(1000)               # Esperar 1s antes de seguir

    def makeHue(self):                                          # Método makeHue
        self.HSV = cv2.cvtColor(self.image2, cv2.COLOR_BGR2HSV) # Pasar de BGR a HSV
        self.HSV[:, :, 1] = 255                                 # Componente H con valor constante de 255
        self.HSV[:, :, 2] = 255                                 # Componente V con valor constante de 255
        self.HSV = cv2.cvtColor(self.HSV, cv2.COLOR_HSV2BGR)    # Pasar de HSV a BGR
        cv2.imshow("HSV", self.HSV)                             # Imprimir imagen HSV convertida
        cv2.waitKey(0)                                          # Esperar para finalizar
