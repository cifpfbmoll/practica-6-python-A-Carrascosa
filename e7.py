# Escribe un programa que pida un número (límite) y luego te pida números hasta que la suma 
# de los números introducidos supere el límite inicial. El programa termina escribiendo la lista de números.
# 
# Escribe límite: 50
# Escribe un valor: 10
# Escribe otro valor: 25
# Escribe otro valor: 7
# Escribe otro valor: 14
# El límite a superar es 50. La lista creada es 10, 25, 7, 14 ya que la suma de estos números es: 56

num_end = int(input('>>> Escribe un número límite:\n >  '))
num_suma = int(0)
lista = []

while num_suma < num_end:
    num = int(input('>>> Escribe un número:\n >  '))
    if num_suma < num_end:
        lista.append(num)
        num_suma = num_suma + num

lista_view = str(lista)[1:-1]
print('\n>>> El límite a superar es %d. La lista creada es %s ya que la suma de estos números es: %d\n' % ( num_end, lista_view, num_suma))