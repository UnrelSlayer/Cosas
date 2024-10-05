def repetidos(A,B):
    for repetidos in A and B:
        if repetidos in A and B:
            return repetidos

listaA =  [1, 5, 11, 0, 6, 4, 11, 14, 12, 12]
listaB = [12, 7, 3, 12, 0, 7, 9, 10, 5, 3]

print(repetidos(listaA,listaB))
