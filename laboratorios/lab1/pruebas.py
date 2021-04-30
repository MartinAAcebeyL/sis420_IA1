a = [[' ', ' ', 'O', ' '], 
    ['A', 'O', ' ', ' '], 
    [' ', ' ', ' ', 'O'],
    ['O', ' ', ' ', ' ']]

actual_posicion_fila= -1
actual_posicion_celda=-1

for idx_fila_actual, fila_actual in enumerate(a):
    for idx_celda_actual, celda_actual in enumerate(fila_actual):
        if celda_actual == 'A':
            actual_posicion_fila = idx_fila_actual
            actual_posicion_celda = idx_celda_actual
            break
    if actual_posicion_fila > -1:
        break
print("{} {}".format(actual_posicion_celda, actual_posicion_fila))