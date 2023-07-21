import re

archivo = input("Ingrese el nombre del archivo: ")
expresion = input("Ingrese la expresión regular a buscar: ")
contador = 0

with open(archivo) as f:
    for linea in f:
        if re.search(expresion, linea):
            contador += 1

print(f"Se encontraron {contador} líneas que coinciden con la expresión regular '{expresion}'.")
