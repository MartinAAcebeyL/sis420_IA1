from Nodos import Nodo
import copy


def busqueda_BPPR(nodo_inicial, solucion, visitado, to_kill=0):
    visitado.append(nodo_inicial.get_estado())
    if nodo_inicial.get_estado() == solucion:
        return nodo_inicial
    else:
        # Expandir nodos sucesores (hijos)
        datos_nodo = nodo_inicial.get_estado()
        for estado in datos_nodo:
            for fila in estado:
                print(fila, end=' ')
            print()
        print("-----")

        #encontramos la posicion de un elemento
        actual_posicion_fila = -1
        actual_posicion_columna = -1
        
        for idx_fila_actual, fila_actual in enumerate(datos_nodo):
            for idx_celda_actual, celda_actual in enumerate(fila_actual):
                if celda_actual == 'A':
                    actual_posicion_fila = idx_fila_actual
                    actual_posicion_columna = idx_celda_actual
                    break
            if actual_posicion_fila > -1:
                break

        lista_hijos = []
        datos_hijo_abajo = []
        datos_hijo_arriba = []
        datos_hijo_derecha = []
        datos_hijo_izquierda = []
        #copias profundas de objetos de datos_nodo      
        datos_hijo_abajo = copy.deepcopy(datos_nodo)
        datos_hijo_arriba = copy.deepcopy(datos_nodo)
        datos_hijo_derecha = copy.deepcopy(datos_nodo)
        datos_hijo_izquierda = copy.deepcopy(datos_nodo)

        nueva_posicion_fila = -1
        nueva_posicion_columna = -1

        _destruidos = 0
        _mar = 0
        #->
        if actual_posicion_columna >= 0 and actual_posicion_columna<3:
            nueva_posicion_columna = actual_posicion_columna + 1
            if datos_hijo_derecha[actual_posicion_fila][nueva_posicion_columna] == '0':
                datos_hijo_derecha[actual_posicion_fila][actual_posicion_columna] = '0'
                datos_hijo_derecha[actual_posicion_fila][nueva_posicion_columna]  = 'A'
                _mar += 1
            elif datos_hijo_derecha[actual_posicion_fila][nueva_posicion_columna] == 'B':
                datos_hijo_derecha[actual_posicion_fila][actual_posicion_columna] = '0'
                datos_hijo_derecha[actual_posicion_fila][nueva_posicion_columna]  = 'X'
                _destruidos += 1
            hijo_derecha = Nodo(datos_hijo_derecha)
            lista_hijos.append(hijo_derecha)
        #<-
        if actual_posicion_columna in range(1,4):
            nueva_posicion_columna = actual_posicion_columna - 1
            if datos_hijo_izquierda[actual_posicion_fila][nueva_posicion_columna] == '0':
                datos_hijo_izquierda[actual_posicion_fila][actual_posicion_columna] = '0'
                datos_hijo_izquierda[actual_posicion_fila][nueva_posicion_columna]  = 'A'
                _mar += 1 
            elif datos_hijo_izquierda[actual_posicion_fila][nueva_posicion_columna] == 'B':
                datos_hijo_izquierda[actual_posicion_fila][actual_posicion_columna] = '0'
                datos_hijo_izquierda[actual_posicion_fila][nueva_posicion_columna]  = 'X'
                _destruidos += 1
            hijo_izquierda = Nodo(datos_hijo_izquierda)
            lista_hijos.append(hijo_izquierda) 
        #down
        if actual_posicion_fila in range(0,3):
            nueva_posicion_fila = actual_posicion_fila + 1
            if datos_hijo_abajo[nueva_posicion_fila][actual_posicion_columna] == '0':
                datos_hijo_abajo[actual_posicion_fila][actual_posicion_columna] = '0'
                datos_hijo_abajo[nueva_posicion_fila][actual_posicion_columna]  = 'A'
                _mar += 1
            elif datos_hijo_abajo[nueva_posicion_fila][actual_posicion_columna] == 'B':
                datos_hijo_abajo[actual_posicion_fila][actual_posicion_columna] = '0'
                datos_hijo_abajo[nueva_posicion_fila][actual_posicion_columna]  = 'X'
                _destruidos += 1
            hijo_abajo = Nodo(datos_hijo_abajo)
            lista_hijos.append(hijo_abajo) 
        #up
        if actual_posicion_fila in (1,4):
            nueva_posicion_fila = actual_posicion_fila - 1
            if datos_hijo_arriba[nueva_posicion_fila][actual_posicion_columna] == '0':
                datos_hijo_arriba[actual_posicion_fila][actual_posicion_columna] = '0'
                datos_hijo_arriba[nueva_posicion_fila][actual_posicion_columna]  = 'A'
                _mar += 1
            elif datos_hijo_arriba[nueva_posicion_fila][actual_posicion_columna] == 'B':
                datos_hijo_arriba[actual_posicion_fila][actual_posicion_columna] = '0'
                datos_hijo_arriba[nueva_posicion_fila][actual_posicion_columna]  = 'X'
                _destruidos += 1
            hijo_arriba = Nodo(datos_hijo_arriba)
            lista_hijos.append(hijo_arriba)
        
        nodo_inicial.set_hijo(lista_hijos)
        """for estado in nodo_inicial.get_estado():
            for fila in estado:
                print(fila, end=' ')
            print()
        print("-----")"""

        for nodo_hijo in nodo_inicial.get_hijo():
            if not nodo_hijo.get_estado() in visitado:
                # Llamada Recursiva
                Solution = busqueda_BPPR(nodo_hijo, solucion, visitado,to_kill=0)
                if Solution is not None:
                    return Solution
        #return None
        

if __name__ == "__main__":
    estado_inicial = [['0', 'B', '0', '0'], 
                      ['A', '0', '0', '0'], 
                      ['0', '0', '0', '0'],
                      ['0', '0', '0', '0']]

    solucion = [['0', 'X', '0', '0'], 
                ['0', '0', '0', '0'], 
                ['0', '0', '0', '0'],
                ['0', '0', '0', '0']]

    nodo_solucion = None
    visitado = []
    nodo_inicial = Nodo(estado_inicial)
    nodo_actual = busqueda_BPPR(nodo_inicial, solucion, visitado)

   # print(nodo_actual.get_estado())
#    Mostrar Resultado
    resultado = []
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_estado())
        nodo_actual = nodo_actual.get_padre()
    resultado.append(nodo_inicial.get_estado())
    resultado.reverse()
    
    for estado in resultado:
        for fila in estado:
            print(fila)
        print("---------")