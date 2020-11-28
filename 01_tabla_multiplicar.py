#Script que calcula la tabla de multiplicar de un numero


#Solicitar numero al usuario por consola
numero = int(input('¿Que numero quieres multiplicar? '))


introduccion = f'A continuacion se muestra la tabla de multiplicar del número {numero}'
print(introduccion) 

for n in range(10):
    indice = n + 1 
    resultado = numero * indice 
    resultado_impreso = f'{numero} * {indice} = {resultado}'
    print(resultado_impreso)

