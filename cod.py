from utiles_es import (
    titulo, ok, error, warn, info,
    pedir_texto, pedir_opcion, pedir_entero, pedir_float,
    pedir_email, pedir_cuit, confirmar, FlujoCancelado
)
from colorama import init, Fore, Style
import sys
import random

numero = int(input("Ingrese un numero: "))
invertido = 0
while numero > 0:
    digitos = numero % 10
    invertido = invertido * 10 + digitos
    numero //= 10
print(invertido)