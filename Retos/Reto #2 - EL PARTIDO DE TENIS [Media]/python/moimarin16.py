'''/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */'''
#Lista de puntuaciones disponibles
#Posiciones: [0,1,2,3]
punt = ['Love','15','30','40']
#Tener en cuenta Deuce y  Ventaja
status = ['Inicio','Deuce','Ventaja P1','Ventaja P2','Final']

#Inicializar puntuación, el que llegue a 6 ganaría, ya que de 0 a 5 corresponde a cada puntuación de la lista anterior
p1_punt = 0
p2_punt = 0
estado = status[0]

while(estado != status[4]): #Mientras estado sea distinto de Final
    marca = input('¿Quién ha  marcado?\n')
    if marca != 'P1' and marca != 'P2':
        print('Introduce un jugador correcto.')
    else:
        #Estado Inicio, siempre que ambos jugadores estén por debajo de 40
        if estado == status[0]:
            if(marca == 'P1'): 
                p1_punt = p1_punt + 1
            elif(marca == 'P2'): 
                p2_punt = p2_punt + 1
            
            if (p1_punt == 3 and p2_punt == 3):#Cambiar a estado Deuce
                estado = status[1]
                print('Deuce')
                continue
            elif (p1_punt == 4 and p2_punt == 3):
                estado = status[2]
                print('Ventaja P1')
                continue
            elif (p2_punt == 4 and p1_punt == 3):
                estado = status[3]
                print('Ventaja P2')
                continue
            elif (p1_punt == 4 and p2_punt < 3):
                estado = status[4]
                print('Ha ganado el P1')
                break
            elif (p2_punt == 4 and p1_punt < 3):
                estado = status[4]
                print('Ha ganado el P2')
                break
            else:
                print(punt[p1_punt],' - ',punt[p2_punt])
        #Deuce
        if estado == status[1]: 
            if(marca == 'P1'): 
                p1_punt = p1_punt + 1
                estado = status[2]
                print('Ventaja P1')
                continue
            elif(marca == 'P2'): 
                p2_punt = p2_punt + 1
                estado = status[3]
                print('Ventaja P2')
                continue
                

        #Ventaja P1
        if estado == status[2]:
            if(marca == 'P1'): 
                estado = status[4]
                print('Ha ganado el P1')
                break
            else: 
                p1_punt = p1_punt - 1
                estado = status[1]
                print('Deuce')
                continue

        #Ventaja P2
        if estado == status[3]:
            if(marca == 'P2'): 
                estado = status[4]
                print('Ha ganado el P2')
                break
            else: 
                p2_punt = p2_punt - 1
                estado = status[1]
                print('Deuce')
                continue
