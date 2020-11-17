# Escribe un programa que te pida dos números, de manera que el segundo sea mayor que el primero. 
# El programa termina escribiendo los dos números tal y como se pide:
# 
# Escribe un número: 6
# Escribe un número mayor que 6: 6
# 6 no es mayor que 6. Vuelve a introducir un número: 1
# 1 no es mayor que 6. Vuelve a introducir un número: 8
# Los números que has escrito son 6 y 8

num1 = int(input('>>> Escribe un número:\n >  '))
num2 = int(input('>>> Escribe un número mayor que %d:\n >  ' % (num1)))

while num1 > num2:
    num2 = int(input('\n ⚠  %d es menor que %d\n>>> Escribe un número mayor que %d:\n >  ' % (num2, num1, num1)))

print('\n>>> Los números que has escrito son %d y %d\n' % (num1, num2))