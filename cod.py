from utiles_es import (pedir_texto, pedir_entero, pedir_float, warn,titulo,ok,error,info, )

nombre = pedir_texto("Ingrese nombre completo: ")
legajo = pedir_entero("Numero de legajo: ", 0)
nota_1 = pedir_entero("Ingrese primera nota: ", 0,10)
nota_2 = pedir_entero("Ingrese la segunda: ", 0,10)
nota_3 = pedir_entero("Ingrese la tercera: ", 0,10)
promedio = (nota_1 + nota_2 + nota_3) / 3

if nota_1 < 4 or nota_2 < 4 or nota_3 < 4:
    estado = "Estado academico: Desaprobado directo"
elif promedio < 8:
    estado = "Estado academico: Promocionado"    
elif 6 >= promedio < 8:
    estado = "Estado academico: Aprobado con final"
else:
    estado = "Estado academico: Desaprobado"

# --- Impresión de Resultados ---
info("\n--- Resultados del Alumno ---")
ok(f"Nombre: {nombre}")
ok(f"Legajo: {legajo}")
ok(f"Notas: {nota_1}, {nota_2}, {nota_3}")
ok(f"Promedio: {promedio:.2f}")
ok(f"\nEstado académico: {estado}")

