from Nodos import Nodo
import copy


def busqueda_BPPR(nodo_inicial, solucion, visitado):
    visitado.append(nodo_inicial.get_estado())
    if nodo_inicial.get_estado() == solucion:
        return nodo_inicial
    else:
        # Expandir nodos sucesores (hijos)
        datos_nodo = nodo_inicial.get_estado()
        
        actual_posicion_fila = -1
        actual_posicion_columna = -1

        for idx_fila_actual, fila_actual in enumerate(datos_nodo):
#             print(idx_fila_actual, fila_actual)
            for idx_celda_actual, celda_actual in enumerate(fila_actual):
#                 print(idx_celda_actual, celda_actual)
                if celda_actual == 'X':
                    actual_posicion_fila = idx_fila_actual
                    actual_posicion_columna = idx_celda_actual
                    break
            if actual_posicion_fila > -1:
                break
        nueva_posicion_fila = -1
        nueva_posicion_celda = -1

        lista_hijos = []
        #copias profundas de objetos de datos_nodo
        datos_hijo_abajo = copy.deepcopy(datos_nodo)
        datos_hijo_arriba = copy.deepcopy(datos_nodo)
        datos_hijo_derecha = copy.deepcopy(datos_nodo)
        datos_hijo_izquierda = copy.deepcopy(datos_nodo)
   

        if actual_posicion_columna in range(1,4):
            nueva_posicion_celda = actual_posicion_columna - 1
            datos_hijo_izquierda[actual_posicion_fila][actual_posicion_columna] = '0'
            datos_hijo_izquierda[actual_posicion_fila][nueva_posicion_celda] = 'X'
            hijo_izquierda = Nodo(datos_hijo_izquierda)
#             print(hijo_izquierda.get_estado())
            lista_hijos.append(hijo_izquierda) 

        if actual_posicion_fila in range(0,2):
            nueva_posicion_fila = actual_posicion_fila + 1
            datos_hijo_abajo[actual_posicion_fila][actual_posicion_columna] = '0'
            datos_hijo_abajo[nueva_posicion_fila][actual_posicion_columna] = 'X'
            hijo_abajo = Nodo(datos_hijo_abajo)
#             print(hijo_abajo.get_estado())
            lista_hijos.append(hijo_abajo) 
            
        if actual_posicion_fila in range(1,3):
            nueva_posicion_fila = actual_posicion_fila - 1
            datos_hijo_arriba[actual_posicion_fila][actual_posicion_columna] = '0'
            datos_hijo_arriba[nueva_posicion_fila][actual_posicion_columna] = 'X'
            hijo_arriba = Nodo(datos_hijo_arriba)
#             print(hijo_arriba.get_estado())
            lista_hijos.append(hijo_arriba)
            
        if actual_posicion_columna in range(0,2):
            nueva_posicion_celda = actual_posicion_columna + 1
            datos_hijo_derecha[actual_posicion_fila][actual_posicion_columna] = '0'
            datos_hijo_derecha[actual_posicion_fila][nueva_posicion_celda] = 'X'
            hijo_derecha = Nodo(datos_hijo_derecha)
#             print(hijo_derecha.get_estado())
            lista_hijos.append(hijo_derecha)
                 
#         print(lista_hijos)
        nodo_inicial.set_hijo(lista_hijos)

        """for estado in nodo_inicial.get_estado():
            for fila in estado:
                print(fila, end=' ')
            print()
        print("-----")"""
        
        for nodo_hijo in nodo_inicial.get_hijo():
            if not nodo_hijo.get_estado() in visitado:
                # Llamada Recursiva
                Solution = busqueda_BPPR(nodo_hijo, solucion, visitado)
                if Solution is not None:
                    return Solution
        return None

if __name__ == "__main__":
    estado_inicial = [['0', '0', '0'], 
                      ['0', '0', 'X'], 
                      ['0', '0', '0']]

    solucion = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', 'X']]
    nodo_solucion = None
    visitado = []
    nodo_inicial = Nodo(estado_inicial)
    nodo_actual = busqueda_BPPR(nodo_inicial, solucion, visitado)

#     print(nodo_actual.get_estado())
#     Mostrar Resultado
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