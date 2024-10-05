def original(abreviada):
    salida = ""
    i = 0
    while i < len(abreviada):
        numero = int(abreviada[i])
        letra = abreviada[i+1]
        salida += letra * numero
        i += 2
    return salida
abr = input("Ingrese palabra abreviada: ")
print("Original:", original(abr))