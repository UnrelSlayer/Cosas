def filtrar(original, eliminar):
    resultado = []
    elementos_repetidos = []
    
    for elemento in original:
        if elemento not in eliminar and elemento not in elementos_repetidos:
            resultado.append(elemento)
            elementos_repetidos.append(elemento)
    
    return resultado

original = [1, 2, 3, 1, 2, 3, 1, 2, 3]

eliminar = [1, 3]

print(filtrar(original,eliminar))

