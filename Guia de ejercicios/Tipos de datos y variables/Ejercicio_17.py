#17.	Pide al usuario un número. Si está entre 1 y 100 (inclusive), muestra “Número válido”.
#  Si no, muestra “Número fuera de rango”.

numero = int(input("Ingrese un unmero en el rango 1-100"))
if numero > 0 and numero <= 100: 
    print("numero valido")
else: 
    print("Numero invalido ")