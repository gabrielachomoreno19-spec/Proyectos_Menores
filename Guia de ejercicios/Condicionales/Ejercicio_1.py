#1.	Pide al usuario que ingrese un número entero y muestra si es positivo.
numero = int(input("ingrese un numero: "))
if numero > 0: 
    print("El numero es positivo")
elif numero == 0: 
    print("El numero es 0")
else: 
    print("El numero es negativo")