#12.	Simula una calculadora: pide dos números y una operación (+, -, , /). 
# Usa condicionales para realizar la operación correspondiente.

try: 
    print("Calculadora")
    print("ingrese dos numeros: ")
    n1 = int(input())
    n2 = int(input())
    suma = n1 + n2
    resta = n1 - n2
    divi = n1 / n2
    mult = n1 * n2 
    print ("""Elije una operacion: 
        1.- suamr
        2.- resta
        3.- dividir
        4.- multiplicar
    """)
    opcion = int(input())

    if opcion == 1: 
        print (suma)
    elif opcion == 2:
        print(resta)
    elif opcion == 3: 
        print (divi)
    elif opcion == 4: 
        print (mult)
    else: 
        print("opcion no valida" )
except ZeroDivisionError: 
    print("no divida por 0 sea serio ")