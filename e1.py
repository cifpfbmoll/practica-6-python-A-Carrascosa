# Escribe un programa que te pida palabras y las guarde en una lista. Para terminar de introducir palabras,
# simplemente pulsa Enter. El programa termina escribiendo la lista de palabras.
# 
# Escribe una palabra: viaje
# Escribe más palabras: aventura
# Escribe más palabras: cómic
# Escribe más palabras:
# Las palabras que has Escrito son [ 'viaje', 'aventura', 'cómic']

lista = []
opened = True

while opened == True:
    added = input('>>> Escribe una palabra:\n >  ')
    if added == '':
        opened = False
    else:
        lista.append(added)

print('>>> Las palabras que has escrito son: %s' % (lista))