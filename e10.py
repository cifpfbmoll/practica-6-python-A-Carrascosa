# Escribe un programa que te pida los nombres y notas de alumnos. Si escribes una nota fuera del intervalo 
# de 0 a 10, el programa entenderá que no quieres introducir más notas de este alumno. Si no escribes el 
# nombre, el programa entenderá que no quieres introducir más alumnos. Nota: La lista en la que se guardan 
# los nombres y notas tiene esta estructura [[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc], 
# [nom3, nota1, nota2, etc], etc]
# 
# Dame un nombre: Héctor Quiroga
# Escribe una nota: 4
# Escribe otra nota: 8.5
# Escribe otra nota: 12
# Dame otro nombre: Inés Valls
# Escribe una nota: 7.5
# Escribe otra nota: 1
# Escribe otra nota: 2
# Escribe otra nota: -5
# Dame otro nombre:
# Las notas de los alumnos son:
# Héctor Quiroga: 4.0 - 8.5
# Inés Valls: 7.5 - 1.0 - 2.0

lista = []
adding = True

print('\n>>> Estas empezando a añadir contactos, para parar el proceso escribe "S":\n')

while adding == True:
    add_name = str(input('>>> Escribe un alumno:\n >  '))
    add_note = float(0.0)
    if add_name != '':
        lista.append([add_name])
        while add_note <= 10 and add_note >= 0:
            add_note = float(input('>>> Escribe la nota de %s:\n >  ' % (add_name)))
            if add_note <= 10 and add_note >= 0:
                lista[-1] += [add_note]
    else:
        adding = False
#print(lista)

print('\n>>>>>>>>>>>>> Alumnos y notas <<<<<<<<<<<<<')
for i in lista:
    print('Las notas de %s son:' % (str(i[0])))
    for j in i:
        if j != i[0] and j != i[-1]:
            print("%s" % (float(j)), end=" - ")
        elif j == i[-1]:
            print("%s" % (float(j)), end="")
    print('\n')
print('>>>>>>>>>>>>>>>>>>> FIN <<<<<<<<<<<<<<<<<<<')