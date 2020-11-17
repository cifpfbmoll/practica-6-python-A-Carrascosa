# Escribe un programa que te pida números cada vez más grandes y que se guarden en una lista. 
# Para acabar de escribir los números, escribe un número que no sea mayor que el anterior. 
# El programa termina escribiendo la lista de números:
# 
# Escribe un número: 6
# Escribe un número mayor que 6: 10
# Escribe un número mayor que 10: 12
# Escribe un número mayor que 12: 25
# Escribe un número mayor que 25: 9
# Los números que has escrito son: 6, 10, 12, 25 

# (Comentario si os fijáis ya no se imprime la lista tal cual, hay que imprimir uno por uno los valores de la lista, 
# haced esto así a partir de ahora)

num_start = int(input('>>> Escribe un número:\n >  '))
num = int(num_start)
lista = []
lista.append(num_start)

while num >= num_start:
    num = int(input('>>> Escribe un número mayor que %d:\n >  ' % (num)))
    if num > num_start:
        lista.append(num)

lista_view = str(lista)[1:-1]
print('\n>>> Los números que has escrito son %s\n' % (lista_view))