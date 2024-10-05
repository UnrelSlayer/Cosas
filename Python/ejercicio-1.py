#costo por viaje
kms_recorrer = float(input("ingrese los kilometros a recorrer:"))
kms_litro = float(input("ingrese los kilometros por litro:"))
costo_litro = float(input("ingrese el costo por litro:"))
total = round(kms_recorrer / kms_litro * costo_litro,2)
print(total)
