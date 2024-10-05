
nombre_usuario = input("Ingresa tu nombre: ")
nombre_mascota = input("Ingresa el nombre de tu mascota: ")
numeros = "0123456789"
letras = "abcdefghijklmnñopqrstuvwxyz."
salir = False

while salir != True:
    
    contraseña = input("Ingresa una contraseña (o escribe FIN para salir): ")

    if contraseña.upper() == "FIN":
        salir = True
    else:
        tiene_minuscula = False
        tiene_mayuscula = False
        tiene_numero = False
        tiene_especial = False
        tiene_nombre = nombre_usuario.lower() in contraseña.lower() or nombre_mascota.lower() in contraseña.lower()
        contiene_patron_letras = False
        contiene_patron_digitos = False

       
        for i in range(len(contraseña)):
            if contraseña[i]in letras.lower():
                tiene_minuscula = True
            elif contraseña[i] in letras.upper():
                tiene_mayuscula = True
            elif contraseña[i]in numeros:
                tiene_numero = True
            elif contraseña[i] in "¡!¿?@#$%&_-+*=|{}[].,;:<>/\\~^'\"":
                tiene_especial = True

            
            if i < len(contraseña) - 4:
                if len(set(contraseña[i:i+5])) == 1 and contraseña[i].isalpha():
                    contiene_patron_letras = True
                elif len(set(contraseña[i:i+5])) == 1 and contraseña[i].isdigit():
                    contiene_patron_digitos = True

        
        if len(contraseña) < 10:
            print("La contraseña debe tener al menos 10 caracteres.")
        elif not tiene_minuscula:
            print("La contraseña debe contener al menos una letra minúscula.")
        elif not tiene_mayuscula:
            print("La contraseña debe contener al menos una letra mayúscula.")
        elif not tiene_numero:
            print("La contraseña debe contener al menos un dígito numérico.")
        elif not tiene_especial:
            print("La contraseña debe contener al menos un caracter especial.")
        elif tiene_nombre:
            print("La contraseña no puede contener el nombre del usuario ni el de su mascota.")
        elif contiene_patron_letras:
            print("La contraseña no puede contener patrones de repetición de 5 letras iguales.")
        elif contiene_patron_digitos:
            print("La contraseña no puede contener patrones de repetición de 5 dígitos iguales.")
        else:
            print("Contraseña válida.")
