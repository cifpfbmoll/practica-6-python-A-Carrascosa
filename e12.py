# Escribir un programa para jugar a adivinar un número (el usuario piensa un número y el 
# programa lo ha de adivinar). El programa empieza pidiendo entre qué números está el número 
# a adivinar y luego intenta adivinar de qué número se trata. El usuario va diciendo si el 
# número que ha dicho el programa es menor, mayor o igual al que se ha buscado.
# 
# Valor mínimo: 0
# Valor máximo: 100
# Piensa un número entre 0 y 100 a ver si lo puedo adivinar.
# Es 50 ?: mayor
# Es 75 ?: menor
# Es 62 ?: menor
# Es 56 ?: mayor
# Es 59 ?: igual
# Gracias por jugar!!
# 
# Mejoras (opcionales):
#     • Que al principio el programa se asegure de que el valor máximo es superior al valor mínimo.
#     • Que el programa detecte "trampas", por ejemplo, si cuando dices "25" le decimos "mayor" 
#       y al decir "26" le decimos "menor", el programa debe decir que estamos haciendo trampas y 
#       debe dejar de jugar con nosotros.


import random
import time

print('\n>>> Escribe dos números para después adivinar uno aleatorio.\n')

num_1 = int(input('>>> Escribe un número mínimo:\n >  '))
num_2 = int(input('>>> Escribe un número máximo:\n >  '))
num_random = int(random.randint(num_1, num_2))
respuesta = str()
# print(num_random)

while num_2 <= num_1: # Comprobacion de limites
    print('\n ⚠  El número máximo es inferior o igual que el número mínimo.\n')
    num_2 = int(input('>>> Escribe otro número máximo:\n >  '))

while respuesta != 'igual':
    respuesta = str(input('>>> El número es %d?: Escribe si el numero mostrado es [mayor, menor, igual]\n >  ' % (num_random)))
    if num_random <= num_1 or num_random >= num_2: # Detector de trampas
        print('\n ⚠  Estas intentando hacer trampas piltrafilla.\n')
        num_random = int(random.randint(num_1, num_2))
    else:
        if respuesta == 'mayor':
            num_2 = num_random
            num_random = int(random.randint(num_1, num_2-1))
        elif respuesta == 'menor':
            num_1 = num_random
            num_random = int(random.randint(num_1+1, num_2))

if respuesta == 'igual':
    print('\n>>> El número aleatorio era %d y ha sido adivinado!\n' % (num_random))