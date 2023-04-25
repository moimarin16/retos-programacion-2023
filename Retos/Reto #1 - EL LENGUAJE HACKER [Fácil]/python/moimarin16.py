'''
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
 '''
 
t = input('Introduce un texto:')
t_mod = ""
for i in t:
    if i == 'a' or i == 'A':
        t_mod = t_mod + '4'
    elif i == 'b' or i == 'B':
        t_mod = t_mod + 'I3'
    elif i == 'c' or i == 'C':
        t_mod = t_mod + '['
    elif i == 'd' or i == 'D':
        t_mod = t_mod + ')'
    elif i == 'e' or i == 'E':
        t_mod = t_mod + '3'
    elif i == 'f' or i == 'F':
        t_mod = t_mod + '|='
    elif i == 'g' or i == 'G':
        t_mod = t_mod + '&'
    elif i == 'h' or i == 'H':
        t_mod = t_mod + '#'
    elif i == 'i' or i == 'I':
        t_mod = t_mod + '1'
    elif i == 'j' or i == 'J':
        t_mod = t_mod + ',_|'
    elif i == 'k' or i == 'K':
        t_mod = t_mod + '>|'
    elif i == 'l' or i == 'L':
        t_mod = t_mod + '1'
    elif i == 'm' or i == 'M':
        t_mod = t_mod + '/\\/\\'
    elif i == 'n' or i == 'N':
        t_mod = t_mod + '^/'
    elif i == 'o' or i == 'O':
        t_mod = t_mod + '0'
    elif i == 'p' or i == 'P':
        t_mod = t_mod + '|*'
    elif i == 'q' or i == 'Q':
        t_mod = t_mod + '(_,)'
    elif i == 'r' or i == 'R':
        t_mod = t_mod + 'I2'
    elif i == 's' or i == 'S':
        t_mod = t_mod + '5'
    elif i == 't' or i == 'T':
        t_mod = t_mod + '7'
    elif i == 'u' or i == 'U':
        t_mod = t_mod + '(_)'
    elif i == 'v' or i == 'V':
        t_mod = t_mod + '\\/'
    elif i == 'w' or i == 'W':
        t_mod = t_mod + '\\/\\/'
    elif i == 'x' or i == 'X':
        t_mod = t_mod + '><'
    elif i == 'y' or i == 'Y':
        t_mod = t_mod + 'j'
    elif i == 'z' or i == 'Z':
        t_mod = t_mod + '2'
    elif i == ' ': 
        t_mod = t_mod + ' '
    
print("El texto hacker es: ",t_mod)