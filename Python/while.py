def codigo_palabra(codigo):
    palabra_descencriptada = ""
    indice = len(codigo) -1
    while indice >= 0:
        palabra_descencriptada += codigo[indice]
        indice -= 2
    return palabra_descencriptada
    
print(codigo_palabra('aczaarltp')) 
print(codigo_palabra('oagriatgrreov')) 


