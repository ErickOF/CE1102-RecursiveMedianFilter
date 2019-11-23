import numpy as np


# Clase filtro
class Filtro:
    # Inicializar el constructor de la clase
    def __init__(self, numFilas, numColumnas):
        self.numFilas = numFilas
        self.numColumnas = numColumnas

    # Metodo de filtrar por medianas
    def filtroDeMedianas(self, imagenGS, anchoVentana, imagenFiltrada): 
        # Se iniciliza la fila actual en cero
        filaActual = 0
        # Filtrar imagen del ruido
        imagenFiltrada = self.filtrar(imagenGS, anchoVentana, filaActual, imagenFiltrada)
        # Imagen ya filtrada de ruido parcialmente
        return imagenFiltrada

    # Metodo para filtrar la imagen
    def filtrar(self, imagenGS, anchoVentana, filaActual, imagenFiltrada):
        # Cuando el numero de filas actuales sea menor al de la imagen
        if (filaActual < self.numFilas):
            # Filtrar por filas
            self.filtroDeFilas(imagenGS, filaActual, anchoVentana, [], imagenFiltrada)
            return imagenFiltrada
        else:
            return imagenFiltrada

    # Metodo para filtrar filas
    def filtroDeFilas(self, imagenGS, filaActual, anchoVentana, filaFiltrada, imagenFiltrada):
        # Se inicializa la fila Actual en cero
        columnaActual = 0
        # Obtener fila filtrada
        filaFiltrada = self.matriz(imagenGS, anchoVentana, columnaActual, filaActual, filaFiltrada)
        # Sumar la fila filtrada a la imagen filtrada
        imagenFiltrada[filaActual] += filaFiltrada
        # Volver a llamar al metodo filtrar
        return self.filtrar(imagenGS, anchoVentana, filaActual + 1, imagenFiltrada)

    def matriz(self, imagenGS, anchoVentana, columnaActual, filaActual, filaFiltrada):
        # Se encarga de realizar todos los pasos para sacar la mediana
        # Cuando la columana actual es menor que el total de columnas
        if (columnaActual < self.numColumnas):
            # Variable para tomar los pixeles de la izquierda y arriba
            x = -(anchoVentana - ((anchoVentana // 2) + 1 ))
            # Variable para tomar los pixeles de la derecha y abajo
            y = anchoVentana - (anchoVentana // 2)
            if (columnaActual + x < 0 or filaActual + x < 0 or y + filaActual > self.numFilas or y + columnaActual > self.numColumnas):
                filaFiltrada += [imagenGS[filaActual][columnaActual]]
                return self.matriz(imagenGS, anchoVentana, columnaActual + 1, filaActual, filaFiltrada)
            else:
                # Tomar ventana 
                tomarVentana = imagenGS[filaActual + x : filaActual + y, columnaActual + x : columnaActual + y]
                # Convertir ventana a matriz
                matriz = tomarVentana.tolist()
                # Unir la matrices en una lista plana
                lista = self.concatenarMatriz(matriz, anchoVentana, [])
                # Llamar el metodo de ordenamiento de la lista
                listaOrdenada = self.burbuja(lista)
                # Sacar mediana
                mediana = self.sacarMediana(listaOrdenada)
                # Hacer recursivo del llamado del metodo
                # Mover a la siguiente columna y sumar la mediana
                return self.matriz(imagenGS, anchoVentana, columnaActual + 1, filaActual, filaFiltrada + [mediana])
        # Devolver las fila filtrada
        else:
            return filaFiltrada

    def concatenarMatriz(self, matriz1, anchoVentana, matriz):
        # Condicion de parada
        if (matriz1 == []):
            # Regresar la matrz
            return matriz
        # Sumar cada pixel de la matriz
        else:
            matriz += matriz1[len(matriz1) - 1]
            return self.concatenarMatriz(matriz1[:-1], anchoVentana - 1, matriz)

    # Metodo de ordenamiento burbuja
    def burbuja(self, lista):
        # Verificar si esta ordenada
        if (self.ordenada(lista) == True):
            # Devolver la matriz ordenada
            return lista
        # Ordenar matriz
        else:
            return self.burbuja(self.burbujaAux(lista, []))

    # Metodo para saber si la matriz esta ordenada
    def ordenada(self, lista):
        # Condicion de parada
        if (len(lista) == 1):
            # Devolver que la matriz si estaba ordenada
            return True
        # Evaluar cada elemento de menor a mayor
        elif (lista[0] <= lista[1]):
            # Llamado recursivo del metodo
            return self.ordenada(lista[1:])
        # Devolver que la lista no esta ordenada
        else:
            return False

    # Metodo que ordena la lista
    def burbujaAux(self, lista, listaOrdenada):
        # Cuando solo queda un elemento
        if (len(lista) == 1):
            # Sumar el ultimo elemento de la lista
            return listaOrdenada + lista
        # Ordenar elementos de menor a mayor
        # Si el primier elemento es menor al segundo
        elif (lista[0] <= lista[1]):
            # Se corta y se suma a la matriz ordenada
            return self.burbujaAux(lista[1:], listaOrdenada + [lista[0]])
        # Cuando el primer elemento es mayor que el primero
        else:
            # Se mantiene el primer elemento y el segundo se suma a la lista ordenada
            return self.burbujaAux([lista[0]] + lista[2:], listaOrdenada + [lista[1]])

    # Metodo para obtener la mediana
    def sacarMediana(self, listaOrdenada):
        # Sacar la mediana de una ventana
        mediana = listaOrdenada[len(listaOrdenada) // 2]
        # Devolver la mediana
        return mediana
