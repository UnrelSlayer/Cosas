def num_digitos(n):
   nd = 1
   while n>9:
      nd += 1
      n = n//10
   return nd

num = 53
resultado = num_digitos(num)
print(resultado)