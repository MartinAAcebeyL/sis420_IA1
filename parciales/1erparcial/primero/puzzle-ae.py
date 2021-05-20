import math
import time
from queue import PriorityQueue

class Tablero:
    def __init__(self, estados):
        self.tamano = 4    
        self.estados = estados
        self.tab=[]

    def ejecutar_accion(self, accion):
        nuevos_estados = self.estados[:]
        indice_vacio_1 = nuevos_estados.index('0')

        para_nxm = []
        intervalo_superior = 4
        for intervalo_inferior in range(0,len(nuevos_estados),4):
            para_nxm.append(nuevos_estados[intervalo_inferior:intervalo_superior])
            intervalo_superior += 4

        self.tab = para_nxm
        
        #2da fase
        if indice_vacio_1 in range(0, len(nuevos_estados)//4):
            fila = 0
        elif indice_vacio_1 in range(4, len(nuevos_estados)*1//2):
            fila = 1
        elif indice_vacio_1 in range(8, len(nuevos_estados)*3//4):
            fila = 2
        elif indice_vacio_1 in range(12, len(nuevos_estados)):
            fila = 3
        columna = para_nxm[fila].index('0')

        if accion == 'L':
            if columna > 0:
                nuevos_estados[indice_vacio_1 - 1], nuevos_estados[indice_vacio_1] = nuevos_estados[indice_vacio_1], nuevos_estados[indice_vacio_1 - 1]
        if accion == 'R':
            if columna < 3:
                nuevos_estados[indice_vacio_1 + 1], nuevos_estados[indice_vacio_1] = nuevos_estados[indice_vacio_1], nuevos_estados[indice_vacio_1 + 1]
        if accion == 'U':
            if fila > 0:
                nuevos_estados[indice_vacio_1 - self.tamano], nuevos_estados[indice_vacio_1] = nuevos_estados[indice_vacio_1], nuevos_estados[indice_vacio_1 - self.tamano]
        if accion == 'D':
            if fila < 3:
                nuevos_estados[indice_vacio_1 + self.tamano], nuevos_estados[indice_vacio_1] = nuevos_estados[indice_vacio_1], nuevos_estados[indice_vacio_1 + self.tamano]
        
        return Tablero(nuevos_estados)

class Nodo:
    def __init__(self, estado:Tablero = None, padre = None, accion = None):
        self.estado = estado
        self.padre = padre
        self.accion = accion

    def __repr__(self):
        return str(self.estado.estados)

    def __eq__(self, otro):
        return self.estado.estados == otro.estado.estados

    def __hash__(self):
        return hash(self.estado)

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

def hamming(estados:Tablero):
    ''' heuristicaa Hamming: cuenta el numero de posiciones erroneas en diferentes estados'''
    cant_posiciones_erroneas = 0
    objetivo_estados = goal_test()
    for i in objetivo_estados:
        if abs(objetivo_estados.index(i) - estados.index(i)) != 0:# and i != 0:
            cant_posiciones_erroneas += 1
    return cant_posiciones_erroneas

def manhattan_calculate(estados):
    '''heuristicaa Manhattan: cuenta el numero de cuadros a
    partir de una ubicacion en relacion a su posicion final'''
    contador = 0
    for i in range(0, 15):
        index = estados.index(str(i + 1))  # because range starts at 0
        contador += (abs((i / 4) - (index / 4)) + abs((i % 4) - (index % 4)))  # %4 is the column and /4 is the row
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
    return ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15','0']

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
                minim.append(manhattan_calculate(x.estado.estados) + gcalc(x) )
            holder.append(x)
        m = min(minim)  #finds minimum F value
        estado_inicial = holder[minim.index(m)]
        #print(estado_inicial.estado.estados)
        
        #print(estado_inicial.estado.tab)
        if estado_inicial.estado.estados == estado_objetivo:  # solution found!
            x=str(' '.join(find_path(estado_inicial)))
            print("Solucion: ")
            print("Movimientos: " + x)
            print("Numero de nodos expandidos: " + str(contador))
            end_time = time.time()
            print("Tiempo empleado: " + str(round((end_time - start_time), 3)))
            return x

        frontera.pop(frontera.index(estado_inicial))
        for hijo in get_hijos(estado_inicial):
            contador += 1
            s = hijo.estado
            if s not in visitado: #or gcalc(hijo) < gcalc(visitado[s]):
                visitado[s] = hijo
                frontera.append(hijo)

def main():
    ei = ['1', '3', '4', '8', '5', '2', '0', '6', '9', '10', '7', '11', '13', '14', '15', '12']
    # ei = ['0', '15', '14', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '1', '2', '3']

    heuristica = input("Enter heuristica either 'H' or 'M' (H is Hamming and M is Manhattan): ")
    if heuristica.upper() == 'H':
        heuristica = 0
    elif heuristica.upper() == 'M':
        heuristica = 1

    #max_depth = 10
    root = Nodo(estado = Tablero(ei))

    x=astar(estado_inicial = root, estado_objetivo = goal_test(), heuristica = heuristica)
    print(x)
    

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()