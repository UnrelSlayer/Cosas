
nombre_persona = input("ingrese su nombre:")
nombre_mascota = input("ingrese el nombre de su mascota:")
caracteres_especiales = "¡!¿?@#$%&_-+*=|{}[].,;:<>/\~^''" + '"'
letras = "abcdefghijklmnñopqrstuvwxyz."
mayusculas = letras.upper
numeros = "0123456789"
espacio = " "
contraseña = ""
while contraseña != "Fin" :
    contraseña = input("ingrese una contraseña:")

    if  len(contraseña) < 10 :
        print("contraseña muy corta debe tener 10 caracteres")
    
    for M in contraseña:
        if M in mayusculas






      