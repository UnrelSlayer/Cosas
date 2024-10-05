muerte = True
song = True
contador_m = 0
contador_s = 0
paciencia = int(input())
while muerte == True and song == True:
    accion = str(input())
    if accion == "si":
        contador_m +=1
        contador_s = 0
        paciencia -=1 
    elif accion == "no":
        contador_m = 0
        contador_s +=1
    if contador_m == 3 or paciencia == 0:
        muerte = False
        print("Aplicando correctivo avalado por las autoridades de esta gran nación. ¡¡ PSSSST PSSSST !!")
    if contador_s == 5:
        song = False
        print("Duérmete pythoncito, duérmete ya, que viene el robotrón y te rociara")
