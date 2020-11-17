# Escribir un programa para jugar a adivinar un número (el ordenador "piensa" el número y el usuario lo ha 
# de adivinar). El programa empieza pidiendo entre qué números está el número a adivinar, se "inventa" un 
# número al azar y luego el usuario va probando valores. El programa va decidiendo si son demasiado 
# grandes o pequeños. pista:
# 
#           import random
#           import time
# 
#           minimo = int (input ( "Valor mínimo:"))
#           max = int (input ( "Valor máximo:"))
#           secreto = random.randint (mínimo, máximo)
# 
# Valor mínimo: 0
# Valor máximo: 100
# A ver si adivinas un número entero entre 0 y 100.
# Escribe un número: 20
# Demasiado pequeño! Volver a probar: 30
# Demasiado grande! Volver a probar: 27
# Correcto! Lo has intentado 3 veces.

import random
import time

print('\n>>> Escribe dos números para después adivinar uno aleatorio.\n')

num_1 = int(input('>>> Escribe un número mínimo:\n >  '))
num_2 = int(input('>>> Escribe un número máximo:\n >  '))
num_random = int(random.randint(num_1, num_2))
# print(num_random)

num_respuesta = int(input('>>> Intenta adivinar el número:\n >  '))

while num_respuesta != num_random:
    if num_respuesta > num_random:
        num_respuesta = int(input('\n>>> Este número es muy grande! Escribe otro mas pequeño:\n >  '))
    else:
        num_respuesta = int(input('\n>>> Este número es muy pequeño! Escribe otro mas grande:\n >  '))

if num_respuesta == num_random:
    print('\n>>> El número aleatorio era %d, lo has acertado!\n' % (num_random))