# Escribe un programa que pida notas y los guarde en una lista. Para terminar de introducir notas, 
# escribe una nota que no esté entre 0 y 10. El programa termina escribiendo la lista de notas.
# 
# Escribe una nota: 7.5
# Escribe una nota: 0
# Escribe una nota: 10
# Escribe una nota: -1
# Las notas que has Escrito son [7.5, 0.0, 10.0]

lista = []
opened = True

while opened == True:
    added = int(input('>>> Escribe un número:\n >  '))
    lista.append(added)
    if added < 0 or added > 10:
        opened = False
        lista.remove(added)

print('\n>>> Los números que has escrito son %s\n' % (lista))