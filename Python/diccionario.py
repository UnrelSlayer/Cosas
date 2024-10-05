verdulería = {
   'Brócoli': [900, 10],
   'Pimentón': [800, 5],
   'Limones': [1500, 0],
   'Lechuga': [700, 10],
   'Palta': [3800, 7],
   'Tomates': [1200, 20],
   'Pepino': [500, 0],
   'Zanahorias': [700, 12],
   'Zapallo italiano': [450, 8],
   'Papas': [950, 25],
   'Frutillas': [3400, 2],
   'Peras': [1500, 0],
   'Manzanas': [1600, 4],
   'Naranjas': [1800, 12],
   'Plátanos': [1100, 3],
   'Kiwis': [2800, 0],
   'Mandarinas': [2200, 4]
   }

def validar_existencia(dicc,producto):
        if producto not in dicc:
            return "producto no existe"
        else:
            return ("el producto {} si existe".format(producto))

def determinar_precio(dicc,producto):
    for key in dicc:
        if str(key) == producto:
            return dicc[key][0]
        
def determinar_stock(dicc,producto):
    for key in dicc:
     if validar_existencia(dicc,producto):
         return dicc[key][1]
        
        
    
    

print(determinar_precio(verdulería,"Kiwis"))
print(validar_existencia(verdulería,"Tomates"))
print(determinar_stock(verdulería,"Kiwis"))