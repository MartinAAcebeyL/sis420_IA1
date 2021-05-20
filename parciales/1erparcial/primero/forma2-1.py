import math
import os
import sys
import time
from queue import PriorityQueue

class Tablero:
    def __init__(self, estados):
        self.tamano = 5
        self.estados = estados

    def ejecutar_accion(self, accion):
        nuevos_estados = self.estados[:]
        indice_vacio_1 = nuevos_estados.index('0')
        
        para_nxm = []
        intervalo_superior = 5
        for intervalo_inferior in range(0,len(nuevos_estados),5):
            para_nxm.append(nuevos_estados[intervalo_inferior:intervalo_superior])
            intervalo_superior += 5
        
        #2da fase
        if indice_vacio_1 in range(0, len(nuevos_estados)*1//3):
            fila = 0
        elif indice_vacio_1 in range(3, len(nuevos_estados)*2//3):
            fila = 1
        elif indice_vacio_1 in range(6, len(nuevos_estados)):
            fila = 3
        
     
        columna = para_nxm[fila].index('0')

        if accion == 'L':
            if columna > 0:
                nuevos_estados[indice_vacio_1 - 1], nuevos_estados[indice_vacio_1] = nuevos_estados[indice_vacio_1], nuevos_estados[indice_vacio_1 - 1]
        if accion == 'R':
            if columna < 4:
                nuevos_estados[indice_vacio_1 + 1], nuevos_estados[indice_vacio_1] = nuevos_estados[indice_vacio_1], nuevos_estados[indice_vacio_1 + 1]
        if accion == 'U':
            if fila > 0:
                nuevos_estados[indice_vacio_1 - self.tamano], nuevos_estados[indice_vacio_1] = nuevos_estados[indice_vacio_1], nuevos_estados[indice_vacio_1 - self.tamano]
        if accion == 'D':
            if fila < 2:
                nuevos_estados[indice_vacio_1 + self.tamano], nuevos_estados[indice_vacio_1] = nuevos_estados[indice_vacio_1], nuevos_estados[indice_vacio_1 + self.tamano]
        print('------------')
        for i in para_nxm:
            print(i)
        print('------------')
        return Tablero(nuevos_estados)

class Nodo:
    def __init__(self, estado:Tablero = None, padre = None, accion = None):
        self.estado = estado
        self.padre = padre
        self.accion = accion


def get_hijos(padre_Nodo):
    hijos = []
    accions = ['L', 'R', 'U', 'D']
    for accion in accions:
        hijo_estado = padre_Nodo.estado.ejecutar_accion(accion)#mueve las fichas
        hijo_Nodo = Nodo(hijo_estado, padre_Nodo, accion)#exapnde, actualiza el table, y ejecuta la accion
        hijos.append(hijo_Nodo)
    return hijos

def gcalc(Nodo):
    ''' calcula g(n): encuentra el costo del estado actual a partir del estado origen o inicial'''
    contador = 0
    while Nodo.padre is not None:
        Nodo = Nodo.padre
        contador += 1
    return contador

def hamming(estados):
    ''' heuristicaa Hamming: cuenta el numero de posiciones erroneas en diferentes estados'''
    cant_posiciones_erroneas = 0
    objetivo_estados = goal_test()
    for i in objetivo_estados:
        if abs(objetivo_estados.index(i) - estados.index(i)) != 0:# and i != 0:
            cant_posiciones_erroneas += 1
    return cant_posiciones_erroneas

def manhattan_calculate(estados):
    contador = 0
    goal = goal_test()
    for i in range(0, 14):
        index = estados.index(str(i + 1))
        index1 = goal.index(str(i + 1))
        contador += abs(index1-index)
    return contador

def find_path(Nodo):
    '''Returns path back to input Nodo or source Nodo'''
    path = []
    while (Nodo.padre is not None):
        path.append(Nodo.accion)
        Nodo = Nodo.padre
    path.reverse()
    return path

def goal_test():
    return ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14','0']

def astar(estado_inicial:Nodo, estado_objetivo = goal_test(), heuristica = None):
    '''A* Search Algorithm'''
    start_time = time.time()

    frontera = list()
    contador = 0
    visitado = dict()

    #duda
    frontera.append(estado_inicial)
    visitado[estado_inicial.estado] = estado_inicial
   
    while frontera:
        minim = []
        holder = []
        for x in frontera:
            #x.estado.estados como a nodos su propiedad estado es una clase tablero, se hace una 
            # escala hasta estado, que es el tablero 
            if heuristica == 0:
                minim.append(hamming(x.estado.estados) + gcalc(x))  # This is the F = h + g
            elif heuristica == 1:
                minim.append(manhattan_calculate(x.estado.estados) + gcalc(x))
            holder.append(x)
        m = min(minim)  #finds minimum F value
        estado_inicial = holder[minim.index(m)]
        
        if estado_inicial.estado.estados == estado_objetivo:  # solution found!
            x=str(' '.join(find_path(estado_inicial)))
            print("Solucion: ")
            print("Movimientos: " + x)
            print("Numero de nodos expandidos: " + str(contador))
            end_time = time.time()
            print("Tiempo empleado: " + str(round((end_time - start_time), 3)))
            break

        frontera.pop(frontera.index(estado_inicial))
        for hijo in get_hijos(estado_inicial):
            contador += 1
            s = hijo.estado
            if s not in visitado or gcalc(hijo) < gcalc(visitado[s]):
                visitado[s] = hijo
                frontera.append(hijo)

def main():
    ei = ['1', '0','3', '4', '2', '5','6', '8', '7', '9', '10', '11','12', '13', '14']

    #heuristica = input("Enter heuristica either 'H' or 'M' (H is Hamming and M is Manhattan): ")
    """if heuristica.upper() == 'H':
        heuristica = 0
    elif heuristica.upper() == 'M':
        heuristica = 1"""

    #max_depth = 10
    root = Nodo(estado = Tablero(ei))

    astar(estado_inicial = root, estado_objetivo = goal_test(), heuristica = 1)
    

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()