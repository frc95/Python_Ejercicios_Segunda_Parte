#dato = input('Ingrese dato: ')

#lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']

#if lista.count(dato) > 0:
    #print('El dato existe', dato)
#else:
    #print('El dato no existe :(', dato)

#calculadora

primero = input('Ingrese el primer numero: ')
try:
    primero = int(primero)
except:
    primero = 'chanchito feliz'

if primero == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

segundo = input('Ingrese el segundo numero: ')
try:
    segundo = int(segundo)
except:
    segundo = 'chanchito feliz'

if segundo == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

simbolo = input('Ingrese operacion: ')
if simbolo == '+':
    print('Suma: ',primero+segundo)
elif simbolo == '-':
    print('Resta: ',primero-segundo)
elif simbolo == '*':
    print('Multiplicacion: ',primero*segundo)
elif simbolo == '/':
    print('Division: ',primero/segundo)
else:
    print('El simbolo ingresado no es valido')



