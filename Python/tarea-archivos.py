def ganadores_tipo_torneo(nombre_archivo, tipo, año):
    ganadores = {}

    archivo = open(nombre_archivo,"r")
    for linea in archivo:
        
            linea = linea.strip().split(";")
            
            año_partido = int(linea[0])

            perdedor = linea[1]

            sets_perdedor = linea[2]

            ronda = linea[3]

            tipo_torneo = linea[4]

            torneo = linea[5]

            ganador = linea[6]

            sets_ganador = linea[7]

            if año_partido == año and tipo_torneo == tipo and ronda == "The Final":
                
                marcador = sets_ganador,sets_perdedor
                
                if ganador not in ganadores:
                    ganadores[ganador] = []
                
                ganadores[ganador].append([perdedor, torneo, marcador])
    archivo.close
    return ganadores

print(ganadores_tipo_torneo("datos_atp.csv", "Grand Slam", 2010))


def construir_resumen(nombre_archivo, año1, año2):
    victorias_por_año = {}

    archivo = open(nombre_archivo)
    for linea in archivo:
            linea = linea.strip()
            
            partes = linea.split(';')
            
            año_partido = int(partes[0])
            ganador = partes[6]
            
            if año1 <= año_partido <= año2:
                if año_partido not in victorias_por_año:
                    victorias_por_año[año_partido] = {}
                if ganador not in victorias_por_año[año_partido]:
                    victorias_por_año[año_partido][ganador] = 0
                victorias_por_año[año_partido][ganador] += 1

    nombre_resumen = "resumen_ATP_" + str(año1) + "-" + str(año2) + ".txt"
    archivo_resumen = open(nombre_resumen, "w")
    archivo_resumen.write("Asociación de Tenis de Pythonia\n")
    archivo_resumen.write("Resumen " + str(año1) + "-" + str(año2) + "\n\n")

    for año in range(año1, año2 + 1):
     if año in victorias_por_año:
         lista_jugadores = []
         for jugador in victorias_por_año[año]:
             lista_jugadores.append([jugador, victorias_por_año[año][jugador]])

         i = 0
         while i < len(lista_jugadores):
             j = i + 1
             while j < len(lista_jugadores):
                 if lista_jugadores[i][1] < lista_jugadores[j][1]:
                    lista_jugadores[i], lista_jugadores[j] = lista_jugadores[j], lista_jugadores[i]
                 j += 1
             i += 1

         
    archivo_resumen.write("Jugadores con más partidos ganados en " + str(año))
    for jugador_info in lista_jugadores[:10]:
            jugador, victorias = jugador_info
            archivo_resumen.write(jugador + " con " + str(victorias) + " triunfos\n")

    archivo_resumen.write("\n")
    archivo_resumen.close()
        
    return sum(len(victorias_por_año[año]) for año in range(año1, año2 + 1))

print(construir_resumen("datos_atp.csv", 2005, 2006))






