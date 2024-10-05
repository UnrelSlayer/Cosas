def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: No se puede dividir por cero."

# Función principal de la calculadora
def calculadora():
    print("Bienvenido a la calculadora.")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Selecciona una opción (1-5): ") 

    while opcion != "5":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            resultado = suma(num1, num2)
            print("El resultado de la suma es:", resultado)
        elif opcion == "2":
            resultado = resta(num1, num2)
            print("El resultado de la resta es:", resultado)
        elif opcion == "3":
            resultado = multiplicacion(num1, num2)
            print("El resultado de la multiplicación es:", resultado)
        elif opcion == "4":
            resultado = division(num1, num2)
            print("El resultado de la división es:", resultado)
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

        print()  # línea en blanco para separar las operaciones

        # Mostrar nuevamente el menú
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")

    print("¡Gracias por usar la calculadora!")

# Ejecutar la calculadora
calculadora()
print("ingrese su numero" , input)