# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 15:36:17 2016
@author: Erick Obregon Fonseca
@carnet: 2016123157
"""
from scipy import misc
import matplotlib.pyplot as plotter
import numpy
import sys

from imgfilter import Filtro


def test1():
    # Cambia el limite de la pila
    sys.setrecursionlimit(10**6)
    print("Test 1 running")
    # Variable para almacenar el nombre o la ruta donde se extraera la imagen
    imagenAbrir = str(input("Digite el nombre o la ruta de la imagen a trabajar: "))
    # Abrir imagen
    imagenGS = misc.imread(imagenAbrir, 1)
    # Definir el numero de filas a trabajar
    numFilas = len(imagenGS)
    # Definir el numero de columnas a trabajar
    numColumnas =len(imagenGS[0])
    # Preguntar al usuario el ancho de la ventana
    anchoVentana = (int(input("Por favor digite el ancho de la ventana: ")))
    # Inicializacion en ceros de la imagen
    imagenFiltrada = numpy.zeros((numFilas, numColumnas))
    # Crear filtrador
    filtrador = Filtro(numFilas, numColumnas) 
    # Lectura de la imagen en escala de grises
    plotter.imshow(imagenGS, plotter.get_cmap('gray'))
    # Muestra de la imagen en escala de grises
    plotter.show()
    # Llamado para el filtrado de la imagen
    filtrador.filtroDeMedianas(imagenGS, anchoVentana, imagenFiltrada)
    print("Esta es su imagen filtrada")
    # Mostrar imagen filtrada
    plotter.imshow(imagenFiltrada, plotter.get_cmap('gray'))
    plotter.show()
    # Variable donde se almacena el nombre o la ruta donde se guardara la imagen
    nombreGuardar = str(input("Donde guardara la imagen y con que nombre? "))
    # Guardar imagen filtrada
    misc.imsave(nombreGuardar, imagenFiltrada)
    # Informar que la imagen fue guardada
    print("Su imagen fue guardada con exito!")
    print("Terminado!")

# Realizar prueba
test1() 
