# Escribe un programa que pida primero dos números (máximo y mínimo) y que después te pida números intermedios. 
# Para terminar de escribir números, escribe un número que no esté comprendido entre los dos valores iniciales. 
# El programa termina escribiendo la lista de números.
# 
# Escribe un número: 6
# Escribe un número mayor que 6: 4
# 4 no es mayor que 6. Vuelve a probar: 50
# Escribe un número entre 6 y 50: 45
# Escribe otro número entre 6 y 50: 13
# Escribe otro número entre 6 y 50: 4
# Los números situados entre 6 y 50 que has escrito son: 45, 13

num_start = int(input('>>> Escribe un número:\n >  '))
num_end = int(input('>>> Escribe otro número:\n >  '))
num = int(num_start+1)
lista = []

while num > num_start and num < num_end:
    num = int(input('>>> Escribe un número entre %d y %d:\n >  ' % (num_start, num_end)))
    if num > num_start and num < num_end:
        lista.append(num)

lista_view = str(lista)[1:-1]
print('\n>>> Los números que has escrito entre %d y %d son: %s.\n' % (num_start, num_end, lista_view))