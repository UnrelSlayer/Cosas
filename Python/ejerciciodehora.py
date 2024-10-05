"""Escriba un programa que reciba la hora actual y una cantidad de horas que debe sumar. El programa debe
imprimir cuantos días pasaran y que hora será."""

hora_actual = int(input("ingrese la hora actual: "))
cantidad_de_horas_sumadas = int(input("ingrese las horas que va a sumar: "))
horas_sumadas = (hora_actual + cantidad_de_horas_sumadas) // 24
hora_a_futuro = (hora_actual +cantidad_de_horas_sumadas) % 24
print("son",horas_sumadas ,"dias y seran las:",hora_actual)

