from math import inf as infinity
import random
import platform
import time
from os import system

def inputPlayerLetter():
	# El jugador elige con que letra quiere jugar "X" u "O"
	# Devuelve una lista con una letra del juegador y una letra del computador
	letter = ''
	while not(letter == 'X' or letter == 'O'):
		print('Elija si quiere jugar con X u O?')
		letter = input().upper()
		if(letter != 'X' and letter != 'O'):
			print("Eligio una letra que sea correcta!")

	# El primer elemento en la lista es el jugador y el segundo es el computador
	if letter == 'X':
		return ['X','O']
	else:
		return ['O','X']

def whoGoesFirts():
	#Se elige aleatoriamente quien va primero humano o computador
	juega=random.randint(0, 1)
	print(juega)
	if juega == 0:
		return 'computador'
	else:
		return 'jugador'

def drawBoard(board):
	#Esta funcion imprime el tablero
	#Un cuadro representado por una lista de 9 strings
    copyBoard = getBoardCopy(board)

    for i in range(1,25):
        if(board[i] == ''):
            copyBoard[i] = str(i)
        else:
            copyBoard[i] = board[i]
    print(copyBoard[1] + '| ------- |' + copyBoard[2] + '| -------- |' + copyBoard[3])
    print('| |'+copyBoard[4]+'| ---- |'+ copyBoard[5] +'| ----- |'+ copyBoard[6]+'| |')
    print('|'+'| ---  '+copyBoard[7]+' -- '+copyBoard[8]+' -- '+copyBoard[9])
    print(copyBoard[10]+'|'+ copyBoard[11] +'||' + copyBoard[12]+'|  ▦   |'+copyBoard[13]+'| |'+copyBoard[14]+'|'+copyBoard[15])
    print('|'+' | - |'+copyBoard[16]+'|-|'+copyBoard[17]+'|-|'+copyBoard[18])
    print('| |'+copyBoard[19]+'| --- |'+ copyBoard[20] +'| --- |'+ copyBoard[21]+'|')
    print(copyBoard[22] + '| ------ |' + copyBoard[23] + '| ------  |' + copyBoard[24])

def getBoardCopy(board):
	# Hace una copia del tablero y la retorna
	copiaBoard = []
	for i in board:
		copiaBoard.append(i)
	return copiaBoard

def getPlayerMove(board):
	# Recibe el movimiento del jugador
	move = ''
	# ve si hay espacions libres y si el movimiento es permitido
	while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24'.split() or not isSpaceFree(board, int(move)):
		print('Cual es su proximo movimiento? (1-24)')
		move = input()
		#en caso de que este en el rango
		if(move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20  21 22 23 24'):
			print("MOVIMENTO INVALIDO!, EL MOVIMIENTO DEBE SER UN VALOR ENTRE 1 Y 24!")
		# si es permitido
		if(move in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20  21 22 23 24'):
			#si no hay espacios disponibles 
			if(not isSpaceFree(board, int(move))):
				print("ESPACO NO DISPONIBLE! ELIJA OTRO ESPACIO ENTRE 1 Y 24 DE LOS ESPACIOS DISPONIBLES!")
	return int(move)

def isSpaceFree(board, move):
	#Retorna True si un espacio solicitado esta libre en el tablero
	if(board[move] == ''):
		return True
	else:
		return False

def makeMove(board, letter, move):
	# registra la jugada de un jugador sobre el tablero
	board[move] = letter



def isWinner(board, letter):
	#Dado un cuadro y una letterra, esta funcion retorn True si la letterra pasada vence el juego
	return((board[1] == letter and board[2] == letter and board[3] == letter) or #linha de cima
		(board[4] == letter and board[5] == letter and board[6] == letter) or #linha do meio
		(board[7] == letter and board[8] == letter and board[9] == letter) or #linha de baixo
        (board[10] == letter and board[11] == letter and board[12] == letter) or #columnauna da esquerda
		(board[13] == letter and board[14] == letter and board[15] == letter) or #columnauna do meio
		(board[16] == letter and board[17] == letter and board[18] == letter) or #columnauna da direito
		(board[19] == letter and board[20] == letter and board[21] == letter) or #diagonal principal
		(board[22] == letter and board[23] == letter and board[24] == letter)or
        
        (board[1] == letter and board[9] == letter and board[22] == letter) or #diagonal principal
		(board[4] == letter and board[11] == letter and board[14] == letter)or
        (board[7] == letter and board[12] == letter and board[16] == letter) or #diagonal principal
		(board[2] == letter and board[5] == letter and board[8] == letter)or
        (board[17] == letter and board[20] == letter and board[23] == letter) or #diagonal principal
		(board[9] == letter and board[13] == letter and board[18] == letter)or
        (board[6] == letter and board[14] == letter and board[21] == letter) or #diagonal principal
		(board[3] == letter and board[15] == letter and board[24] == letter)or
        (board[1] == letter and board[4] == letter and board[7] == letter) or #diagonal principal
		(board[3] == letter and board[6] == letter and board[9] == letter)or
        (board[22] == letter and board[19] == letter and board[16] == letter) or #diagonal principal
		(board[18] == letter and board[21] == letter and board[24] == letter)) #diagonal secundaria

def getComputerMove(board, turn, computerLetter):
	#Definimos aqui qual sera o movimento do computador
	a = -2
	opcoes = []
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	#if len(possiveisOpcoes(board)) == 9:
	#	return 5

	#Comecamos aqui o MiniMax
	#Primeiro chechamos se podemos ganhar no proximo movimento
	for i in range(1, 25):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, computerLetter, i)
			if isWinner(copy, computerLetter):
				return i

	#Checa se o jogador pode vencer no proximo movimento e bloqueia
	for i in range(1, 25):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, playerLetter, i)
			if isWinner(copy, playerLetter):
				return i

	possiveisOpcoesOn = espaciosDisponibles(board)

	for move in possiveisOpcoesOn:
		makeMove(board, computerLetter, move)
		val = alphabeta(board, computerLetter, playerLetter, -2, 2)		
		makeMove(board, '', move)
		if val > a:
			a = val
			opcoes = [move]
		elif val == a:
			opcoes.append(move)
	return random.choice(opcoes)


"""def chooseRandomMoveFromList(board, movesList):
	#Retorna un movimento valido aleatorio
	#Retorna None si no existen movimentos validos posibles

	posiblesMovimentos = []
	for i in movesList:
		if isSpaceFree(board, i):
			posiblesMovimentos.append(i)

	if len(posiblesMovimentos) != 0:
		return random.choice(posiblesMovimentos)
	else:
		return None"""

def isBoardFull(board):
	#Retorna True si no existen espacios disponibles en el tablero
	for i in range(1, 25):
		if isSpaceFree(board, i):
			return False
	return True

def espaciosDisponibles(board):
	#Retorna una lista de todos los espacion disponibles en el tablero

	espacios = []

	for i in range(1, 10):
		if isSpaceFree(board, i):
			espacios.append(i)

	return espacios

def finishGame(board, computerLetter):
	#Verifica si el juego a llegado a su final
	#Retorna -1 si gana el jugador
	#Retorna 1 si gana el computador
	#Retorna 0 si el juego termina empatado
	#Retorna None si el juego no ha terminado

    #ve con que skin esta la pc
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	if(isWinner(board, computerLetter)):
		return 1
	elif(isWinner(board, playerLetter)):
		return -1
	elif(isBoardFull(board)):
		return 0
	else:
		return None

def alphabeta(board, computerLetter, turn, alpha, beta):
	#Fazemos aqui a poda alphabeta

    #decide cual sera el skin de la pc
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'
    #ve de quien es el turno, para darle paso a jugar al otro jugador
	if turn == computerLetter:
		nextTurn = playerLetter
	else:
		nextTurn = computerLetter

	finish = finishGame(board, computerLetter)
    # retorna de -1,0,1 o None para ver si gano alguien
    #verifica si el juega termino 
	if (finish != None):
		return finish
	espacios = espaciosDisponibles(board)
    #recoje los espacios disponibles

    #si le toca a la pc
	if turn == computerLetter:
		for move in espacios:
            #para moverse en los espacions disponibles
			makeMove(board, turn, move)#registra la movida en la lista
			val = alphabeta(board, computerLetter, nextTurn, alpha, beta)#llamada recursiva
			"""print("{} , {}: ".format(alpha, beta))
			print("val: {}".format(val))"""
			makeMove(board, '', move)#para que pinte los numeros
			if val > alpha:
				alpha = val
			if alpha >= beta:
				return alpha
        #print("beta {}".format(alpha))
		return alpha
    #si le toca al humano
	else:
		for move in espacios:
			makeMove(board, turn, move)
			val = alphabeta(board, computerLetter, nextTurn, alpha, beta)
			makeMove(board, '', move)
			if val < beta:
				beta = val
			if alpha >= beta:
				return beta
        #print("beta {}".format(beta))
		return beta


print('Vamos jogar jogo da velha!')
jogar = True


while jogar:
	#Reseta o jogo
    theBoard = ['']*25

    playerLetter, computerLetter = inputPlayerLetter()#asigna skins
    turn = whoGoesFirts()
    print( turn + ' juega primero')
    gameisPlaying = True

    while gameisPlaying:
        if turn == 'jogador':
            #Vez do Jogador
            drawBoard(theBoard)
            #dibuja e tablero
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Woooow! Voce venceu o jogo!')
                gameisPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('O jogo terminou empatado')
                    break
                else:
                    turn = 'computador'
        else:
            #Vez do computador
            move = getComputerMove(theBoard, playerLetter, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("O computador venceu :(")
                gameisPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('O jogo terminou empatado')
                    break
                else:
                    turn = 'jogador'

    letterNew = ''
    while not(letterNew == 'S' or letterNew == 'N'):
        print("Voce quer jogar novamente? Digite S(para sim) ou N(para nao)")
        letterNew = input().upper()
        if (letterNew != 'S' and letterNew != 'N'):
            print("Entrada invalida! Digite S(para sim) ou N(para nao)!")
        if(letterNew == 'N'):
            print("Foi bom jogar com voce! Ate mais!")
            jogar = False
