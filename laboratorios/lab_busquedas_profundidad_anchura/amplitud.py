# Busqueda en Amplitud - Breadth First Search
from Nodos import Nodo
from timeit import default_timer

def busqueda_BPA_solucion(estado_inicial, solucion):
    if len(estado_inicial) != len(solucion):
        return 'dimenciones incorectas'
    x = len(estado_inicial)
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []

    nodo_raiz = Nodo(estado_inicial)
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and len(nodos_frontera) != 0:
        
        nodo_actual = nodos_frontera.pop(0)
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_estado() == solucion:
            # solucion encontrada
            resuelto = True
            return nodo_actual
        else:
            # expandir nodos hijo
            estado_nodo = nodo_actual.get_estado()
            #print(estado_nodo)
            hijo=estado_nodo.copy()
            #print(str(hijo)+' '+str(estado_nodo))
            aux =[]
            for i in range(0,x-1):
                c = hijo[i+1]
                hijo[i+1]=hijo[i]
                hijo[i] = c
                hijo_x = Nodo(hijo)
                if not hijo_x.en_lista(nodos_visitados) and not hijo_x.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo_x)
                aux.append(hijo_x)
               
                hijo = estado_nodo.copy()
            #print('salimos')
            nodo_actual.set_hijo(aux)
            #print(nodo_actual)
        #print(nodo_actual)
            
            #nodo_actual.set_hijo([hijo_izquierda, hijo_centro, hijo_derecha])


if __name__ == "__main__":
    inicio = default_timer()
    estado_inicial = [6,5, 4, 3, 2, 1]
    solucion = [1, 2, 3, 4,5,6]
    nodo_solucion = busqueda_BPA_solucion(estado_inicial, solucion)
    if type(nodo_solucion) == str:
        print(nodo_solucion)
    else:
        # mostrar resultado
        resultado = []
        nodo_actual = nodo_solucion
        while nodo_actual.get_padre() is not None:
            resultado.append(nodo_actual.get_estado())
            nodo_actual = nodo_actual.get_padre()

        resultado.append(estado_inicial)
        resultado.reverse()
        print(resultado)
    print('tiempo de ejecucion {} seg.'.format(default_timer()-inicio))