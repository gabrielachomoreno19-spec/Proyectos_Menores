#4.	Solicita al usuario un número entero. Si es par, muestra “Es par”, si no, muestra “Es impar”.

numero = int(input("Ingrese un numero entero"))
if numero % 2 == 0: 
    print("Numero par: ")
else: 
    print("Numero impar: ")