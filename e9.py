# Escribe un programa que te pida nombres de personas y sus números de teléfono. 
# Para terminar debe pulsar “S” cuando te pida el nombre. El programa termina escribiendo nombres y números de teléfono. 
# Nota: La lista en la que se guardan los nombres y números de teléfono tiene esta
# estructura[[nombre1, telef1], [nombre2, telef2], [nom3, telef3], etc], es decir, lista de listas.
# 
# Dame un nombre: Pepe González
# Dame el teléfono: 971971971
# Dame un nombre: Macarena Gómez
# Dame el teléfono: 971999999
# Dame un nombre: Pascual Ribot
# Dame el teléfono: 666555444
# Dame un nombre: S
# Los nombres y teléfonos de la agenda son:
# Pepe González: 971971971
# Macarena Gómez: 971999999
# Pasqual Ribot: 666555444

lista = []
adding = True

print('\n>>> Estas empezando a añadir contactos, para parar el proceso escribe "S":\n')

while adding == True:
    add_name = str(input('>>> Escribe un nombre:\n >  '))
    if add_name != 'S' and add_name != 's':
        add_numb = int(input('>>> Escribe el número de %s:\n >  ' % (add_name)))
        lista.append([add_name,add_numb])
    else:
        adding = False
# print(lista)

print('\n>>>>>>>>>>>>> AGENDA <<<<<<<<<<<<<')
for i in lista:
    print('%s: %d' % (str(i[0]),i[1]))
print('>>>>>>>>>>> FIN AGENDA <<<<<<<<<<<')