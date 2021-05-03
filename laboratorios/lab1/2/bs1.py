from Nodos import Nodo
import copy

def busqueda_BPPR(nodo_inicial, visitado, to_kill):
    visitado.append(nodo_inicial.get_estado())

    for idx_fila_actual, fila_actual in enumerate(nodo_inicial.get_estado()):
        for idx_celda_actual, celda_actual in enumerate(fila_actual):
            if celda_actual == 'B':
                to_kill+=1

    if to_kill <= 0:
        return nodo_inicial
    else:
        # Expandir nodos sucesores (hijos)
        datos_nodo = nodo_inicial.get_estado()

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

        #->
        if actual_posicion_columna >= 0 and actual_posicion_columna<=2:
            nueva_posicion_columna = actual_posicion_columna + 1
            datos_hijo_derecha[actual_posicion_fila][actual_posicion_columna] = '0'
            datos_hijo_derecha[actual_posicion_fila][nueva_posicion_columna]  = 'A'

            if datos_hijo_derecha[actual_posicion_fila][nueva_posicion_columna] == 'B':
                print("posicio: {} {}".format(actual_posicion_fila,nueva_posicion_columna))
                #visitado.clear()
            hijo_derecha = Nodo(datos_hijo_derecha)
            lista_hijos.append(hijo_derecha)
        #down
        if actual_posicion_fila >=0 and actual_posicion_fila<=2:
            nueva_posicion_fila = actual_posicion_fila + 1
            datos_hijo_abajo[actual_posicion_fila][actual_posicion_columna] = '0'
            datos_hijo_abajo[nueva_posicion_fila][actual_posicion_columna]  = 'A'
            if datos_hijo_abajo[nueva_posicion_fila][actual_posicion_columna] == 'B':
                print("posicio: {} {}".format(nueva_posicion_fila,actual_posicion_columna))
                #visitado.clear()
            hijo_abajo = Nodo(datos_hijo_abajo)
            lista_hijos.append(hijo_abajo)
        #<-
        if actual_posicion_columna >=1 and actual_posicion_columna<=3:
            nueva_posicion_columna = actual_posicion_columna - 1
            datos_hijo_izquierda[actual_posicion_fila][actual_posicion_columna] = '0'
            datos_hijo_izquierda[actual_posicion_fila][nueva_posicion_columna]  = 'A'
            if datos_hijo_izquierda[actual_posicion_fila][nueva_posicion_columna] == 'B':
                print("posicio: {} {}".format(actual_posicion_fila,nueva_posicion_columna))
                #visitado.clear()
            hijo_izquierda = Nodo(datos_hijo_izquierda)
            lista_hijos.append(hijo_izquierda) 
        #up
        if actual_posicion_fila >=1 and actual_posicion_fila<=3:
            nueva_posicion_fila = actual_posicion_fila - 1
            datos_hijo_arriba[actual_posicion_fila][actual_posicion_columna] = '0'
            datos_hijo_arriba[nueva_posicion_fila][actual_posicion_columna]  = 'A'
            if datos_hijo_arriba[nueva_posicion_fila][actual_posicion_columna] == 'B':
                print("posicio: {} {}".format(actual_posicion_fila,nueva_posicion_columna))
            hijo_arriba = Nodo(datos_hijo_arriba)
            lista_hijos.append(hijo_arriba)
        
        nodo_inicial.set_hijo(lista_hijos)
        

        for nodo_hijo in nodo_inicial.get_hijo():
            if not nodo_hijo.get_estado() in visitado:
                # Llamada Recursiva
                Solution = busqueda_BPPR(nodo_hijo, visitado,0)
                if Solution is not None:
                    return Solution
        return None
        

if __name__ == "__main__":
    estado_inicial = [['0', 'B', '0', '0'], 
                      ['0', '0', '0', 'A'], 
                      ['0', '0', 'B', '0'],
                      ['0', 'B', '0', 'B']]

    """solucion = [['0', 'X', '0', '0'], 
                ['0', '0', '0', '0'], 
                ['0', '0', '0', '0'],
                ['0', '0', '0', '0']]"""
    
    nodo_solucion = None
    visitado = []
    nodo_inicial = Nodo(estado_inicial)
    nodo_actual = busqueda_BPPR(nodo_inicial, visitado,0)

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