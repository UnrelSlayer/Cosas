#area de un triangulo
from math import sqrt
a = float(input("ingrese el lado A:"))
b = float(input("ingrese el lado B:"))
c = float(input("ingrese el lado C:"))
s = round(a + b+ c,2) / 2
area = round(sqrt(s * (s-a) * (s-b) * (s-c)),2)
print(area)