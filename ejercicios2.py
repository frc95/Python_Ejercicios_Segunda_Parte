# multiplicar dos números sin usar el símbolo de multiplicación

numeroUno = 5
numeroDos = 5
resultado = 0

for num in range(numeroDos):
    resultado += numeroUno

#print(resultado)

# ingresar nombre y apellido e imprimirlo al reves

nombre = 'carlos'
apellido = 'perez'

concatenacion = nombre + ' ' + apellido

#print(concatenacion[::-1])

# escribir una función que encuentre el elemento menor de una lista
lista = [4,11,8,21,22,3,8,623,10]
menor = 'init'

for num in lista:
    if menor == 'init':
        menor = num
    if num < menor:
        menor = num

#print(menor)

# escribir una función que devuelva el volumen de una esfera por su radio
# 4/3 * pi * r ** 3

def volumen(radio):
    resultado = (4/3) * 3.14 * radio ** 3 # con ** usamos el exponente
    return resultado

#print(volumen(6))

# escribir una función que indique si el usuario es mayor de edad

def ingreseSuEdad(usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self,edad):
        self.edad = edad

usuario = Usuario(25)

if ingreseSuEdad(usuario):
    print('Es mayor')
else:
    print('Es menor')

# escribir una función que indique si un número es par o impar

def esPar(numero):
    return numero % 2 == 0

if esPar(63):
    print('Es par')
else:
    print('Es impar')

# escribir una función que indique cuantas vocales tiene una palabra

def contarVocales(palabra):
    vocales = ['a', 'e', 'i', 'o', 'u']
    contador = 0

    for c in palabra:
        x = c.lower()
        for v in vocales:
            if x == v:
                contador+=1
                break

    return contador

#print('La cantidad de vocales son:', contarVocales('Alejandra'))

# escribir una aplicación que reciba una cantidad infinita de números hasta
# decir basta, luego que devuelva la suma de los números ingresados

# lista = []
# resultado = 0
# print('Ingrese numeros hasta escribir "basta"')

# while True:
#     valor = input('Ingrese un valor:')
#     if valor == 'basta':
#         break
#     else:
#         try:
#             numero = int(valor)
#             lista.append(numero)
#         except:
#             print('Dato invalido')
#             exit()

# for num in lista:
#     resultado += num

# print('El resultado es', resultado)

# escribir una función que reciba nombre y apellido y los vaya agregando a
# un archivo

def guardar(nombre, apellido):
    file = open('archivo.txt', 'a')
    file.write(nombre + ' ' + apellido + '\n')
    file.close()

guardar('juan', 'godoy')