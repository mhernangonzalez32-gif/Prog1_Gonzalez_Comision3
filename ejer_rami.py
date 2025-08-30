#EJERCICIO 1
nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apellido: ")
nombre_completo = str(f"{nombre} {apellido}").capitalize()
edad = input("Ingrese las edad del postulante: ")
promedio = float(input("Ingrese su promedio, 0 - 10: "))
ingresos = int(input("Ingresos familiares mensuales: "))

if promedio < 6.0:
    estatus = "RECHAZADO"
elif promedio >= 6:
    if ingresos < 300000:
        estatus = "Beca completa"
    elif ingresos >= 300000 and ingresos <= 600000:
        estatus = "Media beca"
    else:
        estatus = "Rechazado"

print(f"Nombre completo: {nombre_completo}, {edad} años \n Promedio: {promedio} \n ingresos: {ingresos} \n Resultado: {estatus}")

#2









#3)...
nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apellido: ")
nombre_completo = str(f"{nombre}, {apellido}").capitalize()
cuil = input("Ingrese su numero de Cuilt: ")
ingresos = float(input("Ingresos mensuales:"))
antiguedad_lab = int(input("Ingrese su antiguedad laboral: "))
historial = ["bueno","regular","malo"]
hist_crediticio = input("Ingrese el Historial crediticio, BUENO / REGULAR / MALO: ").lower()

if hist_crediticio == historial[2]:
    estado = "RECHAZADO"
elif ingresos < 200000:
    estado = "RECHAZADO"
elif ingresos >= 200000 and antiguedad_lab < 2:
    estado = "Puede acceder hasta $500.000"
elif ingresos >= 200000 and antiguedad_lab >= 2:
    if hist_crediticio == historial[1]:
        estado = "Puede acceder hasta $1.0000.000"
    else:
        estado = "Puede acceder hasta $3.000.000"
print("/n")
print(f"Cliente: {nombre_completo}")
print(f"Cuil: {cuil}" )
print(f"Ingresos: {ingresos}")
print(f"Historial: {hist_crediticio}")
print(f"monto aprobado: {estado}")