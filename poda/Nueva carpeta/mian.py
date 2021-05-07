def desplegar_tablero(tablero):
    #Con esta función se despliega la nueva configuración del tablero después de cada movimiento
    #cada elemento de la matriz se imprime con un espacio.
	# Carlos Rodríguez
    for ren in tablero:
        for col in ren:
            print(col, end=" ")
        print("")    

def revisa_molinos(jugador, renglon, columna):
    #Esta función se ejecuta después de cada movimiento de un jugador para ver 
    #si el movimiento anterior generó un molino. En caso de que sí se haya formado, regresa True
	# Carlos Rodríguez
    boolean = False
    if jugador == "b":
      ficha = "●"
    else:
      ficha = "○"

    if renglon != 3 and tablero[renglon].count(ficha) == 3:
        boolean = True
    elif [tablero[i][columna] for i in range(1,6) if columna != 3].count(ficha) == 3:
        boolean = True
  
    return boolean 

def quitar_fichas(player):
    # Cuando formes un molino, esta función se activa y te permite quitar una ficha de tu oponente
    # en una casilla que selecciones
	# Carlos Rodríguez
    renglon = int(input("¿De cuál renglón quieres quitar la ficha? (1-5): "))
    columna = int(input("¿De cuál columna quieres quitar la ficha? (1-5): "))

    if jugador == "b":
      ficha = "●"
    else:
      ficha = "○"
    
    while True:
        if renglon not in range(1,6) or columna not in range(1,6):
            print("\n¡Esa casilla no existe!\n")

        elif tablero[renglon][columna] == "|" or tablero[renglon][columna] == "-":
            print("\nPor favor, selecciona una casilla válida.\n")
        
        elif renglon == 3 and columna == 3:
            print("\n¡Ese el centro del tablero!")
            print("¡Escoge otra casilla!\n")
        
        elif tablero[renglon][columna] == "▦":
            print("\n¡Allí no hay ninguna ficha!\n")
        
        elif tablero[renglon][columna] == ficha:
            print("\n¡No puedes quitar una ficha que es tuya!\n")

        else:
            tablero[renglon][columna] = "▦" 
            break
                    
        renglon = int(input("¿De cuál renglón quieres quitar la ficha? (1-5): "))
        columna = int(input("¿De cuál columna quieres quitar la ficha? (1-5): "))
        
# Funciones Fase 1
# Carlos Rodríguez
#-----------------

def colocar_fichas(player):
  #Para colocar las 6 fichas iniciales en el tablero, esta función te permite seleccionar la casilla
  #donde quieres posicionar la ficha y la coloca 
  # Carlos Rodríguez
    renglon = int(input("¿En qué renglón quieres poner la ficha? (1-5): "))
    columna = int(input("¿En qué columna quieres poner la ficha? (1-5): "))
    
    while True:
        if renglon not in range(1,6) or columna not in range(1,6):
            print("\n¡Esa casilla no existe!\n")
  
        elif tablero[renglon][columna] != "▦":
            if tablero[renglon][columna] == "|" or tablero[renglon][columna] == "-": 
                print("\nPor favor, selecciona una casilla válida.\n")
            elif renglon == 3 and columna == 3:
              print("\n¡Ese el centro del tablero!")
              print("¡Escoge otra casilla!\n")
            else:
                print("\n¡Esa casilla ya está ocupada! Selecciona otra.\n")
        
        else:
            if player == "b":
                tablero[renglon][columna] = "●"
            elif player == "n": 
                tablero[renglon][columna] = "○"
            break
            
        renglon = int(input("¿En qué renglón quieres poner la ficha? (1-5): "))
        columna = int(input("¿En qué columna quieres poner la ficha? (1-5): "))

    #Regresa el renglón y la columna para que la función revisar_molinos pueda evaluar si se juntaron tres
    #fichas en el renglón o columna actual  
    return renglon, columna 
    
#Funciones Fase 2
#----------------

def seleccionar_ficha(player):
    #Esta función se activa cuando todas las fichas han sido posicionadas y empieza la fase 2
    #Con esta función los jugadores solo pueden mover sus fichas una casilla a la vez
	#David López
    if player == "b":
        ficha = "●"
    else:
    	ficha = "○"

    renglon = int(input("¿En qué renglón está la ficha que quieres mover? (1-5): "))
    columna = int(input("¿En qué columna está la ficha que quieres mover? (1-5): "))
    
    while True:
        if renglon not in range(1,6) or columna not in range(1,6):
            print("\n¡Esa casilla no existe!\n")
        elif tablero[renglon][columna] != ficha:
            if tablero[renglon][columna] == "|" or tablero[renglon][columna] == "-": 
                print("\nPor favor, selecciona una casilla válida.\n")
            elif tablero[renglon][columna] == "▦":
                print("\n¡Allí no hay ninguna ficha!\n")
            elif renglon == 3 and columna == 3:
                print("\n¡Ese el centro del tablero!")
                print("¡Escoge otra casilla!\n")  
            else:
                print("\n¡Esa casilla tiene una ficha de tu oponente! Selecciona otra.\n")
        else:
            break
        renglon = int(input("¿En qué renglón está la ficha que quieres mover? (1-5): "))
        columna = int(input("¿En qué renglón está la ficha que quieres mover? (1-5): "))
    
    return ficha, renglon, columna

def mover_ficha_1(ficha, renglon, columna):
    #Con esta función los jugadores solo pueden mover sus fichas una casilla a la vez
	#David López
    renglon_nuevo = int(input("¿A cuál renglon quieres mover la ficha? (1-5): "))
    columna_nueva = int(input("¿A cuál columna quieres mover la ficha? (1-5): "))

    while True:
        if tablero[renglon_nuevo][columna_nueva] != "▦":
            if tablero[renglon_nuevo][columna_nueva] == "|" or tablero[renglon_nuevo][columna_nueva] == "-": 
                print("\nPor favor, selecciona una casilla válida.\n")
            elif renglon == 3 and columna == 3:
                print("\n¡Ese el centro del tablero!")
                print("¡Escoge otra casilla!\n")
            else:
                print("\n¡Esa casilla ya está ocupada! Selecciona otra.\n")
        elif renglon != renglon_nuevo and columna != columna_nueva:
            print("\nPosición inválida: solo puedes mover la ficha una casilla.\n")
        elif renglon_nuevo == renglon and columna_nueva != columna:
            dif = columna_nueva - columna
            if renglon == 1 or renglon == 5:
                if abs(dif) == 2:
                    tablero[renglon_nuevo][columna_nueva] = ficha
                    tablero[renglon][columna] = "▦"
                    break
                else:
                    print("\nPosición inválida: solo puedes mover la ficha una casilla\n")
            else:
                if abs(dif) == 1:
                    tablero[renglon_nuevo][columna_nueva] = ficha
                    tablero[renglon][columna] = "▦"
                    break
                else:
                    print("\nPosición inválida: solo puedes mover la ficha una casilla\n")
        elif renglon_nuevo != renglon and columna_nueva == columna:
            dif = renglon_nuevo - renglon
            if columna == 1 or columna == 5:
                if abs(dif) == 2:
                    tablero[renglon_nuevo][columna_nueva] = ficha
                    tablero[renglon][columna] = "▦"
                    break
                else:
                    print("\nPosición inválida: solo puedes mover la ficha una casilla\n")
            else:
                if abs(dif) == 1:
                    tablero[renglon_nuevo][columna_nueva] = ficha
                    tablero[renglon][columna] = "▦"
                    break
                else:
                    print("\nPosición inválida: solo puedes mover la ficha una casiila\n")
        else:
            print("\nDebes mover la ficha a otra casilla\n")

        renglon_nuevo = int(input("¿A cuál renglon quieres mover la ficha? (1-5): "))
        columna_nueva = int(input("¿A cuál columna quieres mover la ficha? (1-5): "))
        
    return renglon_nuevo, columna_nueva

#Funciones Fase 2.5
#----------------

def mover_ficha_2(ficha, renglon, columna):
    #Con esta función los jugadores que tienen solo tres fichas pueden realizar el "vuelo", o bien
	#pueden mover la ficha a la casilla que deseen
	#David López

    renglon_nuevo = int(input("¿A cuál renglon quieres mover la ficha? (1-5): "))
    columna_nueva = int(input("¿A cuál columna quieres mover la ficha? (1-5): "))

    while tablero[renglon_nuevo][columna_nueva] != "▦":
        if renglon not in range(1,6) or columna not in range(1,6):
            print("\n¡Esa casilla no existe!\n")
        elif tablero[renglon_nuevo][columna_nueva] == "|" or tablero[renglon_nuevo][columna_nueva] == "-":
            print("\nPor favor, selecciona una casilla válida.\n")
        elif renglon == 3 and columna == 3:
            print("\n¡Ese el centro del tablero!")
            print("¡Escoge otra casilla!\n")
        else:
            print("\n¡Esa casilla ya está ocupada! Selecciona otra.\n")

        renglon_nuevo = int(input("¿A cuál renglon quieres mover la ficha? (1-5): "))
        columna_nueva = int(input("¿A cuál columna quieres mover la ficha? (1-5): "))

    tablero[renglon_nuevo][columna_nueva] = ficha
    tablero[renglon][columna] = "▦"
    
    return renglon_nuevo, columna_nueva
    
def tipo_de_movimiento(jugador):
	# Especifica si el jugador usará mover_ficha_ 1 o mover_ficha_2 
	# basándose en la cantidad de fichas que le quedan
	#David López

    fich,ren,col = seleccionar_ficha(jugador)
    
    renglon_nuevo = 0
    columna_nueva = 0

    if jugador == "b":
        if fichas_b > 3:
            renglon_nuevo,columna_nueva = mover_ficha_1(fich,ren,col)
        elif fichas_b == 3:
            renglon_nuevo,columna_nueva = mover_ficha_2(fich,ren,col)
    
    else:
        if fichas_n > 3:
            renglon_nuevo,columna_nueva = mover_ficha_1(fich,ren,col)
        elif fichas_n == 3:
            renglon_nuevo,columna_nueva = mover_ficha_2(fich,ren,col)
            
    return renglon_nuevo, columna_nueva
    
#-----------
# Main code
#-----------

#Creación de Tablero como array bidimensional
tablero = [[" ",1,2,3,4,5],
            [1,"▦","-","▦","-","▦"],
			[2,"|","▦","▦","▦","|"],
			[3,"▦","▦"," ","▦","▦"],
			[4,"|","▦","▦","▦","|"],
			[5,"▦","-","▦","-","▦"]]

#Número de fichas por jugador. Los dos comienzan con 6
fichas_b = 6
fichas_n = 6
print("""
  ███╗░░░███╗░█████╗░██╗░░░░░██╗███╗░░██╗░█████╗░
  ████╗░████║██╔══██╗██║░░░░░██║████╗░██║██╔══██╗
  ██╔████╔██║██║░░██║██║░░░░░██║██╔██╗██║██║░░██║
  ██║╚██╔╝██║██║░░██║██║░░░░░██║██║╚████║██║░░██║
  ██║░╚═╝░██║╚█████╔╝███████╗██║██║░╚███║╚█████╔╝
  ╚═╝░░░░░╚═╝░╚════╝░╚══════╝╚═╝╚═╝░░╚══╝░╚════╝░
  
-------------Juego de estrategia mental------------
""")
input("Presiona enter para continuar ")
print("""
---------------------------------------------------
--------------------  REGLAS  ---------------------
---------------------------------------------------
El objetivo del juego es formar filas o columnas de 
tres fichas del mismo color dentro del tablero, a lo
que se le denomina Molino.
 
- Por cada molino que se 
forme, el jugador podrá retirar cualquier ficha de 
su oponente. Los molinos pueden ser formados tanto 
en la primera como en la segunda fase. Gana el jugador 
que deje a su oponente con solo dos 
fichas. 
Cada jugador tendrá seis fichas de su respectivo
color.
- En la primera etapa los jugadores podrán posicionar 
sus fichas por turnos en cualquier casilla del 
tablero, las cuales se representan como “▦“. 
- Una vez que todas las fichas se han posicionado y
se ha completado el sexto turno, se procederá a la
fase 2; ahora las fichas solo se podrán mover una 
casilla a la vez.
El movimiento en diagonal no está permitido. 
- Cuando alguno de los jugadores tenga en el tablero 
solo tres fichas, tendrá la capacidad de mover
cualquiera de ellas a la casilla que desee. 
CÓMO INTERACTUAR CON EL JUEGO
En la interfaz se mostrará el jugador y el turno 
actual.
Introduce solamente números del 1 al 5 para 
representar a los renglones y columnas de la 
posición deseada. 
""")
# Fase 1
# ------
print("""
---------------------------------------------------
------------ ¡Bienvenidos a la Fase 1! ------------
---------------------------------------------------
""")
print("¡Coloca tus fichas en las casillas que tengan un ▦!")
turno = 1

#Switch para cambiar jugador actual
jugador = ""

while turno <= 6:
    print("---------------------------------------------------\n") 
    print(f'TURNO: {turno}/6 \n') #Despliega el turno actual
    print(f'Fichas Blancas: {fichas_b}/6 ●') #Muestra la cantidad actual de fichas blancas
    print(f'Fichas Negras: {fichas_n}/6 ○') #Muestra la cantidad actual de fichas negras
    
    jugador = "b"
    print('\nJUEGAN BLANCAS\n')
    
    desplegar_tablero(tablero)
    print()

    #Por cada turno, cada jugador puede colocar una ficha con colocar_fichas(). Esta regresa las
    #coordenadas de la nueva ficha y revisa_molinos() verifica si se formó un molino
    ren,col = colocar_fichas(jugador) 
    if revisa_molinos(jugador, ren, col) == True: #Si se forma un molino, puede quitar una ficha
        print("\n¡Felicidades, formaste un molino!")
        print("¡Ahora puedes quitarle una ficha a tu oponente!\n")
        desplegar_tablero(tablero)
        print()
        quitar_fichas(jugador) 
        fichas_n-=1
      
    jugador = "n"    
    print('\nJUEGAN NEGRAS\n')
    
    desplegar_tablero(tablero)
    print()
    
    ren,col = colocar_fichas(jugador)
    if revisa_molinos(jugador, ren, col) == True:
        print("\n¡Felicidades, formaste un molino!")
        print("¡Ahora puedes quitarle una ficha a tu oponente!\n")
        desplegar_tablero(tablero)
        print()
        quitar_fichas(jugador)
        fichas_b-=1
  
    turno+=1

# Fase 2
# ------
print("""
---------------------------------------------------
------------ ¡Bienvenidos a la Fase 2! ------------
---------------------------------------------------
""")
print(" ¡Mueve tus fichas para seguir formando molinos!\n")
print("                ¡Recuerda!\n")
print("- Más de 3 fichas, solo te puedes mover una casilla")
print("- Si tienes 3 fichas, ¡te puedes mover donde sea!")
print("- Pierde el primero que se quede con menos de 3.")

ganador = ""

while True:
    print("---------------------------------------------------\n")
    print(f'Fichas Blancas: {fichas_b}/6 ●') 
    print(f'Fichas Negras: {fichas_n}/6 ○') 
  
    jugador = "b"
    print('\nJUEGAN BLANCAS\n')
    
    desplegar_tablero(tablero)
    print()

    
    ren_n, col_n = tipo_de_movimiento(jugador)
    if revisa_molinos(jugador, ren_n, col_n) == True:
        print("\n¡Felicidades, formaste un molino!")
        print("¡Ahora puedes quitarle una ficha a tu oponente!\n")
        desplegar_tablero(tablero)
        print()
        quitar_fichas(jugador)
        fichas_n-=1
        if fichas_n < 3:
            ganador = "BLANCAS"
            break
      
    jugador = "n"    
    print('\nJUEGAN NEGRAS\n')
    
    desplegar_tablero(tablero)
    print()
    
    ren_n,col_n = tipo_de_movimiento(jugador)
    if revisa_molinos(jugador, ren_n, col_n) == True:
        print("\n¡Felicidades, formaste un molino!")
        print("¡Ahora puedes quitarle una ficha a tu oponente!\n")
        desplegar_tablero(tablero)
        print()
        quitar_fichas(jugador)
        fichas_b-=1
        if fichas_b < 3:
            ganador = "NEGRAS"
            break

if ganador == "BLANCAS":
	print("""
	██████╗░██╗░░░░░░█████╗░███╗░░██╗░█████╗░░█████╗░░██████╗
	██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔════╝
	██████╦╝██║░░░░░███████║██╔██╗██║██║░░╚═╝███████║╚█████╗░
	██╔══██╗██║░░░░░██╔══██║██║╚████║██║░░██╗██╔══██║░╚═══██╗
	██████╦╝███████╗██║░░██║██║░╚███║╚█████╔╝██║░░██║██████╔╝
	╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝╚═════╝░
	░██████╗░░█████╗░███╗░░██╗░█████╗░███╗░░██╗██╗
	██╔════╝░██╔══██╗████╗░██║██╔══██╗████╗░██║██║
	██║░░██╗░███████║██╔██╗██║███████║██╔██╗██║██║
	██║░░╚██╗██╔══██║██║╚████║██╔══██║██║╚████║╚═╝
	╚██████╔╝██║░░██║██║░╚███║██║░░██║██║░╚███║██╗
	░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝
""")
else:
	print("""
	███╗░░██╗███████╗░██████╗░██████╗░░█████╗░░██████╗
	████╗░██║██╔════╝██╔════╝░██╔══██╗██╔══██╗██╔════╝
	██╔██╗██║█████╗░░██║░░██╗░██████╔╝███████║╚█████╗░
	██║╚████║██╔══╝░░██║░░╚██╗██╔══██╗██╔══██║░╚═══██╗
	██║░╚███║███████╗╚██████╔╝██║░░██║██║░░██║██████╔╝
	╚═╝░░╚══╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░
	░██████╗░░█████╗░███╗░░██╗░█████╗░███╗░░██╗██╗
	██╔════╝░██╔══██╗████╗░██║██╔══██╗████╗░██║██║
	██║░░██╗░███████║██╔██╗██║███████║██╔██╗██║██║
	██║░░╚██╗██╔══██║██║╚████║██╔══██║██║╚████║╚═╝
	╚██████╔╝██║░░██║██║░╚███║██║░░██║██║░╚███║██╗
	░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝
""")