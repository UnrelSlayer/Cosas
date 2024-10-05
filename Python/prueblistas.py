lista_vacia = []

for suma in range(10):
    valor = (input("valor que va a agregar a la lista:"))
    lista_vacia.append(valor)
    print("el elemento que se añadio fue:",lista_vacia)

    
i = 0
while i < len(lista_vacia):
    print("valor en lista:",lista_vacia[i])
    i+=1
print(lista_vacia)
