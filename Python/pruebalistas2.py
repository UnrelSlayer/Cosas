def contar_veces(lista, elemento):
   n = 0
   while elemento in lista:
      lista.remove(elemento)
      n += 1
   return n
L = [1,2,1,1,1,2,2,1,1]
print(contar_veces(L,2))
print(contar_veces(L,2))