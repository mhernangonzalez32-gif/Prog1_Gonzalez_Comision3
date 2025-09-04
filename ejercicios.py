from utiles_es import (
    titulo, ok, error, warn, info,
    pedir_texto, pedir_opcion, pedir_entero, pedir_float,
    pedir_email, pedir_cuit, confirmar, FlujoCancelado
)
from colorama import init, Fore, Style
import sys

# 1)
'''nombre_completo = pedir_texto("Ingrese el Nombre: ")
edad = pedir_entero("Ingrese edad: ",0,110)
ingresos = pedir_float("Ingresos anuales: ", 0)
mayor = edad > 65 

if ingresos < 500000:
    print(f"Nombre: {nombre_completo}\nIngresos: ${ingresos}\nEdad: {edad}\nIpuesto final: No paga impuestos ")
elif 500000 >= ingresos < 2000000:
    estado = ingresos * 0.1
    print(f"Nombre: {nombre_completo}\nIngresos: ${ingresos}\nEdad: {edad}\nIpuesto final: {estado}")
    if mayor: 
        print("al ser mayor de 65 anios, sus impuestos se ven reducidos al % 50")
        estado = estado / 2
        print("Impuesto final: {estado}")
elif 2000000 >= ingresos < 5000000:
    estado = ingresos * 0.2
    print(f"Nombre: {nombre_completo}\nIngresos: ${ingresos}\nEdad: {edad}\nIpuesto final: {estado}")
    if mayor: 
        print("al ser mayor de 65 anios, sus impuestos se ven reducidos al % 50")
        estado = estado / 2
        print("Impuesto final: {estado}")
elif ingresos >= 5000000:
    estado = ingresos *0.35
    print(f"Nombre: {nombre_completo}\nIngresos: ${ingresos}\nEdad: {edad}\nIpuesto final: {estado}")
    if mayor: 
        print("al ser mayor de 65 anios, sus impuestos se ven reducidos al % 50")
        estado = estado / 2
        print("Impuesto final: {estado}")'''

# 2)

from utiles_es import (pedir_texto, pedir_entero,ok,info, )

nombre = pedir_texto("Ingrese nombre completo: ")
legajo = pedir_entero("Numero de legajo: ", 0)
nota_1 = pedir_entero("Ingrese primera nota: ", 0,10)
nota_2 = pedir_entero("Ingrese la segunda: ", 0,10)
nota_3 = pedir_entero("Ingrese la tercera: ", 0,10)
promedio = (nota_1 + nota_2 + nota_3) / 3

if nota_1 < 4 or nota_2 < 4 or nota_3 < 4:
    estado = error("Desaprobado directo")
elif promedio < 8:
    estado = "Promocionado"    
elif 6 >= promedio < 8:
    estado = "Aprobado con final"
else:
    estado = "Desaprobado"

# --- Impresión de Resultados ---
info("\n--- Resultados del Alumno ---")
ok(f"Nombre: {nombre}")
ok(f"Legajo: {legajo}")
ok(f"Notas: {nota_1}, {nota_2}, {nota_3}")
ok(f"Promedio: {promedio:.2f}")
ok(f"Estado académico: {estado}")


#3
nombre_completo = pedir_texto("Ingrese nombre completo: ")




