# Búsqueda Coste Uniforme - Uniform Cost Search
from Nodos import Nodo

def Comparar(nodo):
    return nodo.get_costo()

def busqueda_BCU(conecciones, estado_inicial, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_raiz = Nodo(estado_inicial)
    nodo_raiz.set_costo(0)
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and len(nodos_frontera) != 0:
        # Ordenar lista de nodos frontera
        nodos_frontera = sorted(nodos_frontera, key=Comparar)
        nodo_actual = nodos_frontera[0]
        # Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo_actual.get_estado() == solucion:
            # Solucion encontrada
            resuelto = True
            return nodo_actual
        else:
            # Expandir nodos hijo (ciudades con conexion)
            datos_nodo = nodo_actual.get_estado()
            lista_hijos = []
            for achild in conecciones[datos_nodo]:
                hijo = Nodo(achild)
                costo = conecciones[datos_nodo][achild]
                hijo.set_costo(nodo_actual.get_costo() + costo)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados):
                    # Si está en la lista lo sustituimos con el nuevo valor de coste si es menor
                    if hijo.en_lista(nodos_frontera):
                        for n in nodos_frontera:
                            if n.equal(hijo) and n.get_costo() > hijo.get_costo():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                    else:
                        nodos_frontera.append(hijo)
            nodo_actual.set_hijo(lista_hijos)


if __name__ == "__main__":
    conecciones = {
        'Potosi': {'Puente Mendez':107, 'Porco':52,'k ingenio':40,'Challapata':193},
        'Puente Mendez':{'Potosi':107, 'Sucre':43},
        'Sucre':{'Puente Mendez':43,'Llallagua':234, 'Aiquile':135,'Monteagudo':289},
        'Monteagudo':{'Sucre':289, 'Cruce ipati':95},
        'Aiquile':{'Sucre':135,'Tolata':162,'La palizada':130},
        'La palizada':{'Aiquile':130,'Cochabamba':237,'Mataral':32},
        'Mataral':{'La palizada':32,'Santa cruz':186,'Guadalupe':59},
        'Guadalupe':{'Mataral':59},
        'Tolata':{'Aiquile':162,'Toro toro':112,'Cochabamba':46},
        'Toro toro':{'Tolata':112},
        'Llallagua':{'Sucre':234, 'Oruro':92},
        'Porco' :{'Potosi': 52, 'Uyuni':162},
        'Uyuni':{'Porco':162,'Hito lx':257,'Atocha':102,'Challapata':186},
        'Hito lx':{'Uyuni':257},
        'k ingenio':{'Potosi':40, 'Tumusla':90, 'Camargo':210},
        'Tumusla':{'k ingenio':90, 'Tupiza':120},
        'Tupiza':{'Tumusla':90,'Villazon':91,'Atocha':102},
        'Villazon':{'Tupiza':91},
        'Atocha':{'Tupiza':102, 'Uyuni':102},
        'Camargo':{'Tarija':102, 'k ingenio':210},
        'Tarija':{'Padcaya':43,'Camargo':102,'Palos blancos':174},
        'Padcaya':{'Bermejo':143,'Tarija':43},
        'Bermejo':{'Padcaya':143},
        'Palos blancos':{'Tarija':174,'Yacuiba':93,'Villamontes':70},
        'Yacuiba':{'Palos blancos':93,'Villamontes':107},
        'Villamontes':{'Palos blancos':70,'Hito br94':116,'Yacuiba':107, 'Boyuibe':98},
        'Hito br94':{'Villamontes':116},
        'Challapata':{'Uyuni':186,'Potosi':193,'Oruro':110},
        'Oruro':{'Challapata':110,'Huachacalla':162,'Totora':125,'Llallagua':92,'Pacatamaya':135,'Cochabamba':214},
        'Huachacalla':{'Oruro':162,'Pisiga':70},
        'Pisiga':{'Huachacalla':70},
        'Totora':{'Oruro':125,'Hito xviii':215,'Pacatamaya':223},
        'Hito xviii':{'Totora':215},
        'Pacatamaya':{'Oruro':135,'Totora':223,'La paz':81},
        'La paz':{'Pacatamaya':81, 'Desaguadero':95,'Huarina':94,'Yocumo':318},
        'Desaguadero':{'La paz':95},
        'Huarina':{'La paz':94,'Copacabana':76,'Escoma':93},
        'Copacabana':{'Huarina':76},
        'Escoma':{'Huarina':93},
        'Yocumo':{'La paz':318,'Rurenabaque':101,'San ignacio de Moxos':185},
        'Rurenabaque':{'Yocumo':101, 'Ixiamas':115,'El chorro':434},
        'Ixiamas':{'Rurenabaque':115},
        'El chorro':{'Rurenabaque':434,'Cobija':315,'Riveralta':71},
        'Cobija':{'El chorro':315},
        'Riveralta':{'El chorro':71,'Guayamerin':84},
        'Guayamerin':{'Riveralta':84},
        'San ignacio de Moxos':{'Yocumo':185,'Trinidad':89},
        'Trinidad':{'San ignacio de Moxos':89, 'San ramon':368},
        'San ramon':{'Trinidad':368, 'San ignacio de velasco':273,'Pailon':125},
        'San ignacio de velasco':{'San ramon':273,'San Matias':308,'San miguel':36},
        'San Matias':{'San ignacio de velasco':308},
        'San miguel':{'San ignacio de velasco':36,'San jose de chiquitos':168},
        'San jose de chiquitos':{'San miguel':168, 'Puerto suarez':355,'Pailon':252},
        'Puerto suarez':{'San jose de chiquitos':355,'Puerto bush':138},
        'Puerto bush':{'Puerto suarez':138},
        'Pailon':{'San jose de chiquitos':255,'San ramon':125, 'Santa cruz':61},
        'Santa cruz':{'Pailon':61,'Montero':62,'Mataral':186,'Abapo':153},
        'Abapo':{'Santa cruz':153, 'Cruce ipati':108,'Boyuibe':230},
        'Cruce ipati':{'Abapo':108, 'Boyuibe':140,'Monteagudo':95},
        'Boyuibe':{'Cruce ipati':108,'Abapo':230, 'Hito villazon':127,'Villamontes':98},
        'Hito villazon':{'Boyuibe':127},
        'Montero':{'Santa cruz':62,'Colonia pirai':135,'Okinawa':46,'Yapacani':67},
        'Colonia pirai':{'Montero':135},
        'Okinawa':{'Montero':46},
        'Yapacani':{'Montero':67,'Ivirgazama':64},
        'Ivirgazama':{'Yapacani':64,'Puerto villaroel':26,'Villa tunari':60},
        'Puerto villaroel':{'Ivirgazama':26},
        'Villa tunari':{'Ivirgazama':60,'Cochabamba':147},
        'Cochabamba':{'Villa tunari':147,'Oruro':214,'Tolata':46,'La palizada':237}
    }
    estado_inicial = 'Bermejo'
    solucion = 'Cobija'
    nodo_solucion = busqueda_BCU(conecciones, estado_inicial, solucion)
    # Mostrar resultado
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_estado())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    print("Costo: %s" % str(nodo_solucion.get_costo()))