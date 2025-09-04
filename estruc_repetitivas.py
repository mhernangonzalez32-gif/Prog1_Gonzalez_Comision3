import random


'''1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.'''

for i in range(0,101):
    print(i)


'''2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.'''

contador = 0
iter = int(input("Ingrese un numero: "))
while iter > 0:
    contador += 1
    iter = iter //10
    
print(f"El numero tiene: {contador} digitos.")


'''3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.'''

numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese otro numero: "))
suma = 0
memoria = 0
if numero_1 == numero_2:
    print("Los numero son iguales")
else:
    if numero_1 > numero_2:
        memoria = numero_1
        numero_1 = numero_2
        numero_2 = memoria
        
while (numero_1 + 1) <= (numero_2 - 1):
    numero_1 += 1
    suma += numero_1
            
print(f"la suma de sus numeros intermedios es: {suma}")

'''4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.'''

suma = 0
while True: 
    numeros = int(input("Ingrese un numero para sumarlo: "))
    if numeros == 0:
        break
    suma = suma + numeros


print(f"La suma es: {suma}")
    

'''5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.'''

import random

numero_random = random.randint(0,9)
print(numero_random)
contador = 0
while True:
    numero_usuario = int(input("Ingrese un numero para adiviar entre el 0 y 9: "))
    if numero_usuario == numero_random:
        print(f"Adivinaste el numero, era el {numero_random}")
        break

    contador += 1

print(f"Adivinaste en {contador} intentos!")


'''6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.'''

iter = 100
for iter in range(100,0,-2):
    print(iter)


'''7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.'''

numeros = int(input("Ingrese un numero para sumarlo: "))
iter = 0
suma = 0
for iter in range(numeros):
    suma = suma + iter

print(f"La suma es: {suma}")
    

'''8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).'''

cantidad_numeros = 100
iter = 0
par = 0
positivos = 0
negativos = 0 
impares = 0 

for iter in range(cantidad_numeros):
    numeros = input("ingrese numeros al azal")
    if numeros < 0:
        negativos += 1
    else:
        positivos += 1
    if numeros % 2 == 0:
        par += 1
    else:
        impares += 1

print(f"Se ingresaron\n {negativos} numeros negativos\n {positivos} numeros positivos\n {par} numeros pares\n {impares} numeros impares")
    
'''9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).'''

cantidad_numeros = 10
iter = 0
suma = 0
for iter in range(cantidad_numeros):
    numeros = int(input("ingrese numeros al azar: "))
    suma += numeros
promedio = suma // cantidad_numeros    

print(f"El promedio es: {promedio}")


'''10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.'''

numero = int(input("Ingrese un numero: "))
invertido = 0
while numero > 0:
    digitos = numero % 10
    invertido = invertido * 10 + digitos
    numero //= 10
print(invertido)