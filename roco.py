from utiles_es import (
    titulo, ok, error, warn, info,
    pedir_texto, pedir_opcion, pedir_entero, pedir_float,
    pedir_email, pedir_cuit, confirmar, FlujoCancelado)
from colorama import init, Fore, Style


# 1)
nombre_completo = pedir_texto("Ingrese el Nombre: ")
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
        print("Impuesto final: {estado}")

# 2)
