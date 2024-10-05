peso_p = 112
peso_m = 75
payasos = int(input( "cuantos payasos quiere:" ))
muñecas = int(input( "cuantas muñecas quiere:" ))
print("hay que tener en cuenta el peso de los productos y su cantidad")
peso_de_productos = int(payasos*peso_p),int(muñecas*peso_m)
total_de_payasos_y_muñecas = payasos+muñecas
print("su cantidad de payasos y muñecas es" , total_de_payasos_y_muñecas)
print("y su peso correspondiente al total es",peso_de_productos ,"g")