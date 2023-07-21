import re

archivo = input("Ingrese el nombre del archivo: ")
suma = 0
contador = 0

with open(archivo) as f:
    for linea in f:
        match = re.search(r"New Revision: (\d+)", linea)
        if match:
            numero = int(match.group(1))
            suma += numero
            contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"El promedio de los números encontrados es {promedio}.")
else:
    print("No se encontraron líneas con el formato especificado.")
