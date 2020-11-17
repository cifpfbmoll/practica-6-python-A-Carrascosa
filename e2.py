# Escribe un programa que te pida números y los guarde en una lista. Para terminar de introducir número, 
# simplemente escribe “Salir”. El programa termina escribiendo la lista de números.
# 
# Escribe un nombre: 14
# Escribe una otro nombre: 123
# Escribe una otro nombre: -25
# Escribe una otro nombre: 123
# Escribe una otro nombre: Salir
# Los números que has escrito son [14, 123, -25, 123]

lista = []
opened = True

while opened == True:
    added = input('>>> Escribe un número:\n >  ')
    if added == 'Salir':
        opened = False
    else:
        added = int(added)
        lista.append(added)

print('\n>>> Los números que has escrito son %s\n' % (lista))