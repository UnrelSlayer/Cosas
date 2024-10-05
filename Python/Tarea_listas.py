recomendaciones = [
["Pad thai", "Costillar cantones", "Lasagna"],
["Ceviche", "Lomo saltado", "Pastel de choclo"],
["Pastel de choclo", "Cazuela", "Ceviche"],
["Lasagna"],
["Fettuccine al pesto", "Lasagna"],
["Ceviche", "Pastel de choclo", "Lasagna", "Cazuela"]
]


lista_recomendados2 = [                                                       # nota no tome en cuenta esta lista nueva solo la cree para probar 
["Pescado frito entero" ,"Ensalada a la chilena", "papas fritas"],            # las funciones con otras listas  xd
["chorrillana"],
["Carpaccio de lomito."],
["Carbonada","Ensalada a la chilena","Humitas"],
["Porotos granados","Sopaipillas"],
["Sushi"],
["hamburguesa","papas fritas"],
["completo","papas fritas"]
]

def mas_popular(lista):
    platos = []
    conteos_plato = []
    
    for sublista in lista:
        for plato in sublista:
            if plato in platos:
                indice = platos.index(plato)
                conteos_plato[indice] += 1
            else:
                platos.append(plato)
                conteos_plato.append(1)
    
 
    max_recomendaciones = max(conteos_plato)
    indice_max = conteos_plato.index(max_recomendaciones)
    plato_mas_popular = platos[indice_max]
    
    
    return [plato_mas_popular,max_recomendaciones]


def similares(plato_base, recomendaciones):
    
    platos_similares = []
    conteos_similares = []
    
    for sublista in recomendaciones:
        if plato_base in sublista:
            for plato in sublista:
                if plato != plato_base:
                    if plato in platos_similares:
                        
                        indice = platos_similares.index(plato)
                        conteos_similares[indice] += 1
                    else:
                        
                        platos_similares.append(plato)
                        conteos_similares.append(1)
    
    
    for i in range(len(conteos_similares)):
        for j in range(0, len(conteos_similares) - i - 1):
            if conteos_similares[j] < conteos_similares[j + 1]:
               
                conteos_similares[j], conteos_similares[j + 1] = conteos_similares[j + 1], conteos_similares[j]
                
                platos_similares[j], platos_similares[j + 1] = platos_similares[j + 1], platos_similares[j]
    
   
    return platos_similares


print(mas_popular(recomendaciones))
print("---------------------------")
print(similares("Lasagna", recomendaciones))
print("                                     ")
print(mas_popular(lista_recomendados2))
print("--------------------")
print(similares("papas fritas",lista_recomendados2))